from django.db import models
from django.urls import reverse
from PIL import Image
from django_resized import ResizedImageField


class Disease(models.Model):
    name = models.CharField(max_length=70)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='disease', on_delete=models.CASCADE)

    # def __self__(self):
    #     return self.name

    def __str__(self):
        return f'{self.name}'


class Field(models.Model):
    name = models.CharField(max_length=70)

    # def __self__(self):
    #     return self.name

    def __str__(self):
        return f'{self.name}'


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    image = ResizedImageField(default='default.svg', size=[
                              300, 300], upload_to='doctor_images')
    fields = models.ForeignKey(Field, on_delete=models.CASCADE)
    treats = models.ManyToManyField(Disease)
    link = models.URLField(null=True, blank=True)

    # def __self__(self):
    #     return self.name

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse('', kwargs={'pk': self.pk})


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=70)
    startTime = models.TimeField(null=True, blank=True)
    endTime = models.TimeField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    division = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    doctors = models.ManyToManyField(Doctor)

    # def __self__(self):
    #     return self.name

    def __str__(self):
        return f'{self.name}'

    # def get_absolute_url(self):
    #     return reverse('', kwargs={'pk': self.pk})
