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

	def create_jobs(self, parameters: dict):
		pass

	def delete_jobs(self, parameters: dict):
		pass

	def update_jobs(self, parameters: dict):
		pass

	def reserve_jobs(self, parameters: dict):
		pass

	def get_tasks(self, parameters: dict):
		pass

	@staticmethod
	def get_jobs_query(where: dict, fields: tuple) -> str:
		return '{jobs(where:'+str(where)+'){'+ ','.join(fields) + '}}'
