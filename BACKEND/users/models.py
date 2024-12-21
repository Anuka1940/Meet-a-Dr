from django.db import models
from django.contrib.auth.models import User

# Patient modules goes here
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    # Links the profile to a specific user. Each user can have only one PatientProfile.

# Doctor modules goes here
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    # Links the profile to a specific user.
    address = models.TextField(null=False)
    # The address field stores the doctor's address information
    services = models.TextField()
    # A services field to store a list or description of the services provided by the doctor.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

# Catergories modules goes here
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name