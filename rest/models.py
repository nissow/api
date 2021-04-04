from django.db import models

# Create your models here.


class Medicament(models.Model):
	Classe_therap=models.CharField(max_length=255)
	Nom_comercial=models.CharField(max_length=255)
	Laboratoire=models.CharField(max_length=255)
	Denomination_med=models.CharField(max_length=255)
	Forme_pharmacetique=models.TextField(max_length=255)
	Duree_conservation=models.CharField(max_length=255)
	Remboursable=models.BooleanField()
	Lot=models.TextField(max_length=255)
	Date_de_Fabrication=models.TextField(max_length=255)
	Date_de_Premption=models.TextField(max_length=255)
	Description=models.TextField(max_length=255)
	Prix=models.FloatField()
	Quantite=models.IntegerField()
	CodeBarre=models.CharField(max_length=15)
