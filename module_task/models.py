from django.db import models


class Task(models.Model):
    name_task = models.CharField(max_length=48)

    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return "%s" % self.name_task


class FileTask(models.Model):
    file = models.FileField(default=0)
    task = models.ForeignKey(Task, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.file

