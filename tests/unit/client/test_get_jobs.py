import unittest

from . import client


class TestGetJobs(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_get_jobs_query(self):
		query = client.get_jobs_query(where={}, fields=('id',))
		self.assertEqual('{jobs(where:{}){id}}', query)

	def test_get_all_jobs(self):
		jobs = client.get_jobs(where={}, fields=['id', 'driver', 'site', 'status'])
		self.assertIsInstance(jobs, list)
		for job in jobs:
			self.assertIn('id', job)
			self.assertIn('driver', job)
			self.assertIn('site', job)
			self.assertIn('status', job)
