# Generated by Django 3.2.16 on 2022-11-04 16:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Must add 880', regex='^\\+?(88)01[3-9][0-9]{8}$')], verbose_name='Trainer_phone')),
                ('address', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Third Gender', 'Third Gender')], max_length=15)),
                ('profile_picture', models.ImageField(upload_to='trainer_picture')),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Must add 880', regex='^\\+?(88)01[3-9][0-9]{8}$')], verbose_name='Member_phone')),
                ('address', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Third Gender', 'Third Gender')], max_length=15)),
                ('profile_picture', models.ImageField(upload_to='member_picture')),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('my_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_trainer', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Must add 880', regex='^\\+?(88)01[3-9][0-9]{8}$')], verbose_name='Admin_phone')),
                ('address', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Third Gender', 'Third Gender')], max_length=15)),
                ('profile_picture', models.ImageField(upload_to='admin_picture')),
                ('joining_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]