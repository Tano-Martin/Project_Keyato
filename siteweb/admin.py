from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.

# Changer le titre de l'administration
admin.site.site_header = 'Keyato Administration'

@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'email', 'telephone', 'marque', 'modele', 'annee', 'type_carburant', 'numero_chassis', 'lieu_livraison', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['prenom', 'email', 'telephone', 'marque', 'modele', 'annee', 'type_carburant', 'numero_chassis', 'lieu_livraison', 'status']

@admin.register(models.Piece)
class PieceAdmin(admin.ModelAdmin):
	list_display = ('view_image', 'designation', 'reference', 'numero_chassis', 'marque', 'modele', 'annee', 'carburant', 'vedette', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['designation', 'reference', 'numero_chassis', 'marque', 'modele', 'annee', 'carburant', 'vedette', 'status']
	
	def view_image(self, obj):
		return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:120px">')
	view_image.short_description = "Apercu des images de image"
 
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom', 'email', 'sujet', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['email', 'sujet', 'status']

@admin.register(models.Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
	list_display = ('view_logo', 'nom', 'adresse_geographique', 'email', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	filter_horizontal = ['contact']
	list_editable = ['nom', 'adresse_geographique', 'email', 'status']
	
	def view_logo(self, obj):
		return mark_safe(f'<img src="{obj.logo.url}" style="height:100px; width:120px">')
	view_logo.short_description = "Apercu des images de logo"


@admin.register(models.Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
	list_display = ('view_image_banniere_accueil', 'view_image_banniere_piece', 'view_image_apropos', 'view_image_instruction_apropos', 'titre_apropos', 'instruction_banniere_accueil', 'instruction_apropos', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']

	def view_image_banniere_accueil(self, obj):
		return mark_safe(f'<img src="{obj.image_banniere_accueil.url}" style="height:100px; width:120px">')
	view_image_banniere_accueil.short_description = "Apercu des images de la banniere d'accueils"

	def view_image_banniere_piece(self, obj):
		return mark_safe(f'<img src="{obj.image_banniere_piece.url}" style="height:100px; width:120px">')
	view_image_banniere_piece.short_description = "Apercu des images de la banniere des pieces"

	def view_image_apropos(self, obj):
		return mark_safe(f'<img src="{obj.image_apropos.url}" style="height:100px; width:120px">')
	view_image_apropos.short_description = "Apercu des images de la banniere d'accueils"

	def view_image_instruction_apropos(self, obj):
		return mark_safe(f'<img src="{obj.image_instruction_apropos.url}" style="height:100px; width:120px">')
	view_image_instruction_apropos.short_description = "Apercu des images de la banniere des pieces"

@admin.register(models.Telephone)
class TelephoneAdmin(admin.ModelAdmin):
	list_display = ('numero', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']

@admin.register(models.Fait)
class FaitAdmin(admin.ModelAdmin):
	list_display = ('titre', 'nombre', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['nombre', 'status']

@admin.register(models.Iconreseaux)
class IconreseauxAdmin(admin.ModelAdmin):
	list_display = ('nom', 'icone', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['icone', 'status']

@admin.register(models.Reseaux)
class ReseauxAdmin(admin.ModelAdmin):
	list_display = ('lien', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']


@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
	list_display = ('nom', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
	list_per_page = 10
	list_editable = ['status']