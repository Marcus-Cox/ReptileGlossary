"""View module for handling requests about reptile types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptileglossaryapi.models import Reptile


class ReptileView(ViewSet):
    """Level up reptile types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single reptile type
        """
        try:
            reptile = Reptile.objects.get(pk=pk)
            serializer = ReptileSerializer(reptile)
            return Response(serializer.data)
        except Reptile.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all reptile types
        """
        reptiles = Reptile.objects.all()
        serializer = ReptileSerializer(reptiles, many=True)
        return Response(serializer.data)


class ReptileSerializer(serializers.ModelSerializer):
    """JSON serializer for reptile types
    """
    class Meta:
        model = Reptile
        fields = ('id',
                  'name',
                  'genus',
                  'species')