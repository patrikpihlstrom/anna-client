from typing import Union


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
		parts = ','.join(list(get_key_val_str(key=key, val=val) for key, val in mutation.items()))
		mutation = 'mutation{createJob(data:{' + parts + '}){id}}'
		yield mutation


def get_key_val_str(key: str, val: Union[tuple, list, str]) -> str:
	if not isinstance(key, str):
		raise TypeError('key must be a string')
	if isinstance(val, str):
		return key + ':"' + val + '"'
	elif isinstance(val, tuple) or isinstance(val, list):
		return key + ':["' + '","'.join(val) + '"]'
	else:
		raise TypeError('val must be a tuple, list or string')


def get_jobs_query(where: dict, fields: tuple) -> str:
	parts = (get_key_val_str(key=key, val=val) for key, val in where.items())
	where = '{' + ','.join(parts) + '}'
	return '{jobs(where:' + where + '){' + ','.join(fields) + '}}'
