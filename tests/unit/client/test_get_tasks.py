import unittest

from . import client


class TestGetTasks(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_get_tasks(self):
		url, tasks = client.get_tasks(namespace='test')
		self.assertIsInstance(tasks, list)
		self.assertIsInstance(url, str)
		for task in tasks:
			self.assertIsInstance(task, list)
			for part in task:
				self.assertIsInstance(part, str)
