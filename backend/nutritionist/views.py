from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Nutritionist, Patient, Appointment, Event, Evolution, Evaluation, Diet
from .serializers import NutritionistSerializer, PatientSerializer, AppointmentSerializer, EventSerializer, EvolutionSerializers, EvaluationSerializers, DietSerializers

class NutritionistView(ModelViewSet):
    
    serializer_class = NutritionistSerializer
    queryset = Nutritionist.objects.all()
    
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

class AppointmentView(ModelViewSet):
    
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    
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
    
    def retrieve(self, request, pk):
        queryset = Appointment.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EventView(ModelViewSet):
    
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    
    def create(self, request):
        serializer = EventSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Event.objects.create(**serializer.validated_data)
        serializer = EventSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list_all(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        queryset = Event.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer(queryset)

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
    
    def update(self, request, pk):
        serializer = EvaluationSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Evaluation.objects.filter(pk=pk).first()
        queryset.update(**serializer.validated_data)
        queryset.save()
        response_serializer = EvaluationSerializers(queryset)
        
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    def list_all(self, request):
        queryset = Evaluation.objects.all()
        serializer = EvaluationSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        queryset = Evaluation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

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
        serializer = EvolutionSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Evolution.objects.filter(pk=pk).first()
        queryset.update(**serializer.validated_data)
        queryset.save()
        response_serializer = EvolutionSerializers(queryset)
        
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