from website import models


def my_data(request):
    company = models.Company.objects.filter(status=True).first()
    configuration = models.Configuration.objects.filter(status=True).first()
    social = models.Social.objects.filter(status=True)
    references = models.Reference.objects.filter(status=True)
    phones = models.Phone.objects.filter(status=True)
    return locals()
