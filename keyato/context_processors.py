from siteweb import models


def my_data(request):
    entreprise = models.Entreprise.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    sociaux = models.Reseaux.objects.filter(status=True)
    references = models.Reference.objects.filter(status=True)
    telephones = models.Telephone.objects.filter(status=True)
    return locals()