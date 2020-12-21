from django.shortcuts import render, redirect
from .models import Note
from django.contrib import auth

# Create your views here.
def index(req):


    notes = []

    if req.user.is_authenticated:
        notes = Note.objects.filter(user=req.user)

    

    return render(req,'index.html',{'notes':notes})

def add_note_page(req):
    return render(req,'one_note.html')

def view(req,id):
    try:
        note = Note.objects.get(pk=id)
    except:
        return redirect("/")
    return render(req,'one_note.html',{"note":note})

def add(req):
    title = req.POST['title']
    desc = req.POST['desc']

    Note.objects.get_or_create(title=title,description=desc,user=req.user)

    

    return redirect('/')    

def delete(req,id):

    try:
        Note.objects.get(pk=id).delete()
    except:
        return redirect('/')    

    return redirect('/')