# Generated by Django 3.0.8 on 2021-04-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Classe_therap', models.CharField(max_length=255)),
                ('Nom_comercial', models.CharField(max_length=255)),
                ('Laboratoire', models.CharField(max_length=255)),
                ('Denomination_med', models.CharField(max_length=255)),
                ('Forme_pharmacetique', models.TextField(max_length=255)),
                ('Duree_conservation', models.CharField(max_length=255)),
                ('Remboursable', models.BooleanField()),
                ('Lot', models.TextField(max_length=255)),
                ('Date_de_Fabrication', models.TextField(max_length=255)),
                ('Date_de_Premption', models.TextField(max_length=255)),
                ('Description', models.TextField(max_length=255)),
                ('Prix', models.FloatField()),
                ('Quantite', models.IntegerField()),
                ('CodeBarre', models.CharField(max_length=15)),
            ],
        ),
    ]
