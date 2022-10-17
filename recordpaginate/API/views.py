from django.contrib.sites import requests
from django.shortcuts import render
from requests import Response
from rest_framework import generics
from .models import cases#, quarantine, sqliteseq, labs, vaccine, summery
from .serializers import casesSerializer#, labsSerializer, quarantineSerializer, sqliteseqSerializer, vaccineSerializer, summerySerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from django.core.paginator import Paginator

class AllSampledata(generics.ListAPIView):
   """ url = "https:localhost:8080/Alldata"
    data = requests.get(url)"""

def get(self, request, data):
        data = data.json()
        key = list.self(keys())

        sampledata = [casesList]
        for key in casesList:
           sampledata.append([key])# Data will Receive in queue and also implement FIFO

        if casesList.pop(self.key):
            return self.key[-1]    #Lifo implementation

            return {'Message': 'Success', data :  sampledata}


    def post(self):
        parser = requests.RequestParser()
        casesList.objects.all(required=True)
        args = parser.parse_args()
        return {'message': 'Cases data', 'data':args}
        data = {"Success" : self.data}
        return Response(data)

    def delete(self, identifier):
        queryset = cases.objects.all()

        if not (identifier in self):
            return {'message': 'cases not found', 'data':{}}, 404
        del self[identifier]
        return {'Message'" DATA HAS BEEN DELETED"}

def keys():
    pass
class casesList(generics.ListAPIView):

    def cases(self, request):
        cases = casesList.objects.all()
        url = "https:localhost:8080/cases"
        data = requests.get(url)
        data = data.json()
        for x in data:
            if x.get("cases").lower()==cases.lower():
                datacases = x
                break
            else:
                datacases = "null"
                continue
        if datacases == "null":
            return Response({"error: Enter valid name"})
        data = {"success" : datacases}
        return Response(data)


        """paginator = Paginator(cases, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        queryset = cases.objects.all()
        serializer_class = casesSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id']
        return render(request=request, context={'cases'})"""

    @classmethod
    def pop(cls, key):
        pass


"""class labList(ListAPIView.generic):
    def get(self):
        queryset = labs.objects.all()
        serializer_class = labsSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id']

class quarantine(ListAPIView):
    queryset = quarantine.objects.all()
    serializer_class = quarantineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class sqliteseq(ListAPIView):
    queryset = sqliteseq.objects.all()
    serializer_class = sqliteseqSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class summery(ListAPIView):
    queryset = summery.objects.all()
    serializer_class = summerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

class vaccine(ListAPIView):
    queryset = vaccine.objects.all()
    serializer_class = vaccineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']"""