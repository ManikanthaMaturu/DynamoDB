from django.urls import path

from .views import *

urlpatterns = [
    path('CreateNotesTable/', CreateNoteTablePost.as_view(), name='CreateNoteTable'),
    path('CreateNotes/', InsertDataintoDynamoDB.as_view(), name='InsertDataintoDynamoDB'),
    path('GetNotes/', GetNotes.as_view(), name='GetNotes'),
    path('GetAllNotes/', GetAllNotes.as_view(), name='GetAllNotes'),
    path('UpdateNotes/', UpdateNotes.as_view(), name='UpdateNotes'),

]


