from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Question, Answer
from .forms import AnswerForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def index(request):
    q = Question.objects.all()
    return render(request,'index.html',{'q':q})


class QuestionDetail(LoginRequiredMixin,DetailView):
    model = Question


class PostQuestion(LoginRequiredMixin,CreateView):
    model = Question
    fields = ['question']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_answer_to_question(request,pk):
    q = get_object_or_404(Question,pk = pk)
    if request.method =='POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.question = q
            answer.user = request.user
            answer.save()
            return redirect('detail', pk = q.pk)
    else:
        form = AnswerForm()
    return render(request,'qna/answer_form.html',{'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
