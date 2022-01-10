# Site web - Keya Automotive Services

*** Description du site ***
    ```Site de présentation de l'entreprise et de ses services, avec possibilité de passer des commandes de pièces en ligne.```

*** Technologies utilisées ***
    - Python
    - JavaScript
    - VueJs (Framework JavaScript)
    - Django (Framework Python)
    - Bootstrap 4 (Framework CSS3)

*** Langage de dynamisation ***
    - Python

*** Modèle et champs ***
    * Commande:
        - nom = models.CharField
        - prenom = models.CharField
        - email = models.EmailField
        - telephone = models.CharField
        - marque = models.CharField
        - modele = models.CharField
        - annee = models.CharField
        - type_carburant = models.CharField
        - numero_chassis = models.CharField
        - piece = models.TextField
        - lieu_livraison = models.CharField

    * Piece:
        - designation = models.CharField
        - image = models.FileField
        - reference = models.CharField
        - numero_chassis = models.CharField
        - marque = models.ForeignKey
        - modele = models.CharField
        - carburant = models.CharField
        - annee = models.CharField
        - vedette = models.BooleanField

    * Contact:
        - nom = models.CharField
        - email = models.EmailField
        - sujet = models.CharField
        - message = models.TextField

    * Entreprise:
        - nom = models.CharField
        - logo = models.FileField
        - adresse_geographique = models.CharField
        - contact = models.ManyToManyField
        - email = models.EmailField
        - carte = models.TextField

    * Configuration:
        - titre_apropos = models.CharField
        - description_apropos = HTMLField
        - image_banniere_accueil = models.FileField
        - image_banniere_piece = models.FileField
        - image_apropos = models.FileField
        - image_instruction_apropos = models.FileField
        - instruction_banniere_accueil = models.CharField
        - instruction_apropos = models.CharField
	    - instruction_pied_site = HTMLField

    * Telephone:
	    - numero = models.CharField

    * Fait:
	    - titre = HTMLField
	    - nombre = models.IntegerField

    * Iconreseaux:
        - nom = models.CharField
        - icone = models.CharField

    * Reseaux:
        - icone = models.ForeignKey
        - lien = models.CharField

    * Reference:
	    - nom = models.CharField

    * Marque:
        - nom = models.CharField