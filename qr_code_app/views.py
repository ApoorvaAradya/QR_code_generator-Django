from django.shortcuts import render

# Create your views here.
# qr_code_app/views.py

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import generate_qr_code

@csrf_exempt
def generate_qr_code_view(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if not data:
            return JsonResponse({'error': 'No data provided'}, status=400)

        qr_code_image = generate_qr_code(data)
        response = HttpResponse(qr_code_image, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="qr_code.png"'
        return response

    return JsonResponse({'error': 'POST request required'}, status=400)
