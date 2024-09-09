# Generated by Django 5.1 on 2024-09-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_course_code_alter_enrollment_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='period',
            field=models.CharField(choices=[('V', 'Vespertino'), ('M', 'Matutino'), ('N', 'Noturno')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday_date',
            field=models.DateField(null=True),
        ),
    ]
