# contacts/views.py
from django.shortcuts import render
from .models import FamilyMember

def contact_list(request):
    members = FamilyMember.objects.all().order_by('name')
    return render(request, 'contacts/contact_list.html', {'members': members})