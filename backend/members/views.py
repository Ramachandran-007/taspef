from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Member

def get_members(request):
    members = Member.objects.all()
    member_list = list(members.values('id', 'name', 'designation', 'subscription', 'joining_date', 'phone'))
    return JsonResponse({'members': member_list})

@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for simplicity in testing
def create_member(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            member = Member.objects.create(
                name=data.get('name'),
                designation=data.get('designation'),
                subscription=data.get('subscription', None),
                joining_date=data.get('joining_date'),
                phone=data.get('phone', None)
            )
            return JsonResponse({'message': 'Member added successfully', 'id': member.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
