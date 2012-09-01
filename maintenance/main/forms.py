from django import forms
from maintenance.main.models import vehicle, chassis, storage_tank, carburetion_tank, radio, chassis_maintenance

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


		

