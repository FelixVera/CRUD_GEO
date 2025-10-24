from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from core.forms import (
AdminAddMerbershipForm2, CliGeoposAddForm)
from core.models import (client,cligeopos)  
from django.db import (transaction, connection)






def index(request):
    template_name = 'core/index.html'
    historial_cargas = client.objects.all().prefetch_related('CLIGEO_NUMBER').order_by('-CLIENT_DMYADM')[:10]
    return render(request, template_name, {'historial_cargas': historial_cargas})




#-----------------------------#
#Client membership application#
#-----------------------------#
def client_membership_application(request):
    template_name = 'core/client_membership_application.html'
    form = AdminAddMerbershipForm2(request.POST or None)

    if request.POST:
        if form.is_valid():
            id = form.cleaned_data.get('id')
            last_name = form.cleaned_data.get('last_name')
            first_name = form.cleaned_data.get('first_name')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            dmybir = form.cleaned_data.get('dmybir')
            sex = form.cleaned_data.get('sex')
            idorigin = form.cleaned_data.get('idorigin')
            dmyadm = form.cleaned_data.get('dmyadm')
            try:
                with transaction.atomic():
                    with connection.cursor() as cursor:
                        cursor.execute("""
                            INSERT INTO client(
                                CLIENT_ID
                                ,CLIENT_LNAME
                                ,CLIENT_FNAME
                                ,CLIENT_PHONE
                                ,CLIENT_ADDRESS
                                ,CLIENT_CITY
                                ,CLIENT_DMYBIR
                                ,CLIENT_SEX
                                ,CLIENT_IDORIGIN
                                ,CLIENT_DMYADM
                                ,CLIENT_STATUS 
                            )
                            VALUES (%s,%s,%s,%s,%s
                                   ,%s,%s,%s,%s,%s, 'ACT')
                                       """,[id, last_name,first_name, phone, address, city, dmybir, sex,idorigin, dmyadm])

                messages.success(request, "Client added successfully")
                return redirect('core:cligeoposadd')

            except Exception as e:
                print(f"Database Error: {e}")
        else:
            for error in form.errors.values():
                messages.error(request, error)
                
    return render(request, template_name,{'form': form})




#---------------------#
#CLIENT GEOPOSITIONING#
#---------------------#

def cligeoposadd(request):
    template_name = 'core/geopos_add_cli.html'
    api_key = settings.GEOAPIFY_API_KEY
    if request.POST:
        form = CliGeoposAddForm(request.POST or None)
        if form.is_valid():
            

            var = form.cleaned_data
            identification= var['identification']
            type= var['type']
            length= var['length']
            latitude = var['latitude']
            observation= var['observation']
            
            try:
                cli = client.objects.get(CLIENT_ID= identification)
            except client.DoesNotExist:
                messages.error(request,"No se encontro un cliente con esa identificacion")
                return redirect('core:index')
            
            cligeopos.objects.create(
                CLIGEO_NUMBER=cli
                ,CLIGEO_TYPPOS=type
                ,CLIGEO_LATITUDE = latitude
                ,CLIGEO_LENGHT = length
                ,CLIGEO_OBSER = observation
                
            )
            
            messages.success(request, "Geopos registered succesfully.")
            return redirect('core:index')
        else:
            print("form.errors: ",form.errors)
    else:
        form = CliGeoposAddForm()

    
    return render(request, template_name, {'form': form, 'api_key':api_key   })

            

