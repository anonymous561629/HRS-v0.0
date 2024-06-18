from django.shortcuts import render
from .models import Property
from .forms import AddPropertyForm
from django.contrib import messages

def properties(request):
    properties = Property.objects.all()[:6]
    context = {
        'properties': properties,
    }
    return render(request, 'properties/properties.html', context)

def property(request, property_id):
    property = Property.objects.get(id=property_id)
    context = {
        'property': property,
    }
    return render(request, 'properties/property.html', context)

def add_property(request):
    form = AddPropertyForm()
    if request.method == 'POST':
        form = AddPropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner_id = request.user
            property.save()
            messages.success(request, 'Property added successfully')
    context = {'form': form}
    return render(request, 'properties/add_property.html', context)

def search_property(request):
    user_search = request.GET['search_property'] 
    user_searched_property = Property.objects.filter(address__iexact=user_search)
    context = {
        'user_searched_property': user_searched_property,
    }
    return render(request, 'properties/search_property.html', context)