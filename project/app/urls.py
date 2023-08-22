from django.urls import path

from .views import *

urlpatterns = [
    path('CreateNoteTablePost/', CreateNoteTablePost.as_view(), name='CreateNoteTable'),
    path('InsertDataintoDynamoDB/', InsertDataintoDynamoDB.as_view(), name='InsertDataintoDynamoDB'),

]


