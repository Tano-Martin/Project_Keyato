import re
import json
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from django.core.paginator import Paginator
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mass_mail


# Create your views here.
def index(request):
    is_index = True
    parts = models.Part.objects.filter(featured=True)
    company = models.Company.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    facts = models.Fact.objects.filter(status=True)
    return render(request, "index.html", locals())


def about(request):
    is_about = True
    company = models.Company.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    return render(request, "about.html", locals())


def part(request):
    is_part = True
    part = models.Part.objects.filter(status=True).order_by("-date_add")[:210]

    paginator = Paginator(part, 21)
    page = request.GET.get("page")
    parts = paginator.get_page(page)
    return render(request, "part.html", locals())


def part_detail(request, id_part):
    part = get_object_or_404(models.Part, id=id_part)
    associated_parts = models.Part.objects.filter(brand=part.brand).exclude(
        chassis_number=part.chassis_number
    )[:3]
    is_part = True
    return render(request, "part_detail.html", locals())


def contact(request):
    is_contact = True
    company = models.Company.objects.filter(status=True).first()
    phones = models.Phone.objects.filter(status=True)
    return render(request, "contact.html", locals())


def order(request, id_part):
    is_index = True
    part = get_object_or_404(models.Part, id=id_part)
    parts = models.Part.objects.filter(featured=True)
    company = models.Company.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    facts = models.Fact.objects.filter(status=True)
    return render(request, "order.html", locals())


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
        name = json.loads(request.POST.get("name"))
        suject = json.loads(request.POST.get("suject"))
        message = json.loads(request.POST.get("message"))

        if (
            email.isspace()
            or email == ""
            or suject.isspace()
            or suject == ""
            or message.isspace()
            or message == ""
        ):
            success = False
            test_message = "Veuillez remplir les champs vides, s'il vous plaît !"
        elif is_email(email):
            success = False
            test_message = "Veuillez saisir un email valide !"
        else:
            contact, created = models.Contact.objects.get_or_create(
                name=name, suject=suject, message=message, email=email
            )
            contact.save()
            if created:
                message = f"Nom et Prénoms : {name}\nEmail : {email}\nSujet : {suject}\nMessage :\n\t{message}"
                # message1 = (suject, message, email, ["info@keyato.net"])
                # message2 = (suject, message, email, ["kofficedric1993@gmail.com"])
                # message3 = (suject, message, email, ["sheilla.yoboue@keyato.net"])
                # send_mass_mail((message1, message2, message3), fail_silently=False)
                test_message = "Votre message a bien été envoyé !"
            else:
                test_message = "Votre message a déjà été envoyé !"

    datas = {"success": success, "test_message": test_message}

    return JsonResponse(datas, safe=False)


@csrf_exempt
def orderPost(request):
    success = True
    test_message = ""
    if request.method == "POST":
        lastname = json.loads(request.POST.get("lastname"))
        firstname = json.loads(request.POST.get("firstname"))
        email = json.loads(request.POST.get("email"))
        phone = json.loads(request.POST.get("phone"))
        brand = json.loads(request.POST.get("brand"))
        modele = json.loads(request.POST.get("modele"))
        year = json.loads(request.POST.get("year"))
        fuel_type = json.loads(request.POST.get("fuel_type"))
        chassis_number = json.loads(request.POST.get("chassis_number"))
        part = json.loads(request.POST.get("part"))
        place_delivery = json.loads(request.POST.get("place_delivery"))

        if (
            phone.isspace()
            or phone == ""
            or part.isspace()
            or part == ""
        ):
            success = False
            test_message = "Veuillez remplir les champs vides, s'il vous plaît !"
        else:
            commande, created = models.Order.objects.get_or_create(
                lastname=lastname,
                firstname=firstname,
                email=email,
                phone=phone,
                brand=brand,
                modele=modele,
                year=year,
                fuel_type=fuel_type,
                chassis_number=chassis_number,
                part=part,
                place_delivery=place_delivery,
            )
            commande.save()
            if created:
                message = f"Nom et Prénoms : {lastname} {firstname}\nEmail : {email}\nTéléphone : {phone}\n\n\t\t\t INFORMATION COMMANDE :\nMarque : {brand}\nModèle : {modele}\nAnnée : {year}\nType de carburant : {fuel_type}\nNuméro de chassis : {chassis_number}\nPièce(s) : \n\t{part}\n\nLieu de livraison : {place_delivery}"
                # message1 = (
                #     "Commande client", 
                #     message, email, 
                #     ["info@keyato.net"]
                # )
                # message2 = (
                #     "Commande client",
                #     message,
                #     email,
                #     ["kofficedric1993@gmail.com"],
                # )
                # message3 = (
                #     "Commande client",
                #     message,
                #     email,
                #     ["sheilla.yoboue@keyato.net"],
                # )
                # send_mass_mail((message1, message2, message3), fail_silently=False)
                test_message = (
                    "Commande effectuée avec succès. Nous vous contacterons bientôt..."
                )
            else:
                test_message = "Commande effectuée a déjà été passée..."

    datas = {"success": success, "test_message": test_message}

    return JsonResponse(datas, safe=False)
