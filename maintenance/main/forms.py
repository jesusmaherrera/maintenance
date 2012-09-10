from django import forms
from maintenance.main.models import *
from django.forms import models
from django.forms.models import BaseInlineFormSet, inlineformset_factory

class new_vehicleForm(forms.ModelForm):
	class Meta:
		model = vehicle

class garage_manageForm(forms.ModelForm):
	class Meta:
		model = garage
		
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

class chassis_maintenanceForm(forms.ModelForm):
	class Meta:
		model = chassis_maintenance

class chassis_maintenance_sForm(forms.ModelForm):
	class Meta:
		model = chassis_maintenance_S

class chassis_maintenance_sgForm(forms.ModelForm):
	class Meta:
		model = chassis_maintenance_SG

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

class services_group_itemsForm(models.ModelForm):
	class Meta:
		model = services_group_items

class serviceForm(forms.ModelForm):
	class Meta:
		model = service

def  get_services_group_items_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return inlineformset_factory(services_group, services_group_items, form, formset, **kwargs)

def  get_chassis_maintenace_Sitems_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return inlineformset_factory(chassis_maintenance, chassis_maintenance_S, form, formset, **kwargs)

def  get_chassis_maintenace_SGitems_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return inlineformset_factory(chassis_maintenance, chassis_maintenance_SG, form, formset, **kwargs)