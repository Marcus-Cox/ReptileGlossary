"""View module for handling requests about reptile types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptileglossaryapi.models import SpecialNeedsReptile


class SpecialNeedsReptileView(ViewSet):
    """Level up reptile types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single reptile type
        """
        try:
            specialneedsreptile = SpecialNeedsReptile.objects.get(pk=pk)
            serializer = SpecialNeedsReptileSerializer(specialneedsreptile)
            return Response(serializer.data)
        except SpecialNeedsReptile.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all reptile types
        """
        specialneedsreptiles = SpecialNeedsReptile.objects.all()
        serializer = SpecialNeedsReptileSerializer(specialneedsreptiles, many=True)
        return Response(serializer.data)


class SpecialNeedsReptileSerializer(serializers.ModelSerializer):
    """JSON serializer for reptile types
    """
    class Meta:
        model = SpecialNeedsReptile
        fields = ('id',
                  'name',
                  'species',
                  'morph')