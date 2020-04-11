from django.db import models
from firstbook.models import Study
from inclusions.models import Inclusion


class Experiment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Experiment name')
    description = models.TextField(verbose_name="Experiment description")
    protocole = models.TextField(verbose_name="Experiment protocole")


class StudyExperiment(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)

