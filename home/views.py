from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import redirect
from django.http import HttpResponse

def start(request):

    if '_auth_user_id' not in request.session.keys():
        return redirect('/log')
    else:
        return render(request, 'home/mainPage.html')


def entry(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        if user:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('<h3>Неверный логин или пароль</h3>')

    return render(request, 'home/log.html')


