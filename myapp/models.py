from django.db import models

class Account(models.Model):
    account = models.CharField(max_length=20)

    def __str__(self):
        return self.account


STATUS_CHOICES = (('pending','pending'),('approved','approved'),('rejected','rejected'))

class Data(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='pics')
    account_type = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    current_status = models.CharField(choices= STATUS_CHOICES , max_length=20)
    
    def __str__(self):
        return self.name

