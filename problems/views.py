from typing import ContextManager
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


from .models import Problem
from .forms import ProblemForm


@login_required
def problem_view(request):
    problem_id = ''
    form = ProblemForm(request.POST or None)
    if form.is_valid():
        app = form.cleaned_data.get('app')
        title = form.cleaned_data.get('title')
        problem = Problem.objects.filter(app=app, title=title, adopted=True)
        for p in problem:
            problem_id = p.id
        if problem:
            return redirect('problem_exists', id =problem_id)
        else:
            obj = form.save(commit=False)
            obj.created_by=request.user
            obj.save()
            messages.success(request, 'Your complains has been submitted!')
        form=ProblemForm()
    else:
        messages.info(request, 'Kindly fill the form!')

    template = 'problems/problems.html'
    context = {"form":form}
    return render(request, template, context)


@login_required
def home_view(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def adopt_solutions_view(request, id):
    problem = Problem.objects.filter(id=id)
    if request.method == 'POST':
        problem.update(adopted=True)
        return redirect('solution_list')
    template = 'problems/adopt.html'
    context = {'problem':problem}
    return render(request, template, context)


def problem_exists_view(request, id):
    problem = Problem.objects.get(id=id)
    return render(request, 'problems/exists.html', {'problem':problem})


