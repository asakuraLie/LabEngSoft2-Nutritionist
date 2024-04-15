from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Nutritionist, Patient, Appointment, Evolution, Evaluation
from .serializers import NutritionistSerializer, PatientSerializer, AppointmentSerializer, EvolutionSerializers, EvaluationSerializers

class NutritionistView(ModelViewSet):
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
    
    
    def list_from_nutritionist(self, request):
        patient_list = request.data['patient_list']
        queryset = Patient.objects.filter(pk__in=patient_list)
        serializer = PatientSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        queryset = Patient.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentView(ModelViewSet):
    def create(self, request):
        serializer = AppointmentSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Appointment.objects.create(**serializer.validated_data)
        serializer = AppointmentSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list_all(self, request):
        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list_from_nutritionist(self, request, prof):
        queryset = Appointment.objects.filter(professional=prof)
        serializer = AppointmentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Appointment.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EvaluationView(ModelViewSet):
    
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
    
    
    def list_from_nutritionist(self, request, prof):
        queryset = Evaluation.objects.filter(professional=prof)
        serializer = EvaluationSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Evaluation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)


class EvolutionView(ModelViewSet):
    
    def create(self, request):
        serializer = EvolutionSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Evolution.objects.create(**serializer.validated_data)
        serializer = EvolutionSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list_all(self, request):
        queryset = Evolution.objects.all()
        serializer = EvolutionSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list_from_nutritionist(self, request, prof):
        queryset = Evolution.objects.filter(professional=prof)
        serializer = EvolutionSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Evolution.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)