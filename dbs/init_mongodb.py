from pymongo import MongoClient

from configs.config import CONFIG


class MongoDB:  # TODO: [Section 3] Handle multithreading instance
	__instance = None

	def __init__(self, host, port):
		self.__host = host
		self.__port = port
		if MongoDB.__instance is None:
			try:
				MongoDB.__instance = MongoClient(host=self.__host, port=self.__port)
				print('Connected MongoDB')
			except Exception as err:
				print(f'Unable to connect to MongoDB:', err)
		else:
			raise Exception('A MongoDB instance is already existed')

	@property
	def host(self):
		return self.__host

	@host.setter
	def host(self, host):
		self.__host = host

	@property
	def port(self):
		return self.__port

	@port.setter
	def port(self, port):
		self.__port = port

	def __repr__(self):
		return f'MongoDB(host={self.__host}, port={self.__port})'

	@staticmethod
	def get_instance(host, port):
		if not MongoDB.__instance:
			MongoDB(host, port)
		return MongoDB.__instance


mongo = MongoDB.get_instance(CONFIG['db']['host'], CONFIG['db']['port'])
