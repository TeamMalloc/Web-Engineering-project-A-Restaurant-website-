# Generated by Django 4.1.3 on 2023-01-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourRestarant', '0003_alter_continentalfood_foodimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_A_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('people', models.CharField(max_length=50)),
                ('messagess', models.CharField(max_length=300)),
            ],
        ),
    ]
