import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from decimal import Decimal
import time
from ..serializers import CreteNotesSerializers
from aws import *
from rest_framework import generics,status
from errormessage import Errormessage
from rest_framework.response import Response


    
class InsertDataintoDynamoDB(generics.GenericAPIView):
    serializer_class = CreteNotesSerializers
    # permission_classes = (IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        try:
            noteid = request.data.get('noteid')
            title = request.data.get('title')
            content = request.data.get('content')
            createdAt = request.data.get('createdAt')
            updatedAt = request.data.get('updatedAt')
        
                

            client = boto3.client(
                'dynamodb',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token if aws_session_token else None
            )

            
            # def put_movie(title, year, plot, rating):
            result = client.put_item(    TableName='dynamodb',
            Item={
                    'noteid': {
                        'N': "{}".format(noteid),
                    },
                    'title': {
                        'S': "{}".format(title),
                    },
                    'content': {
                        "S": "{}".format(content),
                    },
                    'createdAt': {
                        "S": "{}".format(createdAt),
                    },
                    'updatedAt': {
                        "S": "{}".format(updatedAt),
                    }
                }
            )

            print("Insert in to DynamoDB succeeded............")
            pprint(result, sort_dicts=False)


            response_data = {
                            "message": "Data uploaded Successfully",
                            "Result" : True,
                            'Status' : 200,
                            'HasError' : False
                        }
            return Response(response_data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            response_data = {
                    "message":Errormessage(e),
                    "Result" : False,
                    'Status' : 400,
                    'HasError' : True
                }
            return Response(response_data, status=status.HTTP_201_CREATED)
