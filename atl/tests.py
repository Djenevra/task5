from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task
from atl.views import take_task
"These functions are view functions (atl/views)"


User = get_user_model()
class IndexTest(TestCase):
    def test_index_response(self):
        "Tests if index function returns status code 200"
        response = self.client.get(reverse('atl:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['tasks_table'], [])

    def test_exclude_function(self):
        "Tests if exclude function works correctly"
        created_by = User.objects.create(
            username="First_name1", balance="1000")
        executor = User.objects.create(
            username="First_name2", balance="1000")
        a = Task.objects.create(title="Task_1", set_price=500, description="Description_1",
                                created_by=created_by, executor=executor)
        tasks_table = Task.objects.exclude(executor_id__isnull=False)
        self.assertFalse(tasks_table, None)

class TakeTaskTest(TestCase):
    def setUp(self):
        created_by = User.objects.create(
        username="First_name1", balance="1000")
        executor = User.objects.create(
        username="First_name2", balance="1000")
        a = Task.objects.create(id=1, title="Task_1", set_price=500, description="Description_1",
                            created_by=created_by, executor=executor)
    def test_filter(self):
        task = Task.objects.get(pk=1)
        take_task(self, task.id)

        #task=Task.objects.get(pk=task_id)
        #notes, created = TaskRelatedNotes.objects.get_or_create(
        #        task=Task.objects.get(pk=task_id),
        #        executor_id=request.user,
        #        price=task.set_price)
        #self.assertEqual(, 200)
