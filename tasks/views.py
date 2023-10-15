from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.utils import timezone


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.db import IntegrityError

# importando el formulario
from .forms import NewTask_form

from .models import Task


def home(request):
    return render(request, 'home.html')


def sign_up(request):

    if request.method == 'GET':
        print('Entra por get')
        return render(request, 'signup.html', {'alert': 'First time', 'form': UserCreationForm()})
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

                print(user)
                user.save()  # va a tratar de guardarlo en la BD
                login(request, user)

                return redirect('tareas_view')
                # redirecciona a tasks

            except IntegrityError:
                # Cuando haya un error de integridad (sign up de un usuario ya creado) va a ejecutar este except

                return render(
                    request, 'signup.html',
                    {
                        'alert': 'Error: usuario existente',
                        'form': UserCreationForm()
                    }

                )
        else:
            return render(request, 'signup.html', {'alert': 'contraseñas invalidas', 'form': UserCreationForm()})


# vista de tareas
@login_required
def tasks_view(request):

    query_tarea = Task.objects.filter(creada_por=request.user)

    return render(request, 'tasks.html', {'tareas': query_tarea})

@login_required
def task_create(request):

    if request.method == 'GET':
        return render(request,    'crear_task.html',  {'form': NewTask_form})
    else:

        try:
            formulario_tarea = NewTask_form(request.POST)

            nueva_tarea = formulario_tarea.save(commit=False)
            # lo que hace "commit=false" se crea una instancia de la tarea (Task) pero no se guarda en la base de datos todavía.

            nueva_tarea.creada_por = request.user

            nueva_tarea.save()

            return redirect('tareas_view')
        except ValueError:
            return render(
                request,
                'crear_task.html',
                {
                    'form': NewTask_form,
                    'alert': 'Error, por favor intentalo mas tarde.'
                }
            )

@login_required
def task_completed(request, task_id):
    task=    get_object_or_404(Task, pk=task_id, creada_por= request.user    )

    if (request.method == 'POST'):
        task.completada= timezone.now()
        task.save()
    
        return redirect('all_tasks')


@login_required
def all_tasks(request):
    query_tarea = Task.objects.filter(creada_por=request.user)

    return render(request, 'all_tasks.html', {'tareas': query_tarea})

@login_required
def task_deleted(request, task_id):
    task=    get_object_or_404(Task, pk=task_id, creada_por= request.user    )

    if (request.method == 'POST'):
        task.delete()
        return redirect('all_tasks')

@login_required
def task_detail(request, task_id):

    if request.method == 'GET':
        print(task_id)

        task = get_object_or_404(Task, pk=task_id, creada_por=request.user)

        task_instance = NewTask_form(instance=task)

        return render(
            request,
            'task_detail.html',
            {
                'detail': task,
                'form': task_instance,
            }
        )
    else:
        try:
            print(request.POST)
            task = get_object_or_404(Task, pk=task_id, creada_por= request.user)

            form = NewTask_form(request.POST, instance=task)
            form.save()

            return redirect('tareas_view')
        except:
            return render(
                request,
                'task_detail.html',
                {
                    'detail': task,
                    'form': task_instance,
                    'error': 'Error al actualizar La tarea :('
                }
            )


@login_required
def salir(request):

    logout(request)

    return redirect('home')


def ingresar(request):

    if request.method == 'POST':

        print(request.POST)

        # se procede a autenticar con el metodo authenticate
        # esto hara que antes de hacer el metodo login primero se debe verificar en la db

        usr_nombre = request.POST['username']
        usr_password = request.POST['password']

        usuario_autenticado = authenticate(
            request,
            username=usr_nombre,
            password=usr_password
        )

        print(usuario_autenticado)

        if usuario_autenticado == None:
            return render(
                request,
                'ingresar.html',
                {
                    'formulario': AuthenticationForm(),
                    'alert': 'Error: Usuario o contraseña incorrectos'
                }
            )
        else:

            login(request, usuario_autenticado)
            return redirect('tareas_view')
    else:

        # por este flujo retorna cuando es un get

        return render(
            request,
            'ingresar.html',
            {
                'formulario': AuthenticationForm()
            }
        )
