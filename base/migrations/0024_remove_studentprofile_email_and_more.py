# Generated by Django 4.2.3 on 2023-09-08 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0023_alter_dummyform_firstname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='matric_number',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Null', 'Null')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='directorate',
            field=models.CharField(choices=[('Science', 'Science'), ('Engineering', 'Engineering')], max_length=12),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='program_of_study',
            field=models.CharField(choices=[('ND', 'ND'), ('HND', 'HND')], max_length=3),
        ),
        migrations.CreateModel(
            name='ClearanceForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('othernames', models.CharField(max_length=30)),
                ('department', models.CharField(choices=[('Computer Science', 'Computer Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Petroleum Engineering', 'Petroleum Engineering')], max_length=30)),
                ('date_of_birth', models.DateField(verbose_name='(mm/dd/year)')),
                ('date_of_completion', models.DateField(verbose_name='(mm/dd/year)')),
                ('phone_number', models.IntegerField()),
                ('mat_receipt_num', models.IntegerField()),
                ('mat_receipt_num_date', models.DateField(verbose_name='(mm/dd/year)')),
                ('alumini_receipt_num', models.IntegerField()),
                ('alumini_receipt_num_date', models.DateField(verbose_name='(mm/dd/year)')),
                ('school_fees_receipt_year_1', models.IntegerField()),
                ('school_fees_receipt_year_1_date', models.DateField(verbose_name='(mm/dd/year)')),
                ('school_fees_receipt_year_2', models.IntegerField()),
                ('school_fees_receipt_year_2_date', models.DateField(verbose_name='(mm/dd/year)')),
                ('enterpreneur_receipt_num', models.IntegerField()),
                ('enterpreneur_receipt_num_date', models.DateField(verbose_name='(mm/dd/year)')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]