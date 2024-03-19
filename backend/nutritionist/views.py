from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Nutritionist
from .serializers import NutritionistSerializer


class NutritionistView(ModelViewSet):
    def create(self, request):
        serializer = NutritionistSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        nutritionist = Nutritionist.objects.create(**serializer.validated_data)
        nutritionist_serialized = NutritionistSerializer(nutritionist)

        return Response(nutritionist_serialized.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        nutritionist = Nutritionist.objects.filter(pk=pk).first()

        if not nutritionist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NutritionistSerializer(nutritionist)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_all(self, request):
        nutritionist_list = Nutritionist.objects.all()

        if not nutritionist_list:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = NutritionistSerializer(nutritionist_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)