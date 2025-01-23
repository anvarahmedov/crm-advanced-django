from django.http import HttpResponse
from django.shortcuts import render

from leads.models import Agent, Lead
from .forms import LeadForm

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
    #return HttpResponse(request.POST.get('first_name'))
    form = LeadForm()
    if (request.method == "POST"):
        print("receiving post request")
        form = LeadForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            Lead.objects.create(first_name = first_name, last_name=last_name,
                            age=age, agent=Agent.objects.get(id=1))
            print("the form is valid")
            print(form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, 'leads/lead_create.html', context)
