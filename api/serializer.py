from rest_framework import serializers
from django.contrib.auth.models import User
from notes.models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title' , 'description','user','modified']

