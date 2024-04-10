from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import modeuser
from apprentissage import settings
from django.core.mail import send_mail


def index(request):
    
    return render(request, 'authen/index.html')


def connection(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username =username, password = password)
        if username is not None:
            login(request, user)
            messages.success(request, 'connection reuici ')
            print('bonjour')
            return render(request, 'authen/index.html')
        else:
            print('bonsoir')
            messages.error(request, 'echec de connection probleme interne ou information non valide')
            return redirect('/authentification/connection')

    return render(request, 'authen/connection.html')

def creecompte(request):
    if request.method == "POST":
        username = request.POST['username']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        passwordconfim = request.POST['passwordconfim']
        if User.objects.filter(username=username):
            messages.error(request, "ce nom a deja ete utiliser pour la creation d'un compte")
            return redirect("/authentification/creecompte")
        if User.objects.filter(email=email):
            messages.error(request, "cet email a deja ete utiliser pour la creation d'un compte")
            return redirect("/authentification/creecompte")
        if password != passwordconfim:
            messages.error(request, "les deux mots de passe ne coinsident pas veillez corriger")
            return redirect("/authentification/creecompte")
        new = User.objects.create_user(username, email, password)
        new.save()
        messages.success(request, 'vous venez de creer votre compte')
        sujet = 'mail de confirmation'
        message = "bienvenu mr" + new.username + " "+ " \n sur sur notre site votre compte a ete creer avec succes\n\n"
        from_mail = settings.EMAIL_HOST_USER
        to_email =[new.email]
        send_mail(sujet, message, from_mail, to_email, fail_silently = False)


        return redirect("/authentification/connection")
        
    return render(request, 'authen/creecompte.html')

def deconnexion(request):
    logout(request)

    return redirect("/authentification/index")