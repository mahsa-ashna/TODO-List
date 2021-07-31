from urllib import request

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView

from .models import Task, Category


class Task_List_view(ListView):
    model = Task
    template_name = 'Task_List_view.html'
    context_object_name = 'tasklist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timepasstask'] = Task.timepass.get_queryset()
        context['Notask'] = Task.notask. with_counts()
        return context



class Task_detail_view(DetailView):
    model = Task
    template_name = 'Task_detail_view.html'
    context_object_name = 'taskdetail'


class category_list(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categorylist'


def each_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category_list.html', context)


def each_category(request):
    category = request.GET.get('category')
    tasks = Task.objects.filter(category__name=category)
    context = {
        'tasks': tasks,
        'category': category
    }
    return render(request, 'each_category.html', context)


def home(request):
    return render(request, 'index.html')

# class TaskListCreate(CreateView):
#     model = Task
#     template_name = "tasklist_new.html"

def json_file():
    obj = Task.objects.all()
    convert = serialize.serialized("json", obj)
    return HttpResponse(convert, content_type="application/json")