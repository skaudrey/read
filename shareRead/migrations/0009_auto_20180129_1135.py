# Generated by Django 2.0 on 2018-01-29 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareRead', '0008_student_datecreated'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='dateUpdate',
            field=models.DateField(auto_now=True),
        ),
    ]
