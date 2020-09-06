from rest_framework import serializers
from .models import Poll, Questions, Vote
from django.utils import timezone
from django.db import models


class QuestionsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() # MUST BE for correct id mapping in PollSerializer

    def validate(self, data):
        # becouse we remove field 'poll' from fields list, we need hand made insert poll id into data
        if not data.get('poll_id'):
            data['poll_id'] = self.context.get('poll_id')
        # to prevent creation record with id=0 remove field 'id' if it = 0
        if data.get('id') == 0:
            del data['id']
        return data

    class Meta:
        model = Questions
        # remove field 'poll' for best look only :)
        fields = ['id', 'question_type', 'question_text', 'question_options']
# class QuestionsSerializer


class PollSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(PollSerializer, self).__init__(*args, **kwargs)

        # little hack for remove questions from polls list
        if len(args) and type(args[0]) is models.query.QuerySet:
            self.fields.pop('questions')
    # def __init__

    questions = QuestionsSerializer(many=True, required=False)  # questions is writable

    # extract relations (Questions)
    def get_questions(self, data):
        try:
            questions_data = data.pop('questions')
        except:
            questions_data = None
        '''
        questions_data=[
            OrderedDict([('id', 2), ('question_type', 'text'), ('question_text', 'Имя'), ('question_options', ''), ('poll', <Poll: Тест 1>)]),
            OrderedDict([('id', 3), ('question_type', 'variant'), ('question_text', '2 * 2 ='), ('question_options', '3,4,5'), ('poll', <Poll: Тест 1>)]),
            OrderedDict([('id', 4), ('question_type', 'variants'), ('question_text', 'Цвет'), ('question_options', 'Красный, Зелёный, Синий'), ('poll', <Poll: Тест 1>)])
        ]
        '''
        return questions_data
    # def get_questions

    def create(self, validated_data):
        # extract questions from data if exists
        questions_data = self.get_questions(validated_data)

        # create poll before creating questions
        poll = Poll.objects.create(**validated_data)

        # create questions for poll if exists
        if questions_data:
            for question in questions_data:
                data = {item:question[item] for item in question}
                data['poll_id'] = poll.id
                # extract id if exists becouse user can forgot reset it
                id = data.pop('id')
                Questions.objects.create(**data)
            # for question in questions_data
        # if questions_data

        return poll
    # def create

    def update(self, instance, validated_data):
        questions_data = self.get_questions(validated_data)

        instance.name = validated_data.get('name', instance.name)
        #instance.date_start = validated_data.get('date_start', instance.date_start)
        instance.date_end = validated_data.get('date_end', instance.date_end)
        instance.note = validated_data.get('note', instance.note)
        instance.save()

        # modify Questions
        if questions_data:
            ids = []    # existing id
            for question in questions_data:
                # convert for extract id filed
                data = {item:question[item] for item in question}
                data['poll_id'] = instance.id
                id = data.pop('id')

                if id:
                    #Questions.objects.filter(id=id).update(**question) - DO NOT USE: overvrite id field
                    Questions.objects.filter(id=id).update(**data)
                    ids.append(id)
                else:
                    q = Questions.objects.create(**data)
                    ids.append(q.id)
            # for question in questions_data

            # delete all other ids
            Questions.objects.filter(poll=instance).exclude(id__in=ids).delete()
        # if questions_data

        return instance
    # def update

    class Meta:
        model = Poll
        fields = '__all__'
        read_only_fields = ('date_start',)
# class PollSerializer


'''
Used only for filter list of votes
'''
class FilteredVoteSerializer(serializers.ListSerializer):
    '''
    By default the to_representation method calls data.all() on the nested queryset
    But we will filter the data by the parameters passed in the context
    there is also a context['poll_pk'] but we don’t need it
    '''
    def to_representation(self, data):
        data = data.filter(user=self.context['user_pk'])
        data_filtered = super(FilteredVoteSerializer, self).to_representation(data)
        # and we need only 2 fields in this mode
        data_returned = {
            # [0] becouse we allowed only one answer to the question
            'user': data_filtered[0].get('user') if data_filtered else None,
            'answer': data_filtered[0].get('answer') if data_filtered else None,
        }
        return data_returned
# class FilteredVoteSerializer


'''
Used for create vote & filtering votes
'''
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        '''
        To filter data we subclassing ListSerializer as the meta list_serializer_class on the nested Serializer
        context will be passed to FilteredVoteSerializer automatically
        '''
        list_serializer_class = FilteredVoteSerializer
        model = Vote
        fields = '__all__'
# class VoteSerializer


class QuestionsListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(QuestionsListSerializer, self).__init__(*args, **kwargs)

        '''
        We need filtering votes only requested user
        and we pass filter params to VoteSerializer
        '''
        self.fields['votes'] = VoteSerializer(
            many=True,
            read_only=True,
            required=False,
            context={
                'poll_pk': self.context.get('poll_pk'),
                'user_pk': self.context.get('user_pk'),
            }
        )
    # def __init__

    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'question_type', 'question_options', 'votes']
# class QuestionsListSerializer


class PollListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(PollListSerializer, self).__init__(*args, **kwargs)

        # get arguments from context
        poll_pk = self.context.get('poll_pk')

        self.fields['questions'] = QuestionsListSerializer(
            many=True,
            read_only=True,
            required=False,
            # and pass to serializer
            context={
                'poll_pk': poll_pk,
                'user_pk': self.context.get('user_pk'),
            }
        )
    # def __init__

    class Meta:
        model = Poll
        fields = ['id', 'name', 'note', 'date_start', 'date_end', 'questions']
# class PollListSerializer
