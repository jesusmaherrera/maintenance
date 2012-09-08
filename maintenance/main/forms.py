from django import forms
from maintenance.main.models import *

class new_vehicleForm(forms.ModelForm):
	class Meta:
		model = vehicle

class chassis_manageForm(forms.ModelForm):
	class Meta:
		model = chassis

class storage_tank_manageForm(forms.ModelForm):
	class Meta:
		model = storage_tank

class carburetion_tank_manageForm(forms.ModelForm):
	class Meta:
		model = carburetion_tank

class radio_manageForm(forms.ModelForm):
	class Meta:
		model = radio

class chassis_maintenance_manageForm(forms.ModelForm):
	class Meta:
		model = chassis_maintenance
		exclude = ('chassis',)

class chassis_maintenance_S_manageForm(forms.ModelForm):
	class Meta:
		model = chassis_maintenance_S
		exclude = ('chassis_maintenance',)

class chassis_maintenance_Form(forms.ModelForm):
    class Meta:
    	model=chassis_maintenance

class carburetion_tank_maintenanceForm(forms.ModelForm):
	class Meta:
		model = carburetion_tank_maintenance

class storage_tank_maintenanceForm(forms.ModelForm):
	class Meta:
		model = storage_tank_maintenance

class services_groupForm(forms.ModelForm):
	class Meta:
		model = services_group

class serviceForm(forms.ModelForm):
	class Meta:
		model = service