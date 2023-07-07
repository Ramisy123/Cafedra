from django.template import context
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

def edit_page(request):
    if request.user.is_authenticated:
        role=request.user.groups.all()[0].name
    else:
        role = 'None'
    template = 'index.html'
    context = {
        'list_articles': Article.objects.all().order_by('-id'),
        'role':role
    }
    return render (request, template, context)

def page_app(request):
    template = 'index_app.html'
    return render (request, template)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    template_name = 'profile.html'
    form_class = StudentForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        kwargs['update'] =  True
        return super().get_context_data(**kwargs)

class ProfileListView(LoginRequiredMixin, CreateView):
    model = Students
    template_name = 'profile.html'
    form_class = StudentForm
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        kwargs['list'] =  Students.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class RatingListView(LoginRequiredMixin, ListView):
    model = Progress
    template_name = 'rating.html'
    form_class = StudentForm
    success_url = reverse_lazy('rating')

    def get_context_data(self, **kwargs):
        kwargs['list'] =  Progress.objects.all().order_by('-id')

        if Students.objects.filter(author = self.request.user).exists():
            li = Students.objects.filter(author = self.request.user)[0]
            kwargs['students'] = li
            kwargs['styp'] = li.type_of_styp
            summ = Styp.objects.filter(type = li.type_of_styp)[0].summ
            kwargs['summ'] = summ
            kwargs['student_name'] = li.id
            list = Progress.objects.filter(student_id = li.id)
            count={'2':0,'3':0,'4':0,'5':0}

            for i in list:
                if i.score == 3: count['3'] = count['3']+1
                elif i.score == 4: count['4'] = count['4']+1
                elif i.score == 5: count['5'] = count['5']+1

            if count['2']>0: 
                kwargs['styp'] = 'Отчислен' 
                kwargs['summ'] = ''
            elif count['3']>0: 
                kwargs['styp'] = 'Нет ' 
                kwargs['summ'] = ''
            elif count['5']<2:
                kwargs['styp'] = 'Базовая' 
                kwargs['summ'] = '2500'
            elif count['5']>2:
                kwargs['styp'] = 'Средняя' 
                kwargs['summ'] = '3500'
            elif count['4']==0:
                kwargs['styp'] = 'Повышенная' 
                kwargs['summ'] = '4500'
        return super().get_context_data(**kwargs)

class UserLoginViev(LoginView):
    form_class = AuthUserForm
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        return self.success_url

class UserLogout(LogoutView):
    next_page = reverse_lazy('home')

class GroupmatesListViews(LoginRequiredMixin, CreateView):
    model = Students
    template_name = 'groupmates.html'
    form_class = StudentForm
    success_url = reverse_lazy('groupmates')

    def get_context_data(self, **kwargs):
        kwargs['list'] =  Students.objects.all().order_by('-id')
        if Students.objects.filter(author = self.request.user).exists():
            li = Students.objects.filter(author = self.request.user)[0]
            kwargs['student_name'] = li.id
            kwargs['group'] = li.group
            kwargs['user_name'] = li.group
        return super().get_context_data(**kwargs)

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'index.html'
    form_class = ArticleForm
    success_url = reverse_lazy('home')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['list'] =  Article.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    
class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        kwargs['title'] ='Новости'
        if self.request.user.is_authenticated:
            role=self.request.user.groups.all()[0].name
        else:
            role = 'None'
        kwargs['role'] = role
        return super().get_context_data(**kwargs)


