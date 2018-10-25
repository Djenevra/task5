from django.shortcuts import render, get_object_or_404
from tasks.models import Task


#def index(request):
    #tasks_list = Task.objects.order_by('set_price')
    #context = {'tasks_list' : tasks_list}
    #return render(request, 'atl/index.html', context)

#def detail(request, task_id):
    #task = get_object_or_404(Task, pk=task_id)
    #return render(request, 'atl/detail.html', {'task': task})

def task_list(request):
    return render(request, 'atl/index.html', {'task_list' : Task.objects.all()})
