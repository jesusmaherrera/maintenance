from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from maintenance.main.models import vehicle, radio, chassis, storage_tank, carburetion_tank, chassis_maintenance, chassis_maintenance_S, chassis_maintenance_SG, storage_tank_maintenance, storage_tank_maintenance_S, storage_tank_maintenance_SG, carburetion_tank_maintenance, carburetion_tank_S, carburetion_tank_SG, service
from maintenance.main.forms import new_vehicleForm, chassis_manageForm, storage_tank_manageForm, carburetion_tank_manageForm, radio_manageForm, chassis_maintenance_manageForm, chassis_maintenance_S_manageForm

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
		vehicleForm = new_vehicleForm(request.POST)
		if vehicleForm.is_valid():
			vehicleForm.save()
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	vehicleForm = new_vehicleForm()

	return render_to_response('new_vehicle.html', {'vehicleForm': vehicleForm,}
			,context_instance = RequestContext(request))

def chassis_manageView(request, id= None, template_name = 'chassis_manage.html'):
	if id:
	  	chassisI = get_object_or_404(chassis, pk=id)
	else:
		chassisI = chassis()

	if request.method == 'POST':
		chassisForm = chassis_manageForm(request.POST, instance= chassisI)
		if chassisForm.is_valid():
			chassisForm.save()
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
			return render_to_response('index.html',context_instance = RequestContext(request))
	else:
	 	radioForm = radio_manageForm(instance=radioI)

	return render_to_response(template_name, {'radioForm': radioForm,}
			,context_instance = RequestContext(request))

def chassis_maintenance_manageView(request, id=None, template_name='chassis_maintenance_manage.html'):
    if id:
    	chassis_maintenanceI = get_object_or_404(chassis_maintenance, pk=id)
    	servicesI = chassis_maintenance_S.objects.filter(chassis_maintenance = chassis_maintenanceI)
    	servicesGroups = chassis_maintenance_SG.objects.filter(chassis_maintenance = chassis_maintenanceI)
    else:
    	chassis_maintenanceI = chassis_maintenance()
    	servicesI= None
    	servicesGroups = None
    services = service.objects.all()
    if request.method == 'POST':
        chassis_maintenanceForm = chassis_maintenance_manageForm(request.POST, instance=chassis_maintenanceI)
        if chassis_maintenanceForm.is_valid():
            chassis_maintenanceForm.save()
            # If the save was successful, redirect to another page
            return render_to_response('index.html',context_instance = RequestContext(request))
    else:
        chassis_maintenanceForm = chassis_maintenance_manageForm(instance=chassis_maintenanceI)

    return render_to_response(template_name, {
    	 'chassis_maintenanceForm': chassis_maintenanceForm, 'servicesI': servicesI, 'servicesGroups': servicesGroups, 'services':services,
    }, context_instance=RequestContext(request))

    def add_chassis_maintenanceView(request):
    	if request.method == 'POST':
    		chassis_maintenanceForm = chassis_maintenance_manageForm(request.POST, instance= chassis_maintenance())
    		chassis_maintenanceSForm = [chassis_maintenance_SForm(request.POST, prefix = str(x), instance= chassis_maintenance_S()) for x in range(0,3)]
    		if chassis_maintenanceForm.is_valid() and all([chms.is_valid() for chms in chassis_maintenance_SForm]):
    			new_chassis_maintenance = chassis_maintenanceForm.save()
    			for chmd in chassis_maintenanceSForm:
    				new_chmService =chmd.save(commit=False)
    				new_chmService.chassis_maintenance = new_chassis_maintenance
    				new_chmService.save()
    			return HttpResponseRedirect('/chassis_maintenance/add/')
    		else:
    			chassis_maintenanceForm = chassis_maintenance_manageForm(instance = chassis_maintenance())
    			chassis_maintenanceSForm = [chassis_maintenance_SForm(request.POST, prefix = str(x), instance= chassis_maintenance_S()) for x in range(0,3)]
   			return render_to_response('add_chassis_maintenance.html', {'chassis_maintenanceForm': chassis_maintenanceForm, 'chassis_maintenanceSForm': chassis_maintenanceSForm})

	def all(items):
		import operator
		return reduce(operator.and_, [bool(item) for item in items])
