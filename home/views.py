from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from .forms import ListaPessoa
from .models import Pessoa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .utils import menssagens


# Create your views here.


class Home(ListView):
    template_name = 'static/index.html'
    contexto = {}

    def get(self, request):
        try:
            if request.session['logado'] == True:
                self.contexto['btn'] = 1
            else:
                self.contexto['btn'] = 0
        except:
            pass

        return render(request, self.template_name, self.contexto)


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
            request.session['logado'] = False
            return redirect('home')
        except:
            return redirect('home')


class Signin(View):
    template_name = 'static/signin.html'
    contexto = {}

    def get(self, request):
        #User.objects.create_user('kjdfkjs','k@k.com','jksldfjkl')
        return render(self.request, self.template_name, self.contexto)

    def post(self, request):
        username = request.POST['nome']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        retmail = 0

        try:
            email = User.objects.get(email=email)
            if email is not None:
                self.contexto = menssagens(alert='alert-danger', msg='Este E-mail ja esta em uso', username=username, email=email)
                return render(self.request, self.template_name, self.contexto)
        except:
            pass

        try:
            username = User.objects.get(username=username)
            if username is not None:
                self.contexto = menssagens(alert='alert-danger', msg='Este nome de usuario ja existe', username=username, email=email)
                return render(self.request, self.template_name, self.contexto)
        except:
            pass

        try:
            if pass1 != pass2:
                self.contexto = menssagens(alert='alert-danger', msg='As senhas nao conferem', username=username, email=email)
                return render(self.request, self.template_name, self.contexto)
            else:
                User.objects.create_user(username, email, pass1)
                return redirect('login')

        except:

            pass

        return render(request, self.template_name, self.contexto)




