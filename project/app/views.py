from django.shortcuts import render

# Create your views here.

# from app_crud.create_table import CreateNoteTablePost
# from app_crud.put_notes import InsertDataintoDynamoDB

# CreateNoteTablePost()
# InsertDataintoDynamoDB()


from app.app_crud.create_table import CreateNoteTablePost
from app.app_crud.put_notes import InsertDataintoDynamoDB
from app.app_crud.get_notes import GetNotes
from app.app_crud.get_all_notes import GetAllNotes
from app.app_crud.update_notes import UpdateNotes

CreateNoteTablePost()
InsertDataintoDynamoDB()
GetNotes()
GetAllNotes()
UpdateNotes()