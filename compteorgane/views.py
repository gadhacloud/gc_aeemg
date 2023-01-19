from django.shortcuts import render, HttpResponse
from .form import formUser

# Create your views here.
def login(request):
    return render(request,'compteorgane/login.html')




#=================
def ajout_Utilisateur(request):
    if request.method == 'POST':
        fm=formUser(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=formUser()
    return render(request,'compteorgane/register.html',{'fm':fm})