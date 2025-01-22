from django.http import HttpResponse
from django.shortcuts import render

from leads.models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context=context)

def lead_detail(request, pk):
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)

def lead_create(request):
    return render(request, 'leads/lead_create.html', context)
