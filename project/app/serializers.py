from rest_framework import serializers

from datetime import datetime

class CreateNoteTableSerializer(serializers.Serializer):
    table_name = serializers.CharField(max_length=100)
    field1 = serializers.CharField(max_length=100)
    field2 = serializers.CharField(max_length=100)
    



class CreteNotesSerializers(serializers.Serializer):
    noteid = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)

    createdAt = serializers.DateTimeField(read_only=True)
    updatedAt = serializers.DateTimeField(read_only=True)

    def validate(self, data):
        data['createdAt'] = datetime.now()
        data['updatedAt'] = datetime.now()
        return data
    

class GetAllNotesSerializers(serializers.Serializer):
    noteid = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)

    createdAt = serializers.DateTimeField(read_only=True)
    updatedAt = serializers.DateTimeField(read_only=True)

class GetNotesSerializer(serializers.Serializer):
    noteid = serializers.CharField(max_length=100)
   
    
    