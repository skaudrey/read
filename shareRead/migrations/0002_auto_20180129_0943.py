# Generated by Django 2.0 on 2018-01-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareRead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='number',
            field=models.CharField(default='d736602c049511e89424a0afbd73a24a', max_length=32, verbose_name='编号'),
        ),
    ]
