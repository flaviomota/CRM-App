# Generated by Django 4.2.3 on 2023-08-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]
