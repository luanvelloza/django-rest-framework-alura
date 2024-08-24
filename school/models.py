from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50, blank=False)
    cpf = models.CharField(max_length=11)
    birthday_date = models.DateField()
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
    
class Course(models.Model):

    LEVEL = {
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    }

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=False)
    level =models.CharField(max_length=1, blank=False, choices=LEVEL, default='B', null=False)

def __str__(self):
    return self.name