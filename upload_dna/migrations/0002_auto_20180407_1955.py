# Generated by Django 2.0.4 on 2018-04-08 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_dna', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Data',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='post',
            new_name='user',
        ),
    ]