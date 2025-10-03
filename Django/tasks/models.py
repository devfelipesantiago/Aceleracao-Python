import datetime
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    status_list = [("pending", "Pending"), ("doing", "Doing"), ("done", "Done")]
    STATUS = models.CharField(choices=status_list, verbose_name="Status do Pedido")
    description = models.TextField()
    date = models.DateField(default=datetime.date.today())
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
