from django.urls import path, re_path, include
from . import views

app_name = 'poll'

urlpatterns = [
    re_path(r"^vote/(?P<user_pk>[0-9]+)/(?:(?P<poll_pk>[0-9]+)/?)?", views.VoteList.as_view()),
    path("<int:poll>/questions/<int:questions_pk>/vote/", views.CreateVote.as_view()),
    path("<int:poll>/questions/<int:pk>/", views.QuestionDetail.as_view()),
    path("<int:poll>/questions/", views.QuestionsList.as_view()),
    path("<int:pk>/", views.PollDetail.as_view()),
    path('', views.PollList.as_view()),
]

'''
GET polls list:
http://192.168.1.208:8000/poll/
http://192.168.1.208:8000/poll/?format=json

POST new poll:
Example:
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Basic YWRtaW46MTEx' -i 'http://192.168.1.208:8000/poll/' --data '{
    "id": 0,
    "name": "Тест 1",
    "date_end": "2020-05-31T14:01:18Z",
    "note": "описание"
}'

Example with questions embedded (id of question ignored):
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Basic YWRtaW46MTEx' -i 'http://192.168.1.208:8000/poll/' --data '{
    "id": 0,
    "name": "Тест 1",
    "date_end": "2020-05-31T14:01:18Z",
    "note": "описание",
    "questions": [
        {
            "id": 2,
            "question_type": "text",
            "question_text": "Имя",
            "question_options": ""
        },
        {
            "id": 2,
            "question_type": "text",
            "question_text": "Фамилия",
            "question_options": ""
        }
    ]
}'


GET poll with id=1 (questions embedded)
http://192.168.1.208:8000/poll/1/
http://192.168.1.208:8000/poll/1/?format=json

DELETE http://192.168.1.208:8000/poll/24/


GET questions only of poll id=1
http://192.168.1.208:8000/poll/1/questions/
http://192.168.1.208:8000/poll/1/questions/?format=json

GET question id=2 of poll id=1
http://192.168.1.208:8000/poll/1/questions/2/
http://192.168.1.208:8000/poll/1/questions/2/?format=json

DELETE
http://192.168.1.208:8000/poll/1/questions/37/

POST new question into poll id=1
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Basic YWRtaW46MTEx' -i 'http://192.168.1.208:8000/poll/1/questions/' --data '{
    "poll": 1,
    "id": 0,
    "question_type": "variants",
    "question_text": "Когда рак на горе ...?",
    "question_options": "Прыгент, Сдохнет, Свистнет"
}'


POST vote (answers to poll questions)
POST answer to question id=2 in poll id=1
http://192.168.1.208:8000/poll/1/questions/2/vote/
curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Basic dGVzdDp0ZXN0' -i 'http://192.168.1.208:8000/poll/1/questions/2/vote/' --data '{
    "user_pk": 2,
    "answer": "test"
}'


GET poll with user answers
GET all polls (with questions and answers) for user id=1
http://192.168.1.208:8000/poll/vote/1/

GET answers) for user id=2 on poll id=1
http://192.168.1.208:8000/poll/vote/2/1
'''
