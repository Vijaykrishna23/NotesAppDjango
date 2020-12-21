from django.shortcuts import render, redirect
from .models import Note
from django.contrib import auth

# Create your views here.
def index(req):


    notes = []

    if req.user.is_authenticated:
        notes = Note.objects.filter(user=req.user)

    

    return render(req,'index.html',{'notes':notes})

def view(req,id=0):

    return render(req,'one_note.html')

def add(req):
    title = req.POST['title']
    desc = req.POST['desc']

    Note.objects.create(title=title,description=desc,user=req.user)

    

    return redirect('/')    

    