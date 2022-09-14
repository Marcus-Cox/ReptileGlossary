""" Module for Guide Items requests """
from csv import writer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptileglossaryapi.models import Writer
from reptileglossaryapi.models import DietGuide
from reptileglossaryapi.models import ReptileDiet


class DietGuideView(ViewSet):
    """ Guide Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a Guide item """
        try:
            dietguide = DietGuide.objects.get(pk=pk)
            serializer = DietGuideSerializer(dietguide)
            return Response(serializer.data)
        except DietGuide.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the Guide items """
        dietguide = DietGuide.objects.all()
        serializer = DietGuideSerializer(dietguide, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Guide item """
        # incoming_user = request.auth.user
        writer  = Writer.objects.get(user=request.auth.user)
        reptilediet = ReptileDiet.objects.get(pk=request.data["reptilediet"])
        
        new_dietguide = DietGuide.objects.create(
            writer=writer,
            reptilediet=reptilediet,
            title=request.data["title"],
            image=request.data["image"],
            description=request.data["description"],
            content=request.data["content"],
            publishing_date=request.data["publishing_date"]
        )
        serializer = DietGuideSerializer(new_dietguide)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Guide item """
        editing_dietguide = DietGuide.objects.get(pk=pk)

        editing_dietguide.title = request.data["title"]
        editing_dietguide.image = request.data["image"]
        editing_dietguide.description = request.data["description"]
        editing_dietguide.content = request.data["content"]
        editing_dietguide.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a Guide item """
        try:
            dietguide = DietGuide.objects.get(pk=pk)
            dietguide.delete()
        except DietGuide.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class DietGuideSerializer(serializers.ModelSerializer):
    """ JSON serializer for Guide items """
    class Meta:
        model = DietGuide
        fields = (
            'id',
            'writer',
            'reptilediet',
            'title',
            'image',
            'description',
            'content',
            'publishing_date',
            )
