from django.http import JsonResponse

from maper.models import Maper


def list_data(request):
    return JsonResponse([{'employee_id': i.id, 'employee_name': i.employee_name} for i in Maper.objects.all()],safe=False)
# Create your views here.
