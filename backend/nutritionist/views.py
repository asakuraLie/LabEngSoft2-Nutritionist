from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Nutritionist, Patient, Evolution, Evaluation, Diet
from .serializers import NutritionistSerializer, PatientSerializer, EvolutionSerializers, EvaluationSerializers, DietSerializers
from .permissions import AllowPostOnlyPermission

class NutritionistView(ModelViewSet):
    
    serializer_class = NutritionistSerializer
    queryset = Nutritionist.objects.all()
    permission_classes = [AllowPostOnlyPermission,]
    
    def create(self, request):
        serializer = NutritionistSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Nutritionist.objects.create(**serializer.validated_data)
        serializer = NutritionistSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        queryset = Nutritionist.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NutritionistSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_all(self, request):
        queryset = Nutritionist.objects.all()

        if not queryset:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = NutritionistSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class PatientView(ModelViewSet):
    
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    
    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Patient.objects.create(**serializer.validated_data)
        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list_all(self, request):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        queryset = Patient.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

class EvaluationView(ModelViewSet):
    
    serializer_class = EvaluationSerializers
    queryset = Evaluation.objects.all()
    
    def create(self, request):
        serializer = EvaluationSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Evaluation.objects.create(**serializer.validated_data)
        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list_all(self, request):
        queryset = Evaluation.objects.all()
        serializer = EvaluationSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        queryset = Evaluation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_by_patient(self, request, pk):
        queryset = Evaluation.objects.filter(patientId=pk)

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        queryset = Evaluation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

class EvolutionView(ModelViewSet):
    
    serializer_class = EvolutionSerializers
    queryset = Evolution.objects.all()
    
    def create(self, request):
        serializer = EvolutionSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Evolution.objects.create(**serializer.validated_data)
        serializer = EvolutionSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
       
        evolution = Evolution.objects.filter(pk=pk).first()
        evolution.date = request.data.get('date')
        evolution.weight = request.data.get('weight')
        evolution.imc = request.data.get('imc')
        evolution.activity = request.data.get('activity')
        evolution.appetite = request.data.get('appetite')
        evolution.chewing = request.data.get('chewing')
        evolution.intestine = request.data.get('intestine')
        evolution.sleep = request.data.get('sleep')
        evolution.comments = request.data.get('comments')
        evolution.save()
        response_serializer = EvolutionSerializers(evolution)
        
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def list_all(self, request):
        queryset = Evolution.objects.all()
        serializer = EvolutionSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        queryset = Evolution.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvolutionSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_by_patient(self, request, pk):
        queryset = Evolution.objects.filter(patientId=pk)

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvolutionSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        queryset = Evolution.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        serializer = EvolutionSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DietView(ModelViewSet):
    
    serializer_class = DietSerializers
    queryset = Diet.objects.all()
    
    def create(self, request):
        serializer = DietSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Diet.objects.create(**serializer.validated_data)
        serializer = DietSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list_all(self, request):
        queryset = Diet.objects.all()
        serializer = DietSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        queryset = Diet.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DietSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_by_patient(self, request, pk):
        queryset = Diet.objects.filter(patientId=pk)

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DietSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        queryset = Diet.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        serializer = DietSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)