from django.db import models
import statistics


class Study(models.Model):
    name = models.CharField(verbose_name="Study name", max_length=100)
    main_purpose = models.CharField(verbose_name="Main purpose", max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    quick_descritpion = models.TextField(verbose_name="Quick description", blank=True, max_length=500)

    def meanrate(self):
        lst = []
        for i in Comment.objects.filter(study=self):
            lst.append(i.rate)
        if len(lst) != 0:
            return statistics.mean(lst)
        else:
            return 0

    def __str__(self):
        return self.name.title()


class Comment(models.Model):
    CHOICES = [(i, i) for i in range(6)]

    name = models.CharField(verbose_name="Name", max_length=100)
    study = models.ForeignKey('Study', on_delete=models.CASCADE)
    rate = models.IntegerField(verbose_name="Evaluation", choices=CHOICES, blank=0)
    commentary = models.TextField(verbose_name="Commentary", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
