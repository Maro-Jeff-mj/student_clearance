# Generated by Django 4.2.3 on 2023-09-05 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='user',
            new_name='posted_by',
        ),
    ]
