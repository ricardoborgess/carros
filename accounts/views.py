from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST": # Se o metodo do request for POST
        user_form = UserCreationForm(request.POST) # Cria formulario com os dados que foram preenchidos
        if user_form.is_valid(): # Valida se ta tudo certo com os dados preenchidos
            user_form.save() # Salva o usuario
            return redirect('login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"] # Captura o username do formulario e coloca na variavel username
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) # Valida o usuario com a função authenticate do django
        if user is not None: # Se o usuario retornou, ou seja, ta valido
            login(request, user) # Função login do proprio django
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')