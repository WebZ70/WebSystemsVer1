from django.db import models


class Task(models.Model):
    name_task = models.CharField(max_length=48)

    def __str__(self):
        return "%s" % self.name_task

