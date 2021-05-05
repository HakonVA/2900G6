from django.db import models
from django.contrib.auth.models import User

class Shopping(models.Model):
    name = models.CharField(max_length=64)
    unit = models.CharField(max_length=8, null=True, blank=True)
    amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=True, blank=True)
    checked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Shopping, self).save(*args, **kwargs)
    
    class Meta:
       ordering = ['user',]

    def __str__(self):
        return "{} {}".format(self.name, self.user)
