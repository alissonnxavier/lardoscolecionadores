from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import ListaPessoa
from .models import Pessoa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .utils import menssagens, sumform


# Create your views here.


class Home(ListView):
    template_name = 'static/index.html'

    def get(self, request):

        return render(request, self.template_name)


class About(ListView):
    template_name = 'static/about.html'

    def get(self, request):
        return render(request, self.template_name)


class Login(ListView):
    template_name = 'static/login.html'
    contexto = {'form': ListaPessoa, 'alert': '', 'msg': '', 'msgv': 0}

    def get(self, request):
        self.contexto['msgv'] = 0

        try:
            if request.session['logado'] == True:
                return redirect('home')
        except:
            pass

        return render(self.request, self.template_name, self.contexto)

    def post(self, request):

        user = authenticate(username=request.POST['user'], password=request.POST['password'])

        if user is not None:
            request.session['logado'] = True
            return redirect('home')
        else:
            self.contexto = menssagens('alert-danger', 'Usuario ou senha invalidos')

        return render(self.request, self.template_name, self.contexto)


class Sair(ListView):
    template_name = 'static/sair.html'

    def get(self, request):
        try:
            request.session.pop('logado')
            return redirect('home')
        except:
            return redirect('home')


class Signin(ListView):
    template_name = 'static/signin.html'
    contexto = {}

    def get(self, request):
        return render(request, self.template_name, self.contexto)

    def post(self, request):

        sumform(request.POST['nome'], request.POST['email'], request.POST['password1'], request.POST['password2'])


        try:
            username = User.objects.get(username='renan')
            email = User.objects.get(email='alisson@gmail.com')

            if email is not None:
                self.contexto = menssagens('alert-danger', 'Este E-mail ja esta em uso')
            else:
                pass
            if username is not None:
                print('username em uso')
                self.contexto = menssagens('alert-danger', 'Este usuario ja esta em uso, Porfavor escolha outro')
        except:
            pass

        return render(request, self.template_name, self.contexto)
