from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from django.db import IntegrityError

                        
def home(request):
    return render(request, 'home.html')
    


def sign_up(request):

    if request.method == 'GET':
        print('Entra por get')
        return render(request, 'signup.html', {'alert':'First time','form': UserCreationForm()})
    else:
        print(request.POST)
        print('Recibiendo datos')

        if request.POST['password1'] == request.POST['password2']:
            # registrar usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )

                user.save()  # va a tratar de guardarlo en la BD
                login(request, user)

                return  redirect('tareas_view')
                # redirecciona a tasks
                
            except IntegrityError: 
                # Cuando haya un error de integridad (sign up de un usuario ya creado) va a ejecutar este except
                
                return render(
                   request, 'signup.html', 
                   {
                    'alert':'Error: usuario existente',
                    'form': UserCreationForm()
                   }
                
                )
        else:
            return render(request, 'signup.html', {'alert':'contraseñas invalidas','form': UserCreationForm()})


def tasks_view(request):
    return render(request, 'tasks.html')


def salir(request):

    logout(request)
    
    return redirect('home')