# Generated by Django 4.0.2 on 2022-04-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
