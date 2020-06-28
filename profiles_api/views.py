from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'Is similar to a traditional Django view but specifically intended to be used by APIs',
            'Gives you full control over application logic',
            'Is mapped to URL endpoints']
        
        return Response({'message' : 'hello', 'list' : an_apiview})
