from django.db import models

# Create your models here.
class Action(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name


class Man(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class UserAction(models.Model):
    action = models.ForeignKey(Action, on_delete = models.CASCADE)
    order = models.IntegerField()
    man = models.ForeignKey(Man,on_delete = models.CASCADE)   

    def __str__(self):
        return '{} {} {}'.format(self.man, self.action, self.order)
        