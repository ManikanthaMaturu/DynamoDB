from django.shortcuts import render

# Create your views here.

# from app_crud.create_table import CreateNoteTablePost
# from app_crud.put_notes import InsertDataintoDynamoDB

# CreateNoteTablePost()
# InsertDataintoDynamoDB()


from app.app_crud.create_table import CreateNoteTablePost
from app.app_crud.put_notes import InsertDataintoDynamoDB

CreateNoteTablePost()
InsertDataintoDynamoDB()