import unittest

from . import client
from anna_client import graphql


class TestCreateJobs(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_raises_type_error(self):
		with self.assertRaises(TypeError):
			client.create_jobs(data=[{}])
		with self.assertRaises(TypeError):
			client.create_jobs(data=[{'driver': ''}])
		with self.assertRaises(TypeError):
			client.create_jobs(data=[{'site': ''}])
		with self.assertRaises(TypeError):
			client.create_jobs(data=[{'site': 0, 'driver': False}])

	def test_get_create_mutations(self):
		data = [{'driver': 'firefox', 'site': 'test'}, {'driver': 'chrome', 'site': 'test'}]
		i = 0
		for mutation in graphql.get_create_mutations(data):
			self.assertEqual(
				'mutation{createJob(data:{driver:"' + data[i]['driver'] + '",site:"' + data[i]['site'] + '"}){id}}',
				mutation)
			i = i + 1
		self.assertEqual(len(data), i)

	def test_create_one_job(self):
		count = len(client.get_jobs())
		response = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}])
		self.assertEqual(count + 1, len(client.get_jobs()))
		self.assertIsInstance(response, tuple)
		for id in response:
			self.assertIsInstance(id, str)

	def test_create_two_jobs(self):
		count = len(client.get_jobs())
		response = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}, {'driver': 'chrome', 'site': 'test'}])
		self.assertEqual(count + 2, len(client.get_jobs()))
		self.assertIsInstance(response, tuple)
		for id in response:
			self.assertIsInstance(id, str)
