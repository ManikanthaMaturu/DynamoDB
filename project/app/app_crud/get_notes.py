import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from decimal import Decimal
import time
from ..serializers import GetNotesSerializer
from aws import *
from rest_framework import generics,status
from errormessage import Errormessage
from rest_framework.response import Response


    
class GetNotes(generics.GenericAPIView):
    serializer_class = GetNotesSerializer
    # permission_classes = (IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        try:
            noteid = request.data.get('noteid')
            
        
                

            client = boto3.client(
                'dynamodb',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token if aws_session_token else None
            )

            
            # def put_movie(title, year, plot, rating):
            res = client.get_item(       
                    TableName='dynamodb',
                    Key={
                            'noteid': {
                                    'N': "{}".format(noteid),
                            }
                            
                        }
                    )
        
            if res:
                print("Get an item from DynamoDB succeeded............")
                pprint(res, sort_dicts=False)


                response_data = {
                                "message": "Data uploaded Successfully",
                                "Result" : True,
                                'Status' : 200,
                                'HasError' : False
                            }
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
             
                response_data = {
                        "message":'There is no data with this noteid',
                        "Result" : False,
                        'Status' : 400,
                        'HasError' : True
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
