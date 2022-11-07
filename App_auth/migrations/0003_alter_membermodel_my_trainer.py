# Generated by Django 3.2.16 on 2022-11-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_auth', '0002_alter_membermodel_my_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membermodel',
            name='my_trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_trainer', to='App_auth.trainermodel'),
        ),
    ]
