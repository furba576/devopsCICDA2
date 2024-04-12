import unittest
from TaskManager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        # Test adding a task
        self.task_manager.add_task("Task 1")
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_mark_task_completed(self):
        # Test marking a task as completed
        self.task_manager.add_task("Task 1")
        self.task_manager.mark_task_completed(0)
        self.assertTrue(self.task_manager.tasks[0].completed)

    # This will fail
    def test_list_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.mark_task_completed(0)
        expected_output = "1. Task 1 - Completed\n2. Task 2 - Not Completed\n"
        self.assertEqual(self.task_manager.list_tasks(), expected_output)

    # this will also faile
    def test_mark_invalid_task_completed(self):
        self.task_manager.add_task("Task 1")
        with self.assertRaises(IndexError):
            self.task_manager.mark_task_completed(1)

    def test_add_empty_task(self):
        self.task_manager.add_task("")
        self.assertEqual(len(self.task_manager.tasks), 1)

if __name__ == '__main__':
    unittest.main()
