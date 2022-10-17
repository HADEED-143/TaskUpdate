from django.contrib import admin

# Register your models here.
from DjangoFFA1.recordpaginate.API.views import casesList, AllSampledata

admin.site.register(AllSampledata)
admin.site.register(casesList)