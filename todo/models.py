from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    is_complete = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_created=True, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class TodoModelV2(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.title