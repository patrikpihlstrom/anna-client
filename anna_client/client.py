from graphqlclient import GraphQLClient, json

from anna_client import util


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
		query = util.get_jobs_query(where=where, fields=fields)
		response = super().execute(query=query)
		response = json.loads(response)
		if 'jobs' in response:
			return response['jobs']
		return response

	def create_jobs(self, data: list) -> tuple:
		ids = []
		for mutation in util.get_create_mutations(data):
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
