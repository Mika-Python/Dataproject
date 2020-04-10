from django.db import models
from firstbook.models import Study
from datetime import date


class Patient(models.Model):

    FEMALE = 'female'
    MALE = 'male'

    CHARACTER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    identification = models.CharField(verbose_name="Patient Anonymisation", max_length=100)
    birth_date = models.DateField(verbose_name="Date of birth", blank=False)
    gender = models.CharField(verbose_name="Gender", choices=CHARACTER_CHOICES, max_length=20)
    size = models.IntegerField(verbose_name="Size", help_text="(cm)")
    weight = models.IntegerField(verbose_name="Weight", help_text="(kg)")
    pathologies = models.ManyToManyField('Pathology')

    def bmi(self):
        bmi = self.weight/((self.size/100)**2)
        return bmi

    def age(self):
        age = date.today() - self.birth_date
        return age.days

    def __str__(self):
        return self.identification


class Organ(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name.title()


class Pathology(models.Model):

    name = models.CharField(max_length=100)
    organ = models.ForeignKey(Organ, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name.title()} ({self.organ})"

    def __unicode__(self):
        return f"{self.name.title()}({self.organ})"


class Inclusion(models.Model):
    TEMOIN = 'temoin'
    CAS = 'patient'

    STATUS_CHOICES = (
        (TEMOIN, 'Témoin'),
        (CAS, 'Cas'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    status = models.CharField(verbose_name="Inclusion", choices=STATUS_CHOICES, max_length=20)
    inclusion_date = models.DateField(verbose_name="Inclusion date")
