# Generated by Django 4.1.1 on 2022-09-26 15:40

from django.db import migrations, models
import person_generator.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('birthday_date', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('phone', models.CharField(max_length=12, validators=[person_generator.models.only_int])),
                ('photo', models.CharField(max_length=200)),
                ('birthplace', models.CharField(max_length=100)),
            ],
        ),
    ]
