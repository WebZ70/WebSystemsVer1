from django.db import models


class Lecture(models.Model):
    name_lecture = models.CharField(max_length=48)

    def __str__(self):
        return "%s" % self.name_lecture
