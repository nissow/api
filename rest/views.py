from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MedicamentSerializer

from .models import Medicament

# Create your views here.

@api_view(['GET'])
def Med(request):
	api_urls = {
		'ListMedicament':'/Medicament-list/',
		'Create':'/Medicament-create/',
		'Update':'/Medicament-update/',
	}
	return Response(api_urls)



@api_view(['GET'])
def MedList(request):
	Meds = Medicament.objects.all().order_by('-id')
	Medserializer = MedicamentSerializer(Meds, many=True)
	return Response(Medserializer.data)


@api_view(['POST'])
def MedCreate(request):
	Medserializer = MedicamentSerializer(data=request.data)

	if Medserializer.is_valid():
		Medserializer.save()

	return Response(Medserializer.data)

@api_view(['POST'])
def MedUpdate(request, pk):
	Med = Medicament.objects.get(id=pk)
	Medserializer = MedicamentSerializer(instance=Med, data=request.data)
	if Medserializer.is_valid():
		Medserializer.save()
	return Response(Medserializer.data)

