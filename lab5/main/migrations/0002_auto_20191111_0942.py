# Generated by Django 2.2.7 on 2019-11-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
