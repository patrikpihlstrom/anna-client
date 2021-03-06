import unittest

from . import client
from anna_client import graphql


class TestGetJobs(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_get_jobs_query(self):
		query = graphql.get_jobs_query(where={}, fields=('id',))
		self.assertEqual('{jobs(where:{}){id}}', query)
		query = graphql.get_jobs_query(where={'driver': 'firefox'}, fields=('id',))
		self.assertEqual('{jobs(where:{driver:"firefox"}){id}}', query)
		query = graphql.get_jobs_query(where={'driver_in': ('firefox', 'chrome')}, fields=('id',))
		self.assertEqual('{jobs(where:{driver_in:["firefox","chrome"]}){id}}', query)

	def test_get_jobs_query_limit(self):
		query = graphql.get_jobs_query(where={}, fields=('id',), limit=1)
		self.assertEqual('{jobs(where:{} first:1){id}}', query)
		query = graphql.get_jobs_query(where={}, fields=('id',), limit=10000)
		self.assertEqual('{jobs(where:{} first:10000){id}}', query)
		query = graphql.get_jobs_query(where={}, fields=('id',), limit=0)
		self.assertEqual('{jobs(where:{}){id}}', query)
		query = graphql.get_jobs_query(where={}, fields=('id',), limit=-10000)
		self.assertEqual('{jobs(where:{}){id}}', query)

	def test_get_all_jobs(self):
		jobs = client.get_jobs(where={}, fields=['id', 'driver', 'site', 'status'])
		self.assertIsInstance(jobs, list)
		for job in jobs:
			self.assertIn('id', job)
			self.assertIn('driver', job)
			self.assertIn('site', job)
			self.assertIn('status', job)

	def test_get_one_job(self):
		datum = {'driver': 'chrome', 'site': 'test'}
		client.create_jobs(data=[datum, datum])
		jobs = client.get_jobs(where={}, fields=['id', 'driver', 'site', 'status'], limit=1)
		self.assertIsInstance(jobs, list)
		self.assertTrue(len(jobs) < 2)
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

	def test_get_all_pending_jobs(self):
		jobs = client.get_jobs(where={'driver': 'firefox', 'status': 'PENDING'}, fields=['id', 'driver', 'status'])
		self.assertIsInstance(jobs, list)
		for job in jobs:
			self.assertIn('id', job)
			self.assertIn('driver', job)
			self.assertEqual('firefox', job['driver'])
			self.assertEqual('PENDING', job['status'])

	def test_get_all_pending_or_running_jobs(self):
		jobs = client.get_jobs(where={'driver': 'firefox', 'status': 'PENDING,RUNNING'}, fields=['id', 'driver', 'status'])
		self.assertIsInstance(jobs, list)
		for job in jobs:
			self.assertIn('id', job)
			self.assertIn('driver', job)
			self.assertEqual('firefox', job['driver'])
			self.assertTrue(job['status'] in ('PENDING', 'RUNNING'))

