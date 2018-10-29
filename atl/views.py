from django.shortcuts import render
from tasks.models import Task
from django.http import HttpResponse
from billing.models import TaskRelatedNotes
from users.models import User
from decimal import Decimal
from django.db.models import Q


def index(request):
    sort_by = request.GET.get('sort', 'set_price')
    if sort_by not in [ 'set_price', 'title', 'task_id']:
        sort_by = 'set_price'
    tasks_table = Task.objects.exclude(executor_id__isnull=False).order_by(sort_by)
    context = {'tasks_table' : tasks_table}
    return render(request, 'atl/index.html', context)

def take_task(request, task_id):
    task=Task.objects.get(pk=task_id, executor=None)
    notes, created = TaskRelatedNotes.objects.get_or_create(
            task=Task.objects.get(pk=task_id, executor=None),
            executor_id=request.user.id,
            money=task.set_price)
    if created:
        Task.objects.filter(pk=task_id, executor=None).update(executor=request.user.id)
    return HttpResponse("Success! Task's id is %d" % task_id)
