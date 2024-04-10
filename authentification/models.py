from django.db import models



class modeuser(models.Model):
    username = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    passwordconfim = models.CharField(max_length = 30)


    def __init__(self):
        return self.username
