import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from decimal import Decimal
import time
from ..serializers import CreateNoteTableSerializer
from aws import *
from rest_framework import generics,status
from errormessage import Errormessage
from rest_framework.response import Response


    
class CreateNoteTablePost(generics.GenericAPIView):
    serializer_class = CreateNoteTableSerializer
    # permission_classes = (IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        try:
            table_name = request.data.get('table_name')
            field1 = request.data.get('field1')
            field2 = request.data.get('field2')
        
                

            client = boto3.client(
                table_name,
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token if aws_session_token else None
            )

            
            table = client.create_table(
                TableName='Notes',
                KeySchema=[
                    {
                        'AttributeName': field1,
                        'KeyType': 'HASH'  # Partition key
                    },
                    {
                        'AttributeName': field2,
                        'KeyType': 'RANGE'  # Sort key
                    },
                    
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': field1,
                        'AttributeType': 's'
                    },
                    {
                        'AttributeName': field2,
                        'AttributeType': 'S'
                    },

                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            # if __name__ == '__main__':

            print("Table status:{}".format(table))

            time.sleep(30)


            response_data = {
                            "message": "Table Successfully Created in dynamodb",
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
