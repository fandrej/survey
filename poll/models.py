from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
'''
After change do:
python manage.py makemigrations
python manage.py migrate
'''

'''
Атрибуты опроса: название, дата старта, дата окончания, описание.
'''
class Poll(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateTimeField(default=timezone.now, null=False)
    date_end = models.DateTimeField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


'''
Атрибуты вопросов:
    текст вопроса,
    тип вопроса:
        ответ текстом,
        ответ с выбором одного варианта,
        ответ с выбором нескольких вариантов
'''
class Questions(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    QUESTION_TYPE = [
        ('text', 'Ответ текстом'),
        ('variant', 'Ответ с выбором одного варианта'),
        ('variants', 'Ответ с выбором нескольких вариантов'),
    ]
    question_type = models.CharField(
        max_length=10,
        choices=QUESTION_TYPE,
        default='text',
    )
    question_text = models.CharField(max_length=100, null=False, blank=False)
    question_options = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.TextField(null=False, blank=False)

    class Meta:
        unique_together = ("poll", "user", "question")
