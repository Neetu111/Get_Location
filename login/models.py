from django.db import models

class Login(models.Model):
    author = models.ForeignKey('auth.User')
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return (self.title, self.password)

class Detail(models.Model):
    user = models.ForeignKey('auth.User')
    address = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return (self.title, self.password)
