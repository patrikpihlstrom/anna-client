import unittest

from . import client


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

	def test_create_one_job(self):
		pass

	def test_create_two_jobs_one_site_two_drivers(self):
		pass

	def test_create_two_jobs_two_sites_one_driver(self):
		pass

	def test_create_four_jobs_two_sites_two_driver(self):
		pass
