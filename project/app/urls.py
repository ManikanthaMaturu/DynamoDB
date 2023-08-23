from django.urls import path

from .views import *

urlpatterns = [
    path('CreateNotesTable/', CreateNoteTablePost.as_view(), name='CreateNoteTable'),
    path('CreateNotes/', InsertDataintoDynamoDB.as_view(), name='InsertDataintoDynamoDB'),

]


