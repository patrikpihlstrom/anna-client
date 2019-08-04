import unittest

from . import client

from anna_client import util


class TestDeleteJobs(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_get_delete_mutation(self):
		mutation = util.get_delete_mutation(where={'driver': 'firefox'})
		self.assertEqual('mutation{deleteManyJobs(where:{driver:"firefox"}){count}}', mutation)
		mutation = util.get_delete_mutation(where={})
		self.assertEqual('mutation{deleteManyJobs(where:{}){count}}', mutation)

	def test_delete_all(self):
		count = len(client.get_jobs())
		response = client.delete_jobs(where={})
		self.assertEqual(0, len(client.get_jobs()))
		self.assertEqual(count, response['deleteManyJobs']['count'])

	def test_delete_one(self):
		job_id = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}, {'driver': 'firefox', 'site': 'test'}])[0]
		count = len(client.get_jobs())
		response = client.delete_jobs(where={'id': job_id})
		self.assertEqual(count-1, len(client.get_jobs()))
		self.assertEqual(1, response['deleteManyJobs']['count'])
