from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from maintenance.main.models import *
from maintenance.main.forms import *

from django.core.context_processors import csrf
from django.template import RequestContext # For CSRF
from django.forms.formsets import formset_factory, BaseFormSet
from django.forms.models import inlineformset_factory

# Create your views here.
def index(request):
  	vehicles = vehicle.objects.all()
  	return render_to_response('index.html',{'vehicles':vehicles},context_instance=RequestContext(request))

def vehicle_details(request, query):
 	vehicleD = get_object_or_404(vehicle, pk=query)
	context = {'vehicle': vehicleD}
	return render_to_response('vehicle_details.html', context,context_instance=RequestContext(request))

def chassis_maintenanceView(request, query):
 	chassisD = get_object_or_404(chassis, pk=query)
 	chassis_maintenances = chassis_maintenance.objects.filter(chassis = chassisD)
	chassis_services = chassis_maintenance_S.objects.filter(chassis_maintenance__chassis = chassisD)
	chassis_services_groups = chassis_maintenance_SG.objects.filter(chassis_maintenance__chassis = chassisD)
	context = {'chassis': chassisD, 'chassis_services': chassis_services, 'chassis_services_groups':chassis_services_groups, 'chassis_maintenances': chassis_maintenances}
	return render_to_response('chassis_maintenance.html', context,context_instance=RequestContext(request))

def storage_tank_maintenanceView(request, query):
 	storage_tankD = get_object_or_404(storage_tank, pk=query)
 	storage_tank_maintenances = storage_tank_maintenance.objects.filter(storage_tank = storage_tankD)
	storage_tank_services = storage_tank_maintenance_S.objects.filter(storage_tank_maintenance__storage_tank = storage_tankD)
	storage_tank_services_groups = storage_tank_maintenance_SG.objects.filter(storage_tank_maintenance__storage_tank = storage_tankD)
	context = {'storage_tank': storage_tankD, 'storage_tank_services': storage_tank_services, 'storage_tank_services_groups':storage_tank_services_groups, 'storage_tank_maintenances': storage_tank_maintenances}
	return render_to_response('storage_tank_maintenance.html', context,context_instance=RequestContext(request))

def carburetion_tank_maintenanceView(request, query):
 	carburetion_tankD = get_object_or_404(carburetion_tank, pk=query)
 	carburetion_tank_maintenances = carburetion_tank_maintenance.objects.filter(carburetion_tank = carburetion_tankD)
	carburetion_tank_services = carburetion_tank_S.objects.filter(carburetion_tank_maintenance__carburetion_tank = carburetion_tankD)
	carburetion_tank_services_groups = carburetion_tank_SG.objects.filter(carburetion_tank_maintenance__carburetion_tank = carburetion_tankD)
	context = {'carburetion_tank': carburetion_tankD, 'carburetion_tank_services': carburetion_tank_services, 'carburetion_tank_services_groups':carburetion_tank_services_groups, 'carburetion_tank_maintenances': carburetion_tank_maintenances}
	return render_to_response('carburetion_tank_maintenance.html', context,context_instance=RequestContext(request))

def new_vehicleView(request):
	if request.method == 'POST':
		vehicleForm = new_vehicleForm(request.POST, request.FILES)
		if vehicleForm.is_valid():
			vehicleForm.save()
			vehicles = vehicle.objects.all()
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	vehicleForm = new_vehicleForm()

	return render_to_response('new_vehicle.html', {'vehicleForm': vehicleForm,}
			,context_instance = RequestContext(request))

def delete_vehicle(request, id = None):
	vehicleInstance = get_object_or_404(vehicle, pk=id)
	vehicleInstance.delete()

	vehicles = vehicle.objects.all()
  	return render_to_response('index.html',{'vehicles':vehicles},context_instance=RequestContext(request))

def chassis_manageView(request, id= None, template_name = 'chassis_manage.html'):
	if id:
	  	chassisI = get_object_or_404(chassis, pk=id)
	else:
		chassisI = chassis()

	if request.method == 'POST':
		chassisForm = chassis_manageForm(request.POST, instance= chassisI)
		if chassisForm.is_valid():
			chassisForm.save()
			vehicles = vehicle.objects.all()
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	chassisForm = chassis_manageForm(instance= chassisI)

	return render_to_response(template_name, {'chassisForm': chassisForm,}
			,context_instance = RequestContext(request))

def storage_tank_manageView(request, id = None, template_name='storage_tank_manage.html'):
	if id:
	  	storage_tankI = get_object_or_404(storage_tank, pk=id)
	else:
		storage_tankI = storage_tank()

	if request.method == 'POST':
		storage_tankForm = storage_tank_manageForm(request.POST, instance= storage_tankI)
		if storage_tankForm.is_valid():
			storage_tankForm.save()
			vehicles = vehicle.objects.all()
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	storage_tankForm = storage_tank_manageForm(instance= storage_tankI)

	return render_to_response(template_name, {'storage_tankForm': storage_tankForm,}
			,context_instance = RequestContext(request))

def carburetion_tank_manageView(request, id = None, template_name='carburetion_tank_manage.html'):
	if id:
		carburetion_tankI = get_object_or_404(carburetion_tank, pk=id)
	else:
		carburetion_tankI = carburetion_tank()

	if request.method == 'POST':
		carburetion_tankForm = carburetion_tank_manageForm(request.POST, instance= carburetion_tankI)
		if carburetion_tankForm.is_valid():
			carburetion_tankForm.save()
			vehicles = vehicle.objects.all()
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	carburetion_tankForm = carburetion_tank_manageForm(instance= carburetion_tankI)

	return render_to_response(template_name, {'carburetion_tankForm': carburetion_tankForm,}
			,context_instance = RequestContext(request))

def radio_manageView(request, id = None, template_name='radio_manage.html'):
	if id:
		radioI = get_object_or_404(radio, pk=id)
	else:
		radioI = radio()

	if request.method == 'POST':
		radioForm = radio_manageForm(request.POST, instance=radioI)
		if radioForm.is_valid():
			radioForm.save()
			vehicles = vehicle.objects.all()
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	radioForm = radio_manageForm(instance=radioI)

	return render_to_response(template_name, {'radioForm': radioForm,}
			,context_instance = RequestContext(request))

def delete_chassis_maintenance(request, id = None):
	chassis_maintenanceInstance = get_object_or_404(chassis_maintenance, pk=id)
	chassis_maintenanceInstance.delete()
	vehicles = vehicle.objects.all()

  	return render_to_response('index.html',{'vehicles':vehicles},context_instance=RequestContext(request))

def chassis_maintenance_manageView(request , id = None, id_mant = None, template_name='chassis_maintenance_manage.html'):
	# This class is used to make empty formset forms required
    # See http://stackoverflow.com/questions/2406537/django-formsets-make-first-required/4951032#4951032
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

	# chassisMaintenance_FormSet = inlineformset_factory(chassis_maintenance, chassis_maintenance_S)
	# chassisMaintenancei= get_object_or_404(chassis_maintenance , pk = id_mant)
	# chassisMaintenanceiFormSet = chassisMaintenance_FormSet(instance = chassisMaintenancei)
	
    ChassisMaintenanceS_Formset = formset_factory(chassis_maintenance_S_manageForm,can_delete=True, max_num=10, formset=RequiredFormSet)

    chassisI = get_object_or_404(chassis, pk=id)

    if id_mant:
    	chassisMaintenance = get_object_or_404(chassis_maintenance, pk=id_mant)
    else:
		chassisMaintenance = chassis_maintenance()

    if request.method == 'POST': # If the form has been submitted...
        chassis_maintenance_form = chassis_maintenance_manageForm(request.POST, instance = chassisMaintenance) # A form bound to the POST data

        # Create a formset from the submitted data
       	chassis_maintenance_S_formset = ChassisMaintenanceS_Formset(request.POST, request.FILES)
        
        if chassis_maintenance_form.is_valid() and chassis_maintenance_S_formset.is_valid():
            chassis_maintenanceI = chassis_maintenance_form.save(commit=False)
            chassis_maintenanceI.chassis = chassisI
            chassis_maintenanceI.save()
            for form in chassis_maintenance_S_formset.forms:
                chassis_maintenanceS= form.save(commit=False)
                chassis_maintenanceS.chassis_maintenance = chassis_maintenanceI
                chassis_maintenanceS.save()

            return HttpResponseRedirect('thanks') # Redirect to a 'success' page
	#cuando es uno que se va a editar            
    else:
        chassis_maintenance_form = chassis_maintenance_manageForm(instance = chassisMaintenance)
        #chassis_maintenance_S_formset = chassisMaintenanceiFormSet
        chassis_maintenance_S_formset = ChassisMaintenanceS_Formset()
    
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/ 
    c = {'chassis_maintenance_form': chassis_maintenance_form,'chassis':chassisI,
         'chassis_maintenance_S_formset': chassis_maintenance_S_formset,
        }
    c.update(csrf(request))
    
    return render_to_response(template_name, c, context_instance = RequestContext(request))


def manage_chassismaintenance2(request, id_mant = None, template_name='chassis_services_Manage.html'):
 	if id_mant:
 		chassisMaintenance = get_object_or_404(chassis_maintenance, pk=id_mant)
 	else:
 		chassisMaintenance = chassis_maintenance()
	
	chassis_maintenanceInlineFormSet = inlineformset_factory(chassis_maintenance, chassis_maintenance_S, extra=1)

	if request.method == "POST":
		formsetI = chassis_maintenanceInlineFormSet(request.POST, request.FILES, instance=chassisMaintenance)
       
    	# if formsetI.is_valid():
    	# 	formsetI.save()
    	# 	vehicles = vehicle.objects.all()
     #    	return render_to_response('index.html',context_instance = RequestContext(request))
	#sdfdsfdsf        	
	else:
		formsetI = chassis_maintenanceInlineFormSet(instance=chassisMaintenance)
		chassis_maintenance_form = chassis_maintenance_manageForm(instance = chassisMaintenance) # A form bound to the POST data
	
	return render_to_response(template_name, {"formset": formsetI,},context_instance = RequestContext(request))

def chassis_maintenance_manageinlineView(request , id = None, id_mant = None, template_name='chassis_services_Manage.html'):
	
	if id_mant:
		chassisMaintenance = get_object_or_404(chassis_maintenance, pk=id_mant)
	else:
		chassisMaintenance = chassis_maintenance()

	chassis_maintenanceInlineFormSetS = inlineformset_factory(chassis_maintenance, chassis_maintenance_S, extra=1)
	chassis_maintenanceInlineFormSetSG = inlineformset_factory(chassis_maintenance, chassis_maintenance_SG, extra=1)

	if request.method == "POST":
		formsetIS = chassis_maintenanceInlineFormSetS(request.POST, request.FILES, instance=chassisMaintenance)
		formsetISG = chassis_maintenanceInlineFormSetSG(request.POST, request.FILES, instance=chassisMaintenance)
		chassis_maintenance_form = chassis_maintenance_manageForm(request.POST, instance = chassisMaintenance)

		if chassis_maintenance_form.is_valid():
			chassis_maintenance_form.save()
    	 	
    	 	if formsetIS.is_valid() and formsetISG.is_valid():
    			formsetIS.save()
    			formsetISG.save()
    			return render_to_response(template_name, {"formsetS": formsetIS,'formsetSG':formsetISG,'chassis_maintenance_form':chassis_maintenance_form,},context_instance = RequestContext(request))  		
	#sdfdsfdsf        	
	else:
		formsetIS = chassis_maintenanceInlineFormSetS(instance=chassisMaintenance)
		formsetISG = chassis_maintenanceInlineFormSetSG(instance=chassisMaintenance)
		chassis_maintenance_form = chassis_maintenance_manageForm(instance = chassisMaintenance)
	

	return render_to_response(template_name, {"formsetS": formsetIS,'formsetSG':formsetISG,'chassis_maintenance_form':chassis_maintenance_form,},context_instance = RequestContext(request))  		

def chassis_maintenance_manageFormSet(request, object_id=None):
	chassisServiceFormSet, chassisServiceGroupFormSet = inlineformset_factory(chassis_maintenance, chassis_maintenance_S, extra = 1), inlineformset_factory(chassis_maintenance, chassis_maintenance_SG, extra = 1)
	
	if object_id:
		chassisMaintenance = chassis_maintenance.objects.get(pk=object_id)
	else:
		chassisMaintenance=chassis_maintenance()

	if request.method == 'POST':
		f=chassis_maintenance_Form(request.POST, request.FILES, instance=chassisMaintenance)

		if f.is_valid():
			created_maintenance = f.save(commit=False)
			fs, fsg = chassisServiceFormSet(request.POST,prefix='chassisServiceFormS', instance=chassisMaintenance), chassisServiceGroupFormSet(request.POST, prefix="chassisServiceFormSG", instance=chassisMaintenance)

        	if fs.is_valid() and fsg.is_valid():
        		f.save()
        		for form in fs:
        			createdform = form.save(commit=False)
        			createdform.chassis_maintenance = chassisMaintenance
        			createdform.save()
				for form in fsg:
					createdform = form.save(commit=False)
					createdform.chassis_maintenance = chassisMaintenance
        			createdform.save()
            	return render_to_response('chassis_maintenance_manageFormSet.html', {'fs': fs,'f':f,'chassisMaintenance':chassisMaintenance,}, context_instance = RequestContext(request))		
	else:
		f  = chassis_maintenance_Form(instance=chassisMaintenance)
    	fs = chassisServiceFormSet(prefix='chassisServiceFormS', instance=chassisMaintenance)
    	fsg = chassisServiceGroupFormSet(prefix='chassisServiceFormSG', instance=chassisMaintenance)
	return render_to_response('chassis_maintenance_manageFormSet.html', {'fs': fs, 'fsg':fsg, 'f':f,'chassisMaintenance':chassisMaintenance,}, context_instance = RequestContext(request))