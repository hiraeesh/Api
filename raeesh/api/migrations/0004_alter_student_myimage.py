# Generated by Django 3.2.9 on 2022-03-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_student_myimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='myimage',
            field=models.ImageField(default=0, upload_to='images/'),
        ),
    ]
