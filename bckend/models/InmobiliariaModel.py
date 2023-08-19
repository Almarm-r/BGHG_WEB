from django.db import models

class Inmuebles(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField('nombre',max_length=30, blank=False)
    age=models.CharField("edad", max_length=20)
    hab=models.CharField("color",max_length=20)
    p=models.CharField("tipo", max_length=20, blank=False)
    Area=models.CharField("tamaño",max_length=20)
    ub=models.CharField("imagen", max_length=100)
    