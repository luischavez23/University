from django.db import models

class Course(models.Model):
    id_course = models.CharField(max_length=6, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    credit = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return self.name