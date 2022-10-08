""" Module for Guide Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptileglossaryapi.models import Writer
from reptileglossaryapi.models import ReptileGuide
from reptileglossaryapi.models import Reptile


class ReptileGuideView(ViewSet):
    """ Guide Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a Guide item """
        try:
            reptileguide = ReptileGuide.objects.get(pk=pk)
            serializer = ReptileGuideSerializer(reptileguide)
            return Response(serializer.data)
        except ReptileGuide.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the Guide items """
        reptileguide = ReptileGuide.objects.all()
        serializer = ReptileGuideSerializer(reptileguide, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Guide item """
        # incoming_user = request.auth.user
        writer  = Writer.objects.get(user=request.auth.user)
        reptile = Reptile.objects.get(pk=request.data["reptile"])
        
        
        new_reptileguide = ReptileGuide.objects.create(
            writer=writer,
            reptile =reptile,
            title=request.data["title"],
            image=request.data["image"],
            description=request.data["description"],
            content=request.data["content"]
            )
        serializer = ReptileGuideSerializer(new_reptileguide)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Guide item """
        editing_reptileguide = ReptileGuide.objects.get(pk=pk)
        editing_reptileguide.title = request.data["title"]
        editing_reptileguide.image = request.data["image"]
        editing_reptileguide.description = request.data["description"]
        editing_reptileguide.content = request.data["content"]
        editing_reptileguide.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a Guide item """
        try:
            reptileguide = ReptileGuide.objects.get(pk=pk)
            reptileguide.delete()
        except ReptileGuide.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ReptileGuideSerializer(serializers.ModelSerializer):
    """ JSON serializer for Guide items """
    class Meta:
        model = ReptileGuide
        fields = (
            'id',
            'writer',
            'reptile',
            'title',
            'image',
            'description',
            'content'
            )
