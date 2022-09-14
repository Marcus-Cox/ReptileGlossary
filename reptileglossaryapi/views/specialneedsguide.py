""" Module for Guide Items requests """
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from reptileglossaryapi.models import Writer, specialneedsreptile
from reptileglossaryapi.models import SpecialNeedsGuide
from reptileglossaryapi.models import SpecialNeedsReptile


class SpecialNeedsGuideView(ViewSet):
    """ Guide Items Viewset """

    def retrieve(self, request, pk):
        """ Handle a GET request for a Guide item """
        try:
            specialreptileguide = SpecialNeedsGuide.objects.get(pk=pk)
            serializer = SpecialNeedsGuideSerializer(specialreptileguide)
            return Response(serializer.data)
        except SpecialNeedsGuide.DoesNotExist as e:
            return Response({}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """ Handle a GET request for all of the Guide items """
        specialreptileguide = SpecialNeedsGuide.objects.all()
        serializer = SpecialNeedsGuideSerializer(specialreptileguide, many=True)
        return Response(serializer.data)

    def create(self, request):
        """ Handle a POST request for a Guide item """
        # incoming_user = request.auth.user
        writer  = Writer.objects.get(user=request.auth.user)
        specialneedsreptile = SpecialNeedsReptile.objects.get(pk=request.data["specialneedsreptile"])
        
        new_specialreptileguide = SpecialNeedsGuide.objects.create(
            writer=writer,
            specialneedsreptile =specialneedsreptile,
            title=request.data["title"],
            image=request.data["image"],
            description=request.data["description"],
            content=request.data["content"],
            publishing_date=request.data["publishing_date"]
        )
        serializer = SpecialNeedsGuideSerializer(new_specialreptileguide)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """ Handles a PUT request for a Guide item """
        editing_specialreptileguide = SpecialNeedsGuide.objects.get(pk=pk)

        editing_specialreptileguide.title = request.data["title"]
        editing_specialreptileguide.image = request.data["image"]
        editing_specialreptileguide.description = request.data["description"]
        editing_specialreptileguide.content = request.data["content"]
        editing_specialreptileguide.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ Handles a DELETE request for a Guide item """
        try:
            specialreptileguide = SpecialNeedsGuide.objects.get(pk=pk)
            specialreptileguide.delete()
        except SpecialNeedsGuide.DoesNotExist as e:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SpecialNeedsGuideSerializer(serializers.ModelSerializer):
    """ JSON serializer for Guide items """
    class Meta:
        model = SpecialNeedsGuide
        fields = (
            'id',
            'writer',
            'specialneedsreptile',
            'title',
            'image',
            'description',
            'content',
            'publishing_date',
            )
