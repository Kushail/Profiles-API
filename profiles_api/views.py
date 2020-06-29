from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloAPIView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,post,patch,put,delete)',
            'Is similar to a traditional Django view but specifically intended to be used by APIs',
            'Gives you full control over application logic',
            'Is mapped to URL endpoints'
            ]
        
        return Response({'message' : 'hello', 'list' : an_apiview})

    
    def post(self, request, format=None):
        """Create a hello message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle update to object"""
        return Response({'method' : 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial updates to an object"""
        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deletion of an object"""
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial update',
            'Automatically maps URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message ' : 'Hello', 'list' : a_viewset})

    def create(self, request):
        """Create a new hello message"""
    
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http method' : 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http method' : 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'http method' : 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http method' : 'DELETE'})

    
