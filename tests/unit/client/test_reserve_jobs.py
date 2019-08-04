import unittest

from . import client
from anna_client import graphql


class TestReserveJobs(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_get_reserve_jobs_mutation(self):
		client.delete_jobs(where={})
		job_ids = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}, {'driver': 'chrome', 'site': 'test'}])
		mutation = graphql.get_reserve_jobs_mutation(worker='worker', job_ids=job_ids)
		self.assertEqual('mutation{updateManyJobs(where:{id_in:["' + '","'.join(
			job_ids) + '"],worker:null,status:PENDING},data:{worker:"worker",status:RESERVED}){count}}', mutation)
		with self.assertRaises(TypeError):
			graphql.get_reserve_jobs_mutation()

	def test_reserve_one_job(self):
		job_ids = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}])
		reserved = client.reserve_jobs(worker='worker', job_ids=job_ids)
		self.assertEqual(len(job_ids), reserved['updateManyJobs']['count'])

	def test_reserve_two_jobs(self):
		job_ids = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}, {'driver': 'chrome', 'site': 'test'}])
		reserved = client.reserve_jobs(worker='worker', job_ids=job_ids)
		self.assertEqual(len(job_ids), reserved['updateManyJobs']['count'])
