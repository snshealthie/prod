from django.db import models

# Create your models here.

class Gym (models.Model):
    owner = models.ForeignKey('auth.User', related_name='gym')
    name = models.CharField(max_length=200)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def __str__(self):
        return self.name