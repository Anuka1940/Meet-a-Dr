# Generated by Django 5.1.4 on 2024-12-25 22:49

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
        ('users', '0002_remove_doctorprofile_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='category',
        ),
        migrations.RemoveField(
            model_name='doctorprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='user',
        ),
        migrations.CreateModel(
            name='DoctorListing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bio', models.TextField()),
                ('services_offered', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('profile_picture', models.ImageField(upload_to='uploads/listing')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_listing', to='users.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='DoctorProfile',
        ),
        migrations.DeleteModel(
            name='PatientProfile',
        ),
    ]
