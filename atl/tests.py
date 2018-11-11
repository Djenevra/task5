from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Task
"""These functions are atl/view functions (update_balance function
is in users/models)"""


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
        Task.objects.create(title="Task_1", set_price=500,
                            description="Description_1",
                            created_by=created_by, executor=executor)
        tasks_table = Task.objects.exclude(executor_id__isnull=False)
        self.assertFalse(tasks_table, None)


class TakeTaskTest(TestCase):
    def setUp(self):
        created_by = User.objects.create(
                                         username="First_name1",
                                         balance="1000")
        executor = User.objects.create(
                                       username="First_name2", balance="1000")
        Task.objects.create(id=1, title="Task_1",
                            set_price=500, description="Description_1",
                            created_by=created_by, executor=executor)

    def test_take_task(self):
        Task.objects.get(pk=1)
        self.client.get('/atl/sort/{{ task.id }}/take')


class UpdateBalanceTest(TestCase):
    def setUp(self):
        created_by = User.objects.create(id=1,
                                         username="First_name1",
                                         balance="1000")
        executor = User.objects.create(id=2,
                                       username="First_name2", balance="1000")
        Task.objects.create(id=1, title="Task_1", set_price=500,
                            description="Description_1",
                            created_by=created_by, executor=executor)

    def test_update_balance(self):
        Task.objects.get(set_price=500)
        User.objects.get(pk=1)
        User.objects.get(pk=2)
