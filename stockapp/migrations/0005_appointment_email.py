# Generated by Django 3.1.5 on 2021-09-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0004_patient_register_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=250, null=True),
        ),
    ]
