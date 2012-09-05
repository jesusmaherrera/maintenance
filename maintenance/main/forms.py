from django import forms
from maintenance.main.models import vehicle, chassis, storage_tank, carburetion_tank, radio, chassis_maintenance, chassis_maintenance_S

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



		
