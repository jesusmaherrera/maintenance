from django.conf.urls import patterns, include, url
from maintenance.main import views
from django.conf import settings
from django.views.generic.simple import direct_to_template
from maintenance.main.forms import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #LOGIN
    url(r'^login/$',views.ingresar),
    url(r'^logout/$', views.logoutUser),
    # SERVICES GROUPS
    (r'^ServicesGroup/New/$', views.services_groupInline_formset),
    (r'^ServicesGroup/(?P<id>\d+)/$', views.services_groupInline_formset),
    (r'^ServicesGroup/Delete/(?P<id>\d+)/$', views.delete_services_group),
    #SERVICES
    (r'^servicesView/$', views.servicesView),
    (r'^Service/new/$', views.service_manageView, {}, 'service_new'),
    (r'^Service/edit/(?P<id>\d+)/$', views.service_manageView, {}, 'service_edit'),
    (r'^Service/Delete/(?P<id>\d+)/$', views.delete_service),
    #GARAGES
    (r'^Garages/$', views.garagesView),
    (r'^Garage/New/$', views.garage_manageView),
    (r'^Garage/(?P<id>\d+)/$', views.garage_manageView),
    #(r'^Garage/Delete/(?P<id>\d+)/$', views.garage_manageView),
    #MANTENIMIENTOS A CHASIS
    (r'^Chassises/$', views.chassisesView),
    (r'^Chassis/(?P<id>\d+)/$', views.chassis_manageView),
    (r'^Chassis/New/$', views.chassis_manageView),
    (r'^mantenimientos_chasis/(.*)', views.chassis_maintenanceView),
    (r'^ChassisMaintenance/New/$', views.chassis_maintenace_Inline_formset),
    (r'^ChassisMaintenance/(?P<id>\d+)/$', views.chassis_maintenace_Inline_formset),
    (r'^ChassisMaintenance/delete/(?P<id>\d+)/$', views.delete_chassis_maintenance, {}, 'chassis_maintenance_delete'),
    #MANTENIMIENTOS A TANQUE DE CARBURACION
    (r'^mantenimientos_TanqueCarburacion/(.*)', views.carburetion_tank_maintenanceView),
    (r'^CarburetionTankMaintenace/New/$', views.carburetion_tank_maintenance_Inline_formset),
    (r'^CarburetionTankMaintenace/(?P<id>\d+)/$', views.carburetion_tank_maintenance_Inline_formset),
    (r'^CarburetionTankMaintenace/Delete/(?P<id>\d+)/$', views.delete_carburetion_tank_maintenance),

    #MANTENIMIENTOS A TANQUE DE ALMACENAMIENTO
    (r'^mantenimientos_TanqueAlmacenamiento/(.*)', views.storage_tank_maintenanceView),
    (r'^StorageTankMaintenace/New/$', views.storage_tank_maintenance_Inline_formset),
    (r'^StorageTankMaintenace/(?P<id>\d+)/$', views.storage_tank_maintenance_Inline_formset),
    (r'^StorageTankMaintenace/Delete/(?P<id>\d+)/$', views.delete_storage_maintenance),

    
	(r'^$', views.index),
	(r'^detalles_veiculo/(.*)', views.vehicle_details),
    (r'^nuevoVehiculo/', views.new_vehicleView),
    
    (r'^Radio/new/$', views.radio_manageView, {}, 'radio_new'),
    (r'^Radio/edit/(?P<id>\d+)/$', views.radio_manageView, {}, 'radio_edit'),
    (r'^TanqueCarburacion/new/$', views.carburetion_tank_manageView, {}, 'carburetion_tank_new'),
    (r'^TanqueCarburacion/edit/(?P<id>\d+)/$', views.carburetion_tank_manageView, {}, 'carburetion_tank_edit'),
    (r'^TanqueAlmacenamiento/new/$', views.storage_tank_manageView, {}, 'storage_tank_new'),
    (r'^TanqueAlmacenamiento/edit/(?P<id>\d+)/$', views.storage_tank_manageView, {}, 'storage_tank_edit'),
    (r'^Chasis/new/$', views.chassis_manageView, {}, 'chassis_new'),
    (r'^Chasis/edit/(?P<id>\d+)/$', views.chassis_manageView, {}, 'chassis_edit'),
    (r'^ChasisMaintenanceS/delete/(?P<id>\d+)/$', views.delete_chassis_maintenanceS, {}, 'delete_chassis_maintenanceS'),
    (r'^Vehicle/delete/(?P<id>\d+)/$', views.delete_vehicle, {}, 'vehicle_delete'),
    (r'^ServicesGroup/(?P<id>\d+)/$', views.service_group_inlineView ,{},'Service_group_inlineView'),
    
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
    # Examples:
    # url(r'^$', 'maintenance.views.home', name='home'),
    # url(r'^maintenance/', include('maintenance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
