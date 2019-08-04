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
		query = client.get_jobs_query(where={'driver': 'firefox'}, fields=('id',))
		self.assertEqual('{jobs(where:{driver:"firefox"}){id}}', query)
		query = client.get_jobs_query(where={'driver_in': ('firefox', 'chrome')}, fields=('id',))
		self.assertEqual('{jobs(where:{driver_in:["firefox","chrome"]}){id}}', query)

	def test_get_all_jobs(self):
		jobs = client.get_jobs(where={}, fields=['id', 'driver', 'site', 'status'])
		self.assertIsInstance(jobs, list)
		for job in jobs:
			self.assertIn('id', job)
			self.assertIn('driver', job)
			self.assertIn('site', job)
			self.assertIn('status', job)

	def test_get_all_firefox_jobs(self):
		jobs = client.get_jobs(where={'driver': 'firefox'}, fields=['id', 'driver'])
		self.assertIsInstance(jobs, list)
		for job in jobs:
			self.assertIn('id', job)
			self.assertIn('driver', job)
			self.assertEqual('firefox', job['driver'])
