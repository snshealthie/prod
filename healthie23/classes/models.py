from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from gyms.models import Gym


class Classes (models.Model):
    owner = models.ForeignKey('auth.User', related_name='classes')
    name = models.CharField(max_length=100)
    gym = models.ForeignKey(Gym, on_delete=None)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def __str__(self):
        return self.name


class Review (models.Model):
    owner = models.ForeignKey('auth.User', related_name='review_owner')
    review = models.CharField(max_length=10000)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    title = models.CharField(max_length=200)
    class_reviewed = models.ForeignKey(Classes, on_delete=None, null=True, related_name='review_set')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def __str__(self):
        return self.title
