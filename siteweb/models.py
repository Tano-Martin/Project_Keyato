from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Commande(models.Model):
	nom = models.CharField(max_length=255)
	prenom = models.CharField(max_length=255)
	email = models.EmailField()
	telephone = models.CharField(max_length=255)
	marque = models.CharField(max_length=255)
	modele = models.CharField(max_length=255)
	annee = models.CharField(max_length=255)
	type_carburant = models.CharField(max_length=255)
	numero_chassis = models.CharField(max_length=255)
	piece = models.TextField()
	lieu_livraison = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Commande'
		verbose_name_plural = 'Commandes'

	def __str__(self):
		return self.nom

class Piece(models.Model):
	designation = models.CharField(max_length=255)
	image = models.FileField(upload_to='piece_file', blank=True, null=True)
	reference = models.CharField(max_length=255)
	numero_chassis = models.CharField(max_length=255)
	marque = models.CharField(max_length=255)
	modele = models.CharField(max_length=255)
	carburant = models.CharField(max_length=255)
	annee = models.IntegerField(default=0)
	vedette = models.BooleanField(default=False)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Piece'
		verbose_name_plural = 'Pieces'

	def __str__(self):
		return self.designation

class Contact(models.Model):
	nom = models.CharField(max_length=255)
	email = models.EmailField()
	sujet = models.CharField(max_length=255)
	message = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Contact'
		verbose_name_plural = 'Contacts'

	def __str__(self):
		return self.nom

class Entreprise(models.Model):
	nom = models.CharField(max_length=255)
	logo = models.FileField(upload_to='logo_file', blank=True, null=True)
	adresse_geographique = models.CharField(max_length=255)
	contact = models.ManyToManyField('siteweb.Telephone', related_name='contact_entreprise')
	email = models.EmailField()
	carte = models.TextField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Entreprise'
		verbose_name_plural = 'Entreprises'

	def __str__(self):
		return self.nom

class Configuration(models.Model):
	titre_apropos = models.CharField(max_length=255)
	description_apropos = HTMLField()
	image_banniere_accueil = models.FileField(upload_to='Configuration_file')
	image_banniere_piece = models.FileField(upload_to='Configuration_file')
	image_apropos = models.FileField(upload_to='Configuration_file', blank=True, null=True)
	image_instruction_apropos = models.FileField(upload_to='Configuration_file', blank=True, null=True)
	instruction_banniere_accueil = models.CharField(max_length=255)
	instruction_apropos = models.CharField(max_length=255)
	instruction_pied_site = HTMLField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Configuration'
		verbose_name_plural = 'Configurations'

	def __str__(self):
		return self.titre_apropos

class Telephone(models.Model):
	numero = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Telephone'
		verbose_name_plural = 'Telephones'

	def __str__(self):
		return self.numero

class Fait(models.Model):
	titre = HTMLField()
	nombre = models.IntegerField(default=0)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Fait'
		verbose_name_plural = 'Faits'

	def __str__(self):
		return self.titre

class Iconreseaux(models.Model):
	nom = models.CharField(max_length=255)
	icone = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Icone reseaux'
		verbose_name_plural = 'Icone reseaux'

	def __str__(self):
		return self.nom

class Reseaux(models.Model):
	icone = models.ForeignKey('siteweb.Iconreseaux', related_name='icone_reseau', on_delete=models.CASCADE)
	lien = models.URLField()
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Reseaux'
		verbose_name_plural = 'Reseaux'

	def __str__(self):
		return f'{self.icone}'

class Reference(models.Model):
	nom = models.CharField(max_length=255)
	date_add = models.DateTimeField(auto_now_add=True)
	date_update = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Reference'
		verbose_name_plural = 'References'

	def __str__(self):
		return self.nom