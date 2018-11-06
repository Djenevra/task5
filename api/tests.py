from django.test import TestCase
from tasks.models import Task
from django.test import Client
from django.contrib.auth import get_user_model
from billing.models import TaskRelatedNotes
# import requests

User = get_user_model()
class TestExecutorViewSet(TestCase):

    def test_for_queryset(self):
        a = User.objects.create(username='name', balance=300)
        self.assertEqual(a.username, 'name')
        self.assertEqual(a.balance, 300)


class TestPurchaserViewSet(TestCase):
    def test_for_queryset(self):
        a = User.objects.create(username='name', balance=300)
        self.assertEqual(a.username, 'name')
        self.assertEqual(a.balance, 300)


class TestTaskViewSet(TestCase):
    def test_for_queryset(self):
        created_by = User.objects.create(
            username="First_name1", balance="1000")
        executor = User.objects.create(
            username="First_name2", balance="1000")
        a = Task.objects.create(title="Task_1", set_price=500, description="Description_1",
                                created_by=created_by, executor=executor)
        self.assertEqual(a.title, 'Task_1')
        self.assertEqual(a.set_price, 500)
        self.assertEqual(a.description, 'Description_1')
        self.assertEqual(a.created_by, created_by)
        self.assertEqual(a.executor, executor)

User = get_user_model()
class TestTaskRelatedNotesModel(TestCase):
    def test_for_queryset(self):
        created_by = User.objects.create(username = "Zen", balance = "1000", user_type = 1)
        executor = User.objects.create(username = "Fault", balance = "1000", user_type = 2)
        task=Task.objects.create(created_by = created_by, description = "Body", title = "Title", set_price = "200")
        a = TaskRelatedNotes.objects.create(task = task, executor = executor, price = '1050')
        self.assertEquals(a.task, task)
        self.assertEquals(a.executor, executor)
        self.assertEquals(a.price, '1050')



#class ApiTest(TestCase):
    #def test_of_whole_Api_endpoint(self):
    #    self.client = Client()
    #    response = self.client.get('http://127.0.0.1:8000/api/sort')
        # customer_responce = self.client.get('http://127.0.0.1:8000/api/customer/')
        # executer_responce = self.client.get('http://127.0.0.1:8000/api/executer/')
        # task_responce = self.client.get('http://127.0.0.1:8000/api/tasks/')
    #    self.assertEqual(response.status_code, 200)
        # self.assertEqual(customer_response.status_code, 200)
        # self.assertEqual(executer_response.status_code, 200)
        # self.assertEqual(task_response.status_code, 200)
