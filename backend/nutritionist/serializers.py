from rest_framework import serializers

from .models import Nutritionist, Patient, Appointment, Evaluation, Evolution

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
        
class EvaluationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Evaluation
        fields = "__all__"
        
class EvolutionSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Evolution
        fields = "__all__"