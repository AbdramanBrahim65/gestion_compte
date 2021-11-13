from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import CreerUtilisateur
from django.contrib import messages

# Create your views here.

def inscriptionPage(request):
    form=CreerUtilisateur()
    if request.method=="POST":
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get("username")
            messages.success(request,"le compte est créé avec succès pour !"+user)
            return redirect('acces')
    context={"form":form}
    return render(request,"inscription.html",context)

def accesPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"il y'a un erreur dans le nom d'utilisateur et/ou mot de passe ")
    return render(request,"acces.html")

def home(request):
    return render(request,"home.html")
def logoutUser(request):
    logout(request)
    return redirect('acces')