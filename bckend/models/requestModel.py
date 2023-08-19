from django.db import models
from .petModel import PetModel
from .managerModel import User

class RequestModel(models.Model):
    request_id=models.BigAutoField(primary_key=True)
    applicant_name=models.CharField('nombre_solicitante', max_length=30, blank=False)
    applicant_last_name=models.CharField('apellido_solicitante', max_length=30, blank=False)
    document_id=models.CharField('documento',max_length=20)
    address=models.CharField('direccion', max_length=100)
    phone=models.CharField('telefono', max_length=30, blank=False)
    email=models.fields.EmailField('email',max_length=100, blank=False)
    reason=models.CharField('Descripción', max_length=100)
    request_status=models.CharField('estado',max_length=30)
    id=models.ForeignKey(InmobiliariaModel,on_delete=models.CASCADE)
    admin_id=models.ForeignKey(User, on_delete=models.CASCADE)
