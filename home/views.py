from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Dealer, Car


def start(request):
    if '_auth_user_id' not in request.session.keys():
        return redirect('/log')
    else:
        cars = Car.objects.all().filter(
            user=Dealer.objects.get(user=User.objects.get(id=request.session['_auth_user_id'])))
        return render(request, 'home/mainPage.html', {'cars': cars})


def entry(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('<h3>Неверный логин или пароль</h3>')

    return render(request, 'home/log.html')


def add(request):
    obj = Car(user=Dealer.objects.get(user=User.objects.get(id=request.session['_auth_user_id'])),
              count=request.POST['count'], city=request.POST['city'], model=request.POST['model'],
              year=request.POST['year'])
    obj.save()
    return redirect('/')


def rem(request, id):
    obj = Car.objects.get(id=id)
    obj.delete()
    return redirect('/')


def plus(request, id):
    obj = Car.objects.get(id=id)
    obj.count += 1
    obj.save()
    return redirect('/')


def minus(request, id):
    obj = Car.objects.get(id=id)
    if obj.count == 1:
        return redirect('/rem/' + str(id))
    obj.count -= 1
    obj.save()
    return redirect('/')
