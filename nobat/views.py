from django.shortcuts import render
from .models import nobat
from django.contrib.auth.models import User
from django.core.mail import send_mail
from random import randint
# Create your views here.
def base(request):
    data = {'data':nobat.objects.all()}
    fullName = request.POST.get('fullName')
    if request.method == 'POST':
        if nobat.objects.filter(name=fullName):
            pass
        else:
            name = request.POST.get('fullName')
            amount = request.POST.get('amount')
            id = len(nobat.objects.all())
            curser = nobat(id=id,name=name,amount=amount)
            curser.save()
    return render(request,'base.html',data)


# def randomMaker():
#     result = ''
#     for i in range(6):
#         result += str(randint(0,9))
#     return result

# def sendMail(message,toWho):
#     send_mail('autentication',message,'ghaemhubAuth@gmail.com',[toWho])


def createUser(request):
    return render(request,'createUser.html')