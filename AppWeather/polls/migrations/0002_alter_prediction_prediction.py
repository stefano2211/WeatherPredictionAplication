# Generated by Django 4.2.2 on 2023-06-15 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='prediction',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=10),
        ),
    ]
