# Generated by Django 3.2.4 on 2021-06-18 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ediarists_adm', '0003_alter_diarist_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='diarist',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
