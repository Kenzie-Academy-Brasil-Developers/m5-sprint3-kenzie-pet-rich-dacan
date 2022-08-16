from rest_framework.views import APIView, Request, Response, status

from .models import Animal
from .serializers import AnimalSerializer


class AnimalView(APIView):
    def get(self, request: Request) -> Response:
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)

        return Response(serializer.data)
