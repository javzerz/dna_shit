# Generated by Django 2.0.4 on 2018-04-08 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_dna', '0002_auto_20180407_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]