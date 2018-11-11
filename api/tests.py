from django.test import TestCase
from tasks.models import Task
from django.contrib.auth import get_user_model
from billing.models import TaskRelatedNotes


User = get_user_model()


class ExecutorViewSetTest(TestCase):

    def test_for_queryset(self):
        test_user = User.objects.create(username='name', balance=300)
        self.assertEqual(test_user.username, 'name')
        self.assertEqual(test_user.balance, 300)


class PurchaserViewSetTest(TestCase):
    def test_for_queryset(self):
        test_user = User.objects.create(username='name', balance=300)
        self.assertEqual(test_user.username, 'name')
        self.assertEqual(test_user.balance, 300)


class TaskViewSetTest(TestCase):
    def test_for_queryset(self):
        created_by = User.objects.create(
            username="First_name1", balance="1000")
        executor = User.objects.create(
            username="First_name2", balance="1000")
        test_task = Task.objects.create(title="Task_1",
                                        set_price=500,
                                        description="Description_1",
                                        created_by=created_by,
                                        executor=executor)
        self.assertEqual(test_task.title, 'Task_1')
        self.assertEqual(test_task.set_price, 500)
        self.assertEqual(test_task.description, 'Description_1')
        self.assertEqual(test_task.created_by, created_by)
        self.assertEqual(test_task.executor, executor)


User = get_user_model()


class TaskRelatedNotesModelTest(TestCase):
    def test_for_queryset(self):
        created_by = User.objects.create(username="Zen",
                                         balance="1000", user_type=1)
        executor = User.objects.create(username="Fault", balance="1000",
                                       user_type=2)
        task = Task.objects.create(created_by=created_by, description="Body",
                                   title="Title", set_price="200")
        test_notes = TaskRelatedNotes.objects.create(task=task,
                                                     executor=executor,
                                                     price='1050')
        self.assertEquals(test_notes.task, task)
        self.assertEquals(test_notes.executor, executor)
        self.assertEquals(test_notes.price, '1050')
