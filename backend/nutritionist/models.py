from django.db import models

from cpf_field.models import CPFField

class Patient(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    document = models.CharField(max_length=15, unique=True, blank=True, null=True)
    height = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    bmi = models.PositiveIntegerField(null=True, blank=True)
    history = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return str(self.name) + " - Patient: " + str(self.id)
    
class Nutritionist(models.Model):
    id_user = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False, default="")
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, unique=True, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    address = models.CharField(max_length=255, null=True, blank=True)
    cpf = CPFField("cpf", default="")
    service = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(default=100.0)
    is_online = models.BooleanField(default=1, null=False, blank=False)
    bio = models.CharField(max_length=255, null=False, blank=False, default="")
    
    def __str__(self):
        return str(self.name) + " - Professional: " + str(self.id)

class Evaluation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="evaluation")
    patientId = models.PositiveIntegerField()
    name = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(upload_to='evaluation/')
    
    def __str__(self):
        return str(self.patient) + " - File: " + str(self.id) + str(self.name)
    
class Evolution(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="evolution")
    patientId = models.PositiveIntegerField()
    date = models.DateField(null=False, blank=False)
    weight = models.PositiveBigIntegerField(max_length=255, null=False, blank=False)
    imc = models.PositiveIntegerField(max_length=255, null=False, blank=False)
    activity = models.CharField(max_length=255, null=False, blank=False)
    appetite = models.CharField(max_length=255, null=False, blank=False)
    chewing = models.CharField(max_length=255, null=False, blank=False)
    intestine = models.CharField(max_length=255, null=False, blank=False)
    sleep = models.CharField(max_length=255, null=False, blank=False)
    comments = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return str(self.patient) + " - Evolution: " + str(self.id)
    
class Diet(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="diet")
    patientId = models.PositiveIntegerField()
    name = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(upload_to='diet/')
    
    def __str__(self):
        return str(self.patient) + " - File: " + str(self.id) + str(self.name)