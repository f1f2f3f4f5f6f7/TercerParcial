from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import NotasForm
from .models import Notas

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registar
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('notas')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm, "Error": 'Ya existe el usuario.'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm, "Error": 'La contraseña no coinciden'
        })

def notas(request):

    notas = Notas.objects.filter(user = request.user)

    return render(request, 'notas.html', {'notas': notas})

def addNotas(request):

    if request.method == 'GET':
        return render(request, 'addNotas.html',{
            'form':NotasForm
        })
    else:
        try:
            form= NotasForm(request.POST)
            newNota= form.save(commit=False)
            newNota.user= request.user
            newNota.save()
            return redirect('notas')
        except ValueError:
            return render(request, 'addNotas.html',{
            'form':NotasForm,
            'Error':'Ingrese data valida'
            })
            



    

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username = request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signinota=models.CharField(max_length=3)n.html',{
                'form':AuthenticationForm,
                'Error':'Usuario o contrasena incorrecto '
            })
        else:
            login(request, user)
            return redirect('notas')
        


def eliminacionNota(request, title):
    nota = Notas.objects.get(title = title)
    nota.delete()
    return redirect('notas')