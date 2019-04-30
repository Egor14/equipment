from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Dealer, Car


def start(request):
    if '_auth_user_id' not in request.session.keys():
        return redirect('/log')
    else:
        user = Dealer.objects.get(user=User.objects.get(id=request.session['_auth_user_id']))
        cars = Car.objects.all().filter(user=user)

        return render(request, 'home/mainPage.html', {'cars': cars, 'user': user.name})


def entry(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        print(user)
        print(type(user))
        if user and user.is_active == True:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'home/log.html', {'message': 'Неверный логин или пароль'})

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


def out(request):
    logout(request)
    print('sdsad')
    return redirect('/')


def sign(request):
    return render(request, 'home/sign.html')


def query(request):
    obj = User(username=request.POST['user'], is_active=False)
    obj.set_password(request.POST['pass'])
    obj.save()
    obj = Dealer(name=request.POST['name'], phone_number=request.POST['tel'], user=obj)
    obj.save()
    return render(request, 'home/log.html',
                  {'message2': 'Ваша заявка отправлена, администратор свяжется с вами для подтвержения информации'})
