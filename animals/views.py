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
