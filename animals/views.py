from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from .models import Animal
from .serializers import AnimalSerializer


class AnimalView(APIView):
    def post(self, request: Request):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)


class SpecificAnimalView(APIView):
    def get(self, _: Request, animal_id: int):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
            serialized = AnimalSerializer(animal)

            return Response(serialized.data, status.HTTP_200_OK)

        except Http404:
            return Response({"detail": "Animal not found."}, status.HTTP_404_NOT_FOUND)

    def patch(self, request: Request, animal_id: int):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)

            serialized = AnimalSerializer(animal, request.data, partial=True)
            serialized.is_valid(raise_exception=True)
            serialized.save()

            return Response(serialized.data, status.HTTP_200_OK)

        except Http404:
            return Response({"detail": "Animal not found."}, status.HTTP_404_NOT_FOUND)

    def delete(self, _: Request, animal_id: int):
        try:
            animal = get_object_or_404(Animal, pk=animal_id)
            animal.delete()

            return Response("", status.HTTP_204_NO_CONTENT)

        except Http404:
            return Response({"detail": "Animal not found."}, status.HTTP_404_NOT_FOUND)
