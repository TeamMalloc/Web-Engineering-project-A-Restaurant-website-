# Generated by Django 4.1.3 on 2023-01-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourRestarant', '0005_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='rate',
            field=models.IntegerField(),
        ),
    ]