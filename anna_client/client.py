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

	def create_jobs(self, data: list) -> tuple:
		ids = []
		for mutation in self.get_create_mutations(data):
			response = json.loads(super().execute(mutation))
			if 'createJob' in response and 'id' in response['createJob']:
				ids.append(response['createJob']['id'])
		return tuple(ids)

	def delete_jobs(self, parameters: dict):
		pass

	def update_jobs(self, parameters: dict):
		pass

	def reserve_jobs(self, parameters: dict):
		pass

	def get_tasks(self, parameters: dict):
		pass

	@staticmethod
	def get_create_mutations(data: list) -> str:
		if len(data) <= 0:
			raise TypeError('provide at least one dict with a driver & a site')
		for mutation in data:
			if not isinstance(mutation, dict):
				raise TypeError('parameter data must be a list of dicts')
			if 'site' not in mutation or 'driver' not in mutation or not isinstance(mutation['site'], str) \
					or not isinstance(mutation['driver'], str):
				raise TypeError('you must specify a driver & a site')
		for mutation in data:
			parts = ','.join(list(Client.get_key_val_str(key=key, val=val) for key, val in mutation.items()))
			mutation = 'mutation{createJob(data:{' + parts + '}){id}}'
			yield mutation

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
