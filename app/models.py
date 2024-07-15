from django.db import models
from django.contrib.auth.models import User

class Cost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='example')
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title