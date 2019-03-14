from django.db import models
from datetime import datetime


class Member(models.Model):
    name = models.CharField(max_length=250)
    student_id = models.DecimalField(max_digits=12, null=False, decimal_places=0)
    uid = models.CharField(max_length=250, null=False)
    join_date = models.DateTimeField(auto_now_add=True, editable=False)


class Entry(models.Model):
    member = models.ForeignKey(Member, related_name='entry', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)
