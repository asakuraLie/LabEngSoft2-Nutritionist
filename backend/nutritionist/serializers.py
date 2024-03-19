from rest_framework import serializers

from .models import Nutritionist

class NutritionistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutritionist
        fields = '__all__'