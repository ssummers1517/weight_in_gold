from django.shortcuts import render
from django.http import JsonResponse
from .models import ConversionFromPounds
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def convert(request):
# Every time the convert view is called, init is called.
	init(request)
# The conversion object will always be the first object.
	conv = ConversionFromPounds.objects.get(pk=1)

# If there is a from parameter, that is set to a variable.
	if 'from' in request.GET:
		unitToConvertFrom = request.GET['from']
# Otherwise, JSON containing an error message will be returned.
	else:
		response = {'Error' : "Invalid unit conversion request."}
	
# If there is a to parameter, that is set to a variable.
	if 'to' in request.GET:
		unitToConvertTo = request.GET['to']
# If the to parameter from the GET request matches the database, the calculation is performed, and the JSON containing the measurement type and converted weight is returned.
		if unitToConvertTo == conv.to:
			if 'value' in request.GET:
				whatToConvert = float(request.GET['value'])
				if isinstance(whatToConvert, float):
					convertedNumber = float(whatToConvert) * conv.multiplier
					response = {"Units" : unitToConvertTo,"Value" : convertedNumber}
# Anything else returns JSON with an error message.
				else:
					response = {'Error': "Invalid unit conversion request."}
			else:
				response = {'Error' : "Invalid unit conversion request."}
		else:
			response = {'Error' : "Invalid unit conversion request."}
	else:
		response = {'Error' : "Invalid unit conversion request."}
		
	return JsonResponse(response)
	
def init(request):
# init creates a new ConversionFromPounds object representing troy ounces and 14.5833 being the value to multiply to pounds to get troy ounces.
	c = ConversionFromPounds(to="t_oz", multiplier=14.5833)
	c.save()
	
	return c