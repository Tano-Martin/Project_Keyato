<p align="center">
    <img src="static\images\logo.png">
</p>


Information de structure du code
---------------------------------

### Technologies utilisées

* Python
* JavaScript
* VueJs (Framework JavaScript)
* Django (Framework Python)
* Bootstrap 4 (Framework CSS3)

# Langage de dynamisation

`Python`

### Configuration

**1. Fait les migration**

```bash
$ python manage.py migrate
``` 

*NB :*

```bash
En cas de modification des modèles, faire :
$ python manage.py makemigration
$ python manage.py migrate
``` 

**2. Création de super utilisateur pour accéder à l'interface de dynamisation du site**

```bash
$ python manage.py createsuperuser
```

### Modèle et champs
* Order: `Recupère et stock les informartions de commande depuis le formulaire de commande`
    - lastname = models.CharField
    - firstname = models.CharField
    - email = models.EmailField
    - phone = models.CharField
    - brand = models.CharField
    - modele = models.CharField
    - year = models.CharField
    - fuel_type = models.CharField
    - chassis_number = models.CharField
    - part = models.TextField
    - place_delivery = models.CharField

* Part: `Stock et affiche les pièces sur le site`
    - designation = models.CharField
    - picture = models.FileField
    - reference = models.CharField
    - chassis_number = models.CharField
    - brand = models.ForeignKey
    - modele = models.CharField
    - fuel_type = models.CharField
    - year = models.CharField
    - featured = models.BooleanField

* Contact: `Stock les information du formulaire de contact`
    - name = models.CharField
    - email = models.EmailField
    - suject = models.CharField
    - message = models.TextField

* Company: `Affiche les informations de l'entreprise sur le site`
    - name = models.CharField
    - logo = models.FileField
    - address = models.CharField
    - contact = models.ManyToManyField
    - mail = models.ManyToManyField
    - maps = models.TextField

* Configuration: `Affiche les informations de l'entreprise sur le site`
    - about_title = models.CharField
    - about_description = HTMLField
    - about_picture = models.FileField
    - about_picture_instruction = models.FileField
    - about_instruction = HTMLField
    - banner_picture_home = models.FileField
    - banner_picture_part = models.FileField
    - banner_instruction = models.CharField
    - footer_instuction = HTMLField

* Phone: `Affiche les différents contacts de l'entreprise`
    - number = models.CharField

* Fact: `Affiche les faits et informations de services de l'entreprise en terme de chiffres`
    - title = HTMLField
    - number = models.IntegerField

* Socialicon: `Afficher les icones des moyens de contact en ligne de l'entreprise`
    - name = models.CharField
    - icon = models.CharField
    **NB :** les classes icones utiliser sont 
        `icon-whatsapp`
        `icon-facebook`
        `icon-google`

* Social: `Affiche les différents liens vers les moyens de contact en ligne de l'entreprise`
    - icon = models.ForeignKey
    - link = models.CharField

* Reference: `Affiche le nom des références des l'entreprise`
    - name = models.CharField

* Brand: `Affiche dans l'interface administrateur les différentes marques de pièces fournis par l'entreprise`
    - name = models.CharField

* Mail: `Affiche dans l'interface administrateur les différentes email de l'entreprise`
    - email = models.EmailField


