from typing import Union

from graphqlclient import GraphQLClient, json


class Client(GraphQLClient):
	"""
	Wrapper around GraphQLClient
	"""

	def __init__(self, endpoint):
		super().__init__(endpoint)

	def query(self, query: str, variables: str) -> list:
		return super().execute(query=query, variables=variables)

	def get_jobs(self, where=None, fields: tuple = ('id',)) -> list:
		if where is None:
			where = {}
		query = self.get_jobs_query(where=where, fields=fields)
		response = super().execute(query=query)
		response = json.loads(response)
		if 'jobs' in response:
			return response['jobs']
		return response

	def create_jobs(self, data: list) -> list:
		response = []
		for mutation in self.get_create_mutation(data):
			response.append(json.loads(super().execute(mutation)))
		return response

	def delete_jobs(self, parameters: dict):
		pass

	def update_jobs(self, parameters: dict):
		pass

	def reserve_jobs(self, parameters: dict):
		pass

	def get_tasks(self, parameters: dict):
		pass

	@staticmethod
	def get_create_mutation(data: list) -> str:
		if len(data) <= 0:
			raise TypeError('provide at least one dict with a driver & a site')
		for d in data:
			if not isinstance(d, dict):
				raise TypeError('parameter data must be a list of dicts')
			if 'site' not in d or 'driver' not in d or not isinstance(d['site'], str) or not isinstance(d['driver'],
																										str):
				raise TypeError('you must specify a driver & a site')
		return ''

	@staticmethod
	def get_key_val_str(key: str, val: Union[tuple, list, str]) -> str:
		if not isinstance(key, str):
			raise TypeError('key must be a string')
		if isinstance(val, str):
			return key + ':"' + val + '"'
		elif isinstance(val, tuple) or isinstance(val, list):
			return key + ':["' + '","'.join(val) + '"]'
		else:
			raise TypeError('val must be a tuple, list or string')

	@staticmethod
	def get_jobs_query(where: dict, fields: tuple) -> str:
		parts = (Client.get_key_val_str(key=key, val=val) for key, val in where.items())
		where = '{' + ','.join(parts) + '}'
		return '{jobs(where:' + where + '){' + ','.join(fields) + '}}'
