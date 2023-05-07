from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
	"""Test API View"""

	def get(self, request, format=None):
		"""Returns a list of APIView features"""
		an_apiview = [
			'Usa el método HTTP como función (get, post, patch, put, delete)'
			'Similar a una vista tradicional Django'
			'Da mayor control sobre la lógica de la aplicacion'
			'Se mapea manualmente hacia las URLs'
		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})