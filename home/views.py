from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import ListaPessoa
from .models import Pessoa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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

        try:
            if request.session['login'] == True:
                return redirect('home')
        except:
            pass

        self.contexto['msgv'] = 0
        return render(self.request, self.template_name, self.contexto)

    def post(self, request):
        email_db = Pessoa.objects.all()
        # user = User.objects.create_user('renan', 'renan@gmail.com', '123456')
        request.session['login'] = True

        user = authenticate(username=request.POST['user'], password=request.POST['password'])

        if user is not None:
            print('ok ok ok')
            return redirect('home')

        else:
            print('usuario ou senha invalidos')

        if user.is_authenticated:
            print('usuario logado')
        else:
            print('usuario nao permitido')

        if not email_db:
            pessoa = Pessoa(nome=request.POST['nome'], email=request.POST['email'], senha=request.POST['password1'])
            pessoa.save()
            self.contexto['alert'] = 'alert-info'
            self.contexto['msg'] = 'Cadastro realizado com sucesso!'
            self.contexto['msgv'] = 2
        else:
            self.contexto['alert'] = 'alert-danger'
            self.contexto['msg'] = 'este email ja esta em uso'
            self.contexto['msgv'] = 1
            print('Erro disparado')

        return render(self.request, self.template_name, self.contexto)


class Sair(ListView):
    template_name = 'static/sair.html'

    def get(self, request):
        try:
            request.session.pop('login')
            return redirect('home')
        except:
            return redirect('home')

