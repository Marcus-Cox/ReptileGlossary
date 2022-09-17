"""View module for handling requests about ReptileDiet types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptileglossaryapi.models import ReptileDiet


class ReptileDietView(ViewSet):
    """Level up ReptileDiet types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single ReptileDiet type
        """
        try:
            reptilediet = ReptileDiet.objects.get(pk=pk)
            serializer = ReptileDietSerializer(reptilediet)
            return Response(serializer.data)
        except ReptileDiet.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all ReptileDiet types
        """
        reptilediets = ReptileDiet.objects.all()
        serializer = ReptileDietSerializer(reptilediets, many=True)
        return Response(serializer.data)


class ReptileDietSerializer(serializers.ModelSerializer):
    """JSON serializer for ReptileDiet types
    """
    class Meta:
        model = ReptileDiet
        fields = ('id',
                  'type',
                  'reptile',
                  'diet')