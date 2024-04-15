from django.db import models

APPOINTMENT_OPTIONS = (
    ('0', 'CANCELED'),
    ('1', 'PENDING'),
    ('2', 'CONFIRMED'),
)

RESTRICTIONS_OPTIONS = (
    ('N', 'NO'),
    ('VA', 'VEGETARIAN'),
    ('VE', 'VEGAN'),
)

ALCOHOL_OPTIONS = (
    ('N', 'NO'),
    ('E', 'EVERYDAY'),
    ('S', 'SOCIALLY'),
)

SMOKER_OPTIONS = (
    ('N', 'NO'),
    ('E', 'EVERYDAY'),
    ('W', 'WEEKENDS'),
    ('S', 'SOCIALLY'),
)

APPETITE_OPTIONS = (
    ('N', 'NORMAL'),
    ('I', 'INCREASED'),
    ('D', 'DECREASED'),
)

CHEWING_OPTIONS = (
    ('N', 'NORMAL'),
    ('R', 'RAPID'),
    ('S', 'SLOW'),
)

INTESTINE_OPTIONS = (
    ('N', 'NORMAL'),
    ('C', 'CONSTIPATED'),
    ('D', 'DIARRHEIC'),
    ('V', 'VARIED'),
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
        return self.name
    
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
        return self.name

class Appointment(models.Model):
    professional = models.ForeignKey(Nutritionist, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    datetime = models.DateTimeField(null=False, blank=False)
    is_online = models.BooleanField(null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=APPOINTMENT_OPTIONS, null=True, blank=True)

    def __str__(self):
        return self.professional

class Evaluation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="evaluation")
    date = models.DateField(null=False, blank=False)
    height = models.PositiveIntegerField(null=False, blank=False)
    weight = models.PositiveBigIntegerField(null=False, blank=False)
    restrictions = models.CharField(null=False, blank=False)
    alcohol = models.CharField(null=False, blank=False, choices=ALCOHOL_OPTIONS)
    smoker = models.CharField(null=False, blank=False, choices=SMOKER_OPTIONS)
    delivery = models.CharField(null=False, blank=False)
    shopping = models.CharField(null=False, blank=False)
    living = models.CharField(null=False, blank=False)
    diets = models.CharField(null=False, blank=False)
    previousprofessional = models.CharField(null=False, blank=False)
    previousprocess = models.CharField(null=False, blank=False)
    previousweightloss = models.CharField(null=False, blank=False)
    sleepquality = models.CharField(null=False, blank=False)
    sleephours = models.CharField(null=False, blank=False)
    sleeptime = models.CharField(null=False, blank=False)
    sleepcomments = models.CharField(null=False, blank=False)
    activity = models.CharField(null=False, blank=False)
    activityfrequency = models.CharField(null=False, blank=False)
    activitycomment = models.CharField(null=False, blank=False)
    appetite = models.CharField(null=False, blank=False, choices=APPETITE_OPTIONS)
    chewing = models.CharField(null=False, blank=False, choices=CHEWING_OPTIONS)
    intestine = models.CharField(null=False, blank=False, choices=INTESTINE_OPTIONS)
    evacuation = models.CharField(null=False, blank=False)
    urination = models.CharField(null=False, blank=False)
    supplements = models.CharField(null=False, blank=False)
    allergies = models.CharField(null=False, blank=False)
    intolerance = models.CharField(null=False, blank=False)
    aversions = models.CharField(null=False, blank=False)
    comments = models.CharField(null=False, blank=False)
    
    def __str__(self):
        return self.patient
    
class Evolution(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    weight = models.CharField(null=False, blank=False)
    imc = models.PositiveIntegerField(null=False, blank=False)
    activity = models.CharField(null=False, blank=False)
    appetite = models.CharField(null=False, blank=False, choices=APPETITE_OPTIONS)
    chewing = models.CharField(null=False, blank=False, choices=CHEWING_OPTIONS)
    intestine = models.CharField(null=False, blank=False, choices=INTESTINE_OPTIONS)
    sleep = models.CharField(null=False, blank=False)
    comments = models.CharField(null=False, blank=False)
    
    def __str__(self):
        return self.patient