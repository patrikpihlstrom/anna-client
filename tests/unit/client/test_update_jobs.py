import unittest

from . import client
from anna_client import util


class TestUpdateJobs(unittest.TestCase):
	def setUp(self) -> None:
		pass

	def tearDown(self) -> None:
		pass

	def test_get_update_mutation(self):
		job_id = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}])[0]
		mutation = util.get_update_mutation(where={'id': job_id}, data={'status': 'STARTING'})
		self.assertEqual('mutation{updateManyJobs(where:{id:"' + job_id + '"},data:{status:"STARTING"}){count}}',
						 mutation)

	def test_update_one_job_one_field(self):
		job_id = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}])[0]
		response = client.update_jobs(where={'id': job_id}, data={'status': 'STARTING'})
		self.assertEqual(1, response['updateManyJobs']['count'])
		job = client.get_jobs(where={'id': job_id}, fields=('status',))[0]
		self.assertEqual('STARTING', job['status'])

	def test_update_one_job_two_fields(self):
		job_id = client.create_jobs(data=[{'driver': 'firefox', 'site': 'test'}])[0]
		response = client.update_jobs(where={'id': job_id}, data={
			'status': 'STARTING',
			'log': 'running some.task @ http://localhost:5000/ on firefox'
		})
		self.assertEqual(1, response['updateManyJobs']['count'])
		job = client.get_jobs(where={'id': job_id}, fields=('status', 'log'))[0]
		self.assertEqual('STARTING', job['status'])
		self.assertEqual('running some.task @ http://localhost:5000/ on firefox', job['log'])

	def test_update_two_jobs_one_field(self):
		job_ids = client.create_jobs(data=[
			{'driver': 'firefox', 'site': 'test'},
			{'driver': 'chrome', 'site': 'test'}
		])
		response = client.update_jobs(where={'id_in': job_ids}, data={
			'status': 'STARTING',
			'log': 'running some.task @ http://localhost:5000/ on firefox'
		})
		self.assertEqual(2, response['updateManyJobs']['count'])
		jobs = client.get_jobs(where={'id_in': job_ids}, fields=('status',))
		for job in jobs:
			self.assertEqual('STARTING', job['status'])

	def test_update_two_jobs_two_fields(self):
		job_ids = client.create_jobs(data=[
			{'driver': 'firefox', 'site': 'test'},
			{'driver': 'chrome', 'site': 'test'}
		])
		response = client.update_jobs(where={'id_in': job_ids}, data={
			'status': 'STARTING',
			'log': 'running some.task @ http://localhost:5000/ on firefox'
		})
		self.assertEqual(2, response['updateManyJobs']['count'])
		jobs = client.get_jobs(where={'id_in': job_ids}, fields=('status', 'log'))
		for job in jobs:
			self.assertEqual('STARTING', job['status'])
			self.assertEqual('running some.task @ http://localhost:5000/ on firefox', job['log'])
