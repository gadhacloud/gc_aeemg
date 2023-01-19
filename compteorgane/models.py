from django.db import models

# Create your models here.
# Create your models here.
class Organe(models.Model):
    nom=models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.nom


#============================================
class Membre(models.Model):
    nom=models.CharField(max_length=40)

    def __str__(self) -> str:
        return super().__str__(self.nom)


#=========================================
class User(models.Model):
    membre=models.ForeignKey('Membre',on_delete=any)
    login=models.CharField(max_length=30)
    motDePasse=models.CharField(max_length=30)
    organe=models.ForeignKey('Organe',on_delete=any)
    type=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.membre