# Generated by Django 4.2.3 on 2023-09-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_clearanceform_posted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile-pics/'),
        ),
    ]
