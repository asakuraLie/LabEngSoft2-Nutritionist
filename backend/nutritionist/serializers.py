from rest_framework import serializers

from .models import Nutritionist, Patient, Appointment, Event, Evaluation, Evolution, Diet

class NutritionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritionist
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        
class EventSerializer(serializers.ModelSerializer):
    
    appointment = AppointmentSerializer;
    class Meta:
        model = Event
        fields =  ["title", "start", "end", "desc", "color" ]
    
class EvaluationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"
        
        extra_kwargs = {
            'patient': {'validators': []},
            'patientId': {'validators': []}, 
        }
        
class EvolutionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = "__all__"
        
class DietSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = "__all__"