from django.urls import path
from .models import cases#, labs, quarantine, sqliteseq, summeryvaccine,
from .views import AllSampledata

urlpatterns = [
    path("Alldata/", AllSampledata.as_view(), name="AllQueue"),
    path('casesList<slug:cases>/', cases.as_view(), name='cases'),
    path('labsList<slug:labs>/', labs.as_view(), name='labs'),
    path('quarantineList<slug:labs>/', quarantine.as_view(), name='quarantine'),
    path('sqliteseqList<slug:labs>/', sqliteseq.as_view(), name='sqliteseq'),
    path('summeryList<slug:labs>/', summery.as_view(), name='summery'),
    path('vaccineList<slug:labs>/', vaccine.as_view(), name='vaccine'),
]