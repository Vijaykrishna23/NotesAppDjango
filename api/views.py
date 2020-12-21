from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializer import NoteSerializer, UserSerializer
from django.contrib.auth.models import User
from notes.models import Note
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.forms.models import model_to_dict

# Create your views here.
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def register(req):
    serializer = UserSerializer(data=req.data)
    if serializer.is_valid():
        User.objects.create_user(username=serializer.data['username'],password=serializer.data['password'])
        return Response(serializer.data)
    
    
    return Response(serializer.errors)


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(req):

    uname = req.data['username']
    password = req.data['password']

    serializer = UserSerializer(req.data)

    user = auth.authenticate(username=uname,password=password)
    if user is not None:
        auth.login(req,user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'})

@api_view(['GET'])
def get_current_user(req):
    return Response(req.user.username)


@api_view(['GET'])
def logout(req):
    serializer = UserSerializer(req.user)
    if serializer.is_valid:
        auth.logout(request=req)
        return Response(serializer.data)
    
    return Response({'error': 'User not logged in'})

@api_view(['GET'])
def get_notes(req):

    notes = Note.objects.filter(user=req.user)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one_note(req, id):
    note = Note.objects.filter(pk=id)[0]
    if note is None:
        return Response({"error": "note not found"})
    
    serializer = NoteSerializer(data=model_to_dict(note))

    if serializer.is_valid():
        return Response(serializer.data)

    return Response(serializer.errors)


@api_view(['POST'])
def create_note(req):

    if not req.user.is_authenticated:
        return Response({'error': 'User not logged in'})
    
    serializer = NoteSerializer(data=req.data)
    serializer.initial_data['user'] = req.user.id
    if serializer.is_valid():
        Note.objects.get_or_create(title=req.data['title'],description=req.data['description'],user=req.user)
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['PUT'])
def update_note(req , id):

    if not req.user.is_authenticated:
        return Response({'error': 'User not logged in'})
    
    serializer = NoteSerializer(data=req.data)
    serializer.initial_data['user'] = req.user.id
    if serializer.is_valid():
        Note.objects.filter(pk=id).update(title=req.data['title'],description=req.data['description'],user=req.user)
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_note(req,id):
    try:
        Note.objects.get(pk=id).delete()
    except:
        return Response({"error":"note not found"})


    return Response({"msg":"note deleted"})




