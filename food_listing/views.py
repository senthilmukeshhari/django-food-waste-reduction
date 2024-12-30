from django.shortcuts import render
from django.http import JsonResponse
import json

def nearest_foods(request):
	if request.method == 'POST':
		try:
			data = json.loads(request.body)
			latitude = data.get('latitude')
			longitude = data.get('longitude')

			print(latitude, longitude)
			return JsonResponse({
				'message': 'Successfully...'
			})
		except Exception as e:
			print(e)
			return JsonResponse({
				'message': 'Failed...'
			})
	else:
		return JsonResponse({
			'message': 'Not Valied...'
		})

def food_list(request):
	return render(request, 'food_listing/foods.html')