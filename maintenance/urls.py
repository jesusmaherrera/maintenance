from django.conf.urls import patterns, include, url
from maintenance.main import views
from django.conf import settings
from django.views.generic.simple import direct_to_template
from maintenance.main.forms import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #inlineform set
    (r'^ServicesGroup/New/$', views.services_groupInline_formset),
    (r'^ServicesGroup/(?P<id>\d+)/$', views.services_groupInline_formset),
    (r'^servicesView/$', views.servicesView),
	(r'^$', views.index),
	(r'^detalles_veiculo/(.*)', views.vehicle_details),
	(r'^mantenimientos_chasis/(.*)', views.chassis_maintenanceView),
    (r'^mantenimientos_TanqueAlmacenamiento/(.*)', views.storage_tank_maintenanceView),
    (r'^mantenimientos_TanqueCarburacion/(.*)', views.carburetion_tank_maintenanceView),
    (r'^nuevoVehiculo/', views.new_vehicleView),
    (r'^Chasis/', views.chassis_manageView),
    (r'^MantenimientoChasis/new/$', views.chassis_maintenance_manageView, {}, 'article_new'),
    (r'^MantenimientoChasis/edit/(?P<id>\d+)/$', views.chassis_maintenance_manageView, {}, 'article_edit'),
    (r'^Radio/new/$', views.radio_manageView, {}, 'radio_new'),
    (r'^Radio/edit/(?P<id>\d+)/$', views.radio_manageView, {}, 'radio_edit'),
    (r'^Service/new/$', views.service_manageView, {}, 'service_new'),
    (r'^Service/edit/(?P<id>\d+)/$', views.service_manageView, {}, 'service_edit'),
    (r'^TanqueCarburacion/new/$', views.carburetion_tank_manageView, {}, 'carburetion_tank_new'),
    (r'^TanqueCarburacion/edit/(?P<id>\d+)/$', views.carburetion_tank_manageView, {}, 'carburetion_tank_edit'),
    (r'^TanqueAlmacenamiento/new/$', views.storage_tank_manageView, {}, 'storage_tank_new'),
    (r'^TanqueAlmacenamiento/edit/(?P<id>\d+)/$', views.storage_tank_manageView, {}, 'storage_tank_edit'),
    (r'^Chasis/new/$', views.chassis_manageView, {}, 'chassis_new'),
    (r'^Chasis/edit/(?P<id>\d+)/$', views.chassis_manageView, {}, 'chassis_edit'),
    (r'^ChasisMaintenanceS/delete/(?P<id>\d+)/$', views.delete_chassis_maintenanceS, {}, 'delete_chassis_maintenanceS'),
    (r'^Vehicle/delete/(?P<id>\d+)/$', views.delete_vehicle, {}, 'vehicle_delete'),
    (r'^ChassisMaintenance/delete/(?P<id>\d+)/$', views.delete_chassis_maintenance, {}, 'chassis_maintenance_delete'),
    (r'^FormSet/(?P<id>\d+)/(?P<id_mant>\d+)/$', views.chassis_maintenance_manageView, {}, 'chassis_maintenance_manage'),
    (r'^ChasisMaintenenceFS/(?P<object_id>\d+)/$', views.chassis_maintenance_manageFormSet,{},'manage_chassismaintenance2'),
    (r'^ChasisMaintenenceFS/new/$', views.chassis_maintenance_manageFormSet,{},'manage_chassismaintenance2'),
    (r'^carburetionTankMaintenanceFS/new/$', views.carburetion_tank_maintenance_MFS,{},'carburetion_tank_maintenance_MFS'),
    (r'^carburetionTankMaintenanceFS/(?P<object_id>\d+)/$', views.carburetion_tank_maintenance_MFS,{},'carburetion_tank_maintenance_MFS'),
    (r'^storageTankMaintenanceFS/new/$', views.storage_tank_maintenance_MFS,{},'storage_tank_maintenance_MFS'),
    (r'^storageTankMaintenanceFS/(?P<object_id>\d+)/$', views.storage_tank_maintenance_MFS,{},'storage_tank_maintenance_MFS'),
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
