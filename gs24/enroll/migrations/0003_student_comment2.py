# Generated by Django 3.0.5 on 2020-05-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment2',
            field=models.CharField(default='available', max_length=40),
        ),
    ]
