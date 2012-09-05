from django.conf.urls import patterns, include, url
from maintenance.main import views
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
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
    (r'^TanqueCarburacion/new/$', views.carburetion_tank_manageView, {}, 'carburetion_tank_new'),
    (r'^TanqueCarburacion/edit/(?P<id>\d+)/$', views.carburetion_tank_manageView, {}, 'carburetion_tank_edit'),
    (r'^TanqueAlmacenamiento/new/$', views.storage_tank_manageView, {}, 'storage_tank_new'),
    (r'^TanqueAlmacenamiento/edit/(?P<id>\d+)/$', views.storage_tank_manageView, {}, 'storage_tank_edit'),
    (r'^Chasis/new/$', views.chassis_manageView, {}, 'chassis_new'),
    (r'^Chasis/edit/(?P<id>\d+)/$', views.chassis_manageView, {}, 'chassis_edit'),
    (r'^Vehicle/delete/(?P<id>\d+)/$', views.delete_vehicle, {}, 'vehicle_delete'),
    (r'^ChassisMaintenance/delete/(?P<id>\d+)/$', views.delete_chassis_maintenance, {}, 'chassis_maintenance_delete'),
    (r'^FormSet/(?P<id>\d+)/(?P<id_mant>\d+)/$', views.chassis_maintenance_manageView, {}, 'chassis_maintenance_manage'),
    (r'^ChasisMaintenenceFS/(?P<object_id>\d+)/$', views.chassis_maintenance_manageFormSet,{},'manage_chassismaintenance2'),
    (r'^ChasisMaintenenceFS/new/$', views.chassis_maintenance_manageFormSet,{},'manage_chassismaintenance2'),
    # (r'^chassis_maintenance/add/$', views.chassis_services_ManageView, {}, 'chassis_maintenance_add'),
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
