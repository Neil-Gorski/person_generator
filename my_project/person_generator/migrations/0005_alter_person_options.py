# Generated by Django 4.1.1 on 2022-09-28 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_generator', '0004_remove_person_image_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['surname', 'age']},
        ),
    ]