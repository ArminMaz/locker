from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=250, null=True)
    student_id = models.DecimalField(max_digits=12, null=True, decimal_places=0)
    uid = models.CharField(null=False, max_length=50, default='')
    join_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.name)


class Entry(models.Model):
    member = models.ForeignKey(Member, related_name='entry', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    approved = models.BooleanField(default=False, null=False)
    uid = models.CharField(null=False, max_length=50, default='')
