from django.db import models

APPOINTMENT_OPTIONS = (
    ('0', 'CANCELED'),
    ('1', 'PENDING'),
    ('2', 'CONFIRMED'),
)

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
    name = models.CharField(max_length=120, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    document = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
    is_online = models.BooleanField(default=1, null=False, blank=False)
    summary = models.TextField(max_length=500, null=True, blank=True)
    patients = models.ManyToManyField(Patient, blank=True, null=True)
    
    def __str__(self):
        return str(self.name) + " - Professional: " + str(self.id)

class Appointment(models.Model):
    professional = models.ForeignKey(Nutritionist, on_delete=models.CASCADE, related_name="appointments")
    patientId = models.PositiveIntegerField(unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    datetime = models.DateTimeField(null=False, blank=False)
    is_online = models.BooleanField(null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=APPOINTMENT_OPTIONS, null=True, blank=True)

    def __str__(self):
        return str(self.professional) + " - Appoint: " + str(self.id)
    
class Event(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="event")
    title = models.CharField(max_length=255, null=False, blank=False)
    start = models.DateTimeField(null=False, blank=False)
    end = models.DateTimeField(null=False, blank=False)
    desc = models.CharField(max_length=255, null=False, blank=False)
    color = models.CharField(max_length=255, default="#CCBAF7")    
    
    def __str__(self):
        return str(self.title) + " - Event: " + str(self.id) + " - Appoint: " + str(self.appointment)

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