from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser
from rest_framework import viewsets, authentication, permissions, generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404
import traceback
from .models import *
from .serializer import *


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class PollList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser|ReadOnly]
    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Poll.objects.all()
        else:
            queryset = Poll.objects.filter(date_end__gte=timezone.now())
        return queryset
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser|ReadOnly]
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionsList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser|ReadOnly]
    def get_queryset(self):
        queryset = Questions.objects.filter(poll=self.kwargs["poll"])
        return queryset

    # pass arguments to serializer
    def get_serializer_context(self):
        data = {
            'request': self.request,
            'view': self,
            'format': self.request.GET.get('format') if self.request and self.request.GET else None,
            "poll_id": self.kwargs.get('poll'),
        }
        return data

    serializer_class = QuestionsSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        queryset = Questions.objects.filter(poll=self.kwargs["poll"])
        return queryset
    serializer_class = QuestionsSerializer


class CreateVote(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, poll, questions_pk):
        if request.data:
            user_pk = request.data.get("user_pk")
            answer = request.data.get("answer")
        else:
            user_pk = None
            answer = None

        data = {'question': questions_pk, 'poll': poll, 'answer': answer, 'user': user_pk}

        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            try:
                vote = serializer.save()
            except:
                data = {'errors': str(traceback.format_exc())}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            # redefine errors
            if 'non_field_errors' in data:
                if 'poll, user, question must make a unique set' in data['non_field_errors'][0]:
                    data = {'errors': 'You have already answered this question.'}
            else:
                    data = {'errors': data}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        # else if serializer.is_valid()
    # def post
# class CreateVote


class VoteList(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]  # add |ReadOnly for anonimouses

    def get_queryset(self):
        # self.kwargs = {'poll_pk': None, 'user_pk': '1'}
        polls_ids = [ r[0] for r in Vote.objects.filter(user=self.kwargs['user_pk']).values_list('poll').distinct() ]
        if self.kwargs['poll_pk']:
            queryset = Poll.objects.filter(pk=self.kwargs['poll_pk'])
        else:
            queryset = Poll.objects.filter(id__in=polls_ids).order_by('id')
        return queryset

    # pass arguments to serializer
    def get_serializer_context(self):
        data = {
            'request': self.request,
            'view': self,
            'format': self.request.GET.get('format'),
            "poll_pk": self.kwargs.get('poll_pk'),
            "user_pk": self.kwargs.get('user_pk'),
        }
        return data

    serializer_class = PollListSerializer
# class VoteList
