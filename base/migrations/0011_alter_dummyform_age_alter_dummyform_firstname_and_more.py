# Generated by Django 4.2.3 on 2023-09-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_dummyform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummyform',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dummyform',
            name='firstname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='dummyform',
            name='lastname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='dummyform',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Null', 'Null')], max_length=6, null=True),
        ),
    ]
