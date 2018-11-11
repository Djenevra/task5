from django.shortcuts import render
from tasks.models import Task
from django.http import HttpResponse
from billing.models import TaskRelatedNotes
from django.db import transaction


def index(request):
    sort_by = request.GET.get('sort', 'set_price')
    if sort_by not in ['set_price', 'title', 'task_id']:
        sort_by = 'set_price'
    tasks_table = Task.objects.exclude(
                                       executor_id__isnull=False
                                       ).order_by(sort_by)
    context = {'tasks_table': tasks_table}
    return render(request, 'atl/index.html', context)

def take_task(request, task_id):
    Task.objects.filter(pk=task_id).update(executor_id=request.user.id)
    task = Task.objects.get(pk=task_id)
    notes, created = TaskRelatedNotes.objects.get_or_create(
            task=Task.objects.get(pk=task_id),
            executor_id=request.user.id,
            price=task.set_price)

    if created:
        with transaction.atomic():
            request.user.update_balance(task.set_price, task.executor_id,
                                        task.created_by_id,)
    return HttpResponse("Success! Task's id is %d" % task_id)
