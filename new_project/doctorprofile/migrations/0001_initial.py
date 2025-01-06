# Generated by Django 5.1.4 on 2024-12-30 19:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('manageusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('practice_name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('services_offered', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=8)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('image', models.ImageField(upload_to='uploads/doctor_profiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to='manageusers.user')),
            ],
        ),
    ]
