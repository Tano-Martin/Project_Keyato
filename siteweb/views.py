from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.core.paginator import Paginator

import re
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    is_index = True
    pieces = models.Piece.objects.filter(vedette=True)
    entreprise = models.Entreprise.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    faits = models.Fait.objects.filter(status=True)
    return render(request, "index.html", locals())

def about(request):
    is_about = True
    entreprise = models.Entreprise.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    return render(request, "about.html", locals())

def part(request):
    is_part = True
    piece = models.Piece.objects.filter(status=True)
    
    paginator = Paginator(piece, 15)
    page = request.GET.get('page')
    pieces = paginator.get_page(page)
    return render(request, "part.html", locals())

def part_detail(request, id_part):
    part = get_object_or_404(models.Piece, id=id_part)
    piece_associees = models.Piece.objects.filter(marque=part.marque)
    is_part = True
    return render(request, "part_detail.html", locals())

def contact(request):
    is_contact = True
    entreprise = models.Entreprise.objects.filter(status=True).first()
    telephones = models.Telephone.objects.filter(status=True)
    return render(request, "contact.html", locals())

def is_email(email):
    try:
        validate_email(email)
        return True
    except:
        return False

@csrf_exempt
def contactPost(request):
    success = True
    test_message = ""
    if request.method == "POST":
        email = json.loads(request.POST.get("email"))
        nom = json.loads(request.POST.get("nom"))
        sujet = json.loads(request.POST.get("sujet"))
        message = json.loads(request.POST.get("message"))

        if (
            email.isspace()
            or email == ""
            or sujet.isspace()
            or sujet == ""
            or nom.isspace()
            or nom == ""
            or message.isspace()
            or message == ""
        ):
            success = False
            test_message = "Veuillez remplir les champs vides, s'il vous plaît !"
        elif is_email(email):
            success = False
            test_message = "Veuillez saisir un email valide !"
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", nom):
            success = False
            test_message = "Veuillez saisir un nom valide !"
        else:
            contact, created = models.Contact.objects.get_or_create(
                nom=nom, sujet=sujet, message=message, email=email
            )
            contact.save()
            if created:
                # message = f"Nom et Prénoms : {nom}\nEmail : {email}\nSujet : {sujet}\n\n{message}"
                # send_mail(sujet, message, email, [settings.EMAIL_HOST_USER], fail_silently=False)
                test_message = "Votre message a bien été envoyé !"
            else:
                test_message = "Votre message est déjà envoyé !"

    datas = {"success": success, "test_message": test_message}

    return JsonResponse(datas, safe=False)

@csrf_exempt
def commandePost(request):
    success = True
    test_message = ""
    if request.method == "POST":
        nom = json.loads(request.POST.get("nom"))
        prenom = json.loads(request.POST.get("prenom"))
        email = json.loads(request.POST.get("email"))
        telephone = json.loads(request.POST.get("telephone"))
        marque = json.loads(request.POST.get("marque"))
        modele = json.loads(request.POST.get("modele"))
        annee = json.loads(request.POST.get("annee"))
        type_carburant = json.loads(request.POST.get("type_carburant"))
        numero_chassis = json.loads(request.POST.get("numero_chassis"))
        piece = json.loads(request.POST.get("piece"))
        lieu_livraison = json.loads(request.POST.get("lieu_livraison"))

        if (
            nom.isspace() or nom == "" or 
            prenom.isspace() or prenom == "" or 
            email.isspace() or email == "" or 
            telephone.isspace() or telephone == "" or 
            marque.isspace() or marque == "" or 
            modele.isspace() or modele == "" or 
            annee.isspace() or annee == "" or 
            type_carburant.isspace() or type_carburant == "" or 
            numero_chassis.isspace() or numero_chassis == "" or 
            piece.isspace() or piece == "" or 
            lieu_livraison.isspace() or lieu_livraison == ""

        ):
            success = False
            test_message = "Veuillez remplir les champs vides, s'il vous plaît !"
        elif is_email(email):
            success = False
            test_message = "Veuillez saisir un email valide !"
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", nom):
            success = False
            test_message = "Veuillez saisir un nom valide !"
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", prenom):
            success = False
            test_message = "Veuillez saisir un prénom valide !"
        else:
            commande, created = models.Commande.objects.get_or_create(
                nom=nom, prenom=prenom, email=email, telephone=telephone,
                marque=marque, modele=modele, annee=annee, type_carburant=type_carburant,
                numero_chassis=numero_chassis, piece=piece, lieu_livraison=lieu_livraison
            )
            commande.save()
            if created:
                # message = f"Nom et Prénoms : {nom} {prenom}\nEmail : {email}\nTéléphone : {telephone}\n\n_____ INFORMATION COMMANDE _____\nMarque : {marque}\nModèle : {modele}\nAnnée : {annee}\nType de carburant : {type_carburant}\nNuméro de chassis : {numero_chassis}\n Pièce(s) : \n\t{piece}\n\nLieu de livraison : {lieu_livraison}"
                # send_mail("Commande client", message, email, [settings.EMAIL_HOST_USER], fail_silently=False)
                test_message = "Commande effectuée avec succès. Nous vous contacterons bientôt..."
            else:
                test_message = "Votrecommande est déjà envoyé !"

    datas = {"success": success, "test_message": test_message}

    return JsonResponse(datas, safe=False)


