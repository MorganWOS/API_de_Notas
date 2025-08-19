from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    dtnascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'materia'

class Nota_Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.FloatField()
    materia = models.ForeignKey('Materia', models.DO_NOTHING, db_column='materia', blank=True, null=True)
    aluno = models.ForeignKey('User', models.DO_NOTHING, db_column='aluno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_aluno'
