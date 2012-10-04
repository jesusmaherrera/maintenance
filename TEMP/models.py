#encoding:utf-8
from django.db import models

class chassis(models.Model):
    name = models.CharField('Serie',max_length=50)
    brand = models.CharField('Marca',max_length=30, blank=True, null=True)
    line = models.CharField('Linea',max_length=30, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    model = models.CharField(max_length=4, blank=True, null=True)
    license_plates = models.CharField(max_length=15, blank=True, null=True)
    mileage = models.CharField(max_length=10, blank=True, null=True)
    TYPE_CHOICES = (
        ('N', 'NORMAL'),
        ('D', 'DESHABILITADO'),
    )
    state = models.CharField(max_length=10, choices=TYPE_CHOICES,
                                      default='N')
    
    def __unicode__(self):
        return self.name

class storage_tank(models.Model):
    series = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=4, blank=True, null=True)
    water_nominal_cap = models.CharField(max_length=10, blank=True, null=True)
    capArt = models.CharField(max_length=10, blank=True, null=True)
    content = models.CharField(max_length=30, blank=True, null=True)
    TYPE_CHOICES = (
        ('N', 'NORMAL'),
        ('D', 'DESHABILITADO'),
    )
    state = models.CharField(max_length=10, choices=TYPE_CHOICES,
                                      default='N')

    def __unicode__(self):
        return self.series

class carburetion_tank(models.Model):
    series = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=4, blank=True, null=True)
    capacity = models.CharField(max_length=10, blank=True, null=True)
    TYPE_CHOICES = (
        ('N', 'NORMAL'),
        ('D', 'DESHABILITADO'),
    )
    state = models.CharField(max_length=10, choices=TYPE_CHOICES,
                                      default='N')
    def __unicode__(self):
        return self.series

class radio(models.Model):
    series = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, blank=True, null=True)
    model = models.CharField(max_length=10, blank=True, null=True)
    TYPE_CHOICES = (
        ('N', 'NORMAL'),
        ('D', 'DESHABILITADO'),
    )
    state = models.CharField(max_length=10, choices=TYPE_CHOICES,
                                      default='N')

    def __unicode__(self):
        return self.series

# def get_sentinel_chassis():
#     return chassis.objects.get_or_create(name='deleted', brand='default')[0]

class vehicle(models.Model):
    name = models.CharField('Numero Econimico', max_length=50)
    #chassis = models.ForeignKey(chassis, on_delete=models.SET(get_sentinel_chassis))
    chassis = models.ForeignKey(chassis, on_delete=models.SET_NULL, blank=True, null=True)
    storage_tank = models.ForeignKey(storage_tank, on_delete=models.SET_NULL, blank=True, null=True)
    carburetion_tank = models.ForeignKey(carburetion_tank, on_delete=models.SET_NULL, blank=True, null=True)
    radio = models.ForeignKey(radio, on_delete=models.SET_NULL, blank=True, null=True)
    
    VEHICLE_TYPE_CHOICES = (
        ('PI', 'PIPA'),
        ('TR', 'TROCA'),
    )
    vehicle_type = models.CharField('Tipo',max_length=10, choices=VEHICLE_TYPE_CHOICES,
                                      default='TR')
    image = models.ImageField(blank=True, null=True, upload_to='vehicles', verbose_name='Imágen')

    def __unicode__(self):
        return self.name

#----------------Mantenimientos-----------------------------------
class garage(models.Model):
    name = models.CharField(max_length=60)
    office_phone = models.CharField(max_length=60, blank=True, null=True)

    def __unicode__(self):
        return self.name

class radio_maintenance(models.Model):
    date = models.DateTimeField()
    garage = models.ForeignKey(garage, on_delete=models.SET_NULL, blank=True, null=True)
    radio = models.ForeignKey(radio, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=150)
    
    def __unicode__(self):
        return u'%s %s'% (self.date, self.garage)

class chassis_maintenance(models.Model):
    date = models.DateTimeField()
    garage = models.ForeignKey(garage, on_delete=models.SET_NULL, blank=True, null=True)
    chassis = models.ForeignKey(chassis, on_delete=models.SET_NULL, blank=True, null=True)
    mileage = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s'% (self.date, self.garage)

class storage_tank_maintenance(models.Model):
    date = models.DateTimeField()
    garage = models.ForeignKey(garage, on_delete=models.SET_NULL, blank=True, null=True)
    storage_tank = models.ForeignKey(storage_tank, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s'% (self.date, self.garage)

class carburetion_tank_maintenance(models.Model):
    date = models.DateTimeField()
    garage = models.ForeignKey(garage, on_delete=models.SET_NULL, blank=True, null=True)
    carburetion_tank = models.ForeignKey(carburetion_tank, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s'% (self.date, self.garage)        

#--------------------- Servicios ----------------------------
class service(models.Model):
    name = models.CharField(max_length=60)
    
    SERVICE_TYPE_CHOICES = (
        ('CH', 'CHASIS'),
        ('TC', 'TANQUE DE CARBURACION'),
        ('TA', 'TANQUE DE ALMACENAMIENTO'),
        ('R', 'RADIO'),
    )

    service_type = models.CharField('Tipo',max_length=10, choices=SERVICE_TYPE_CHOICES,
                                      default='CH')
    def __unicode__(self):
        return self.name

class services_group(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class services_group_items(models.Model):
    services = models.ForeignKey(service)
    services_group = models.ForeignKey(services_group)

    def __unicode__(self):
        return unicode(self.id)

#------------- Servicios en Mantenimientos -----------------
#CHASSIS
class chassis_maintenance_S(models.Model):
    chassis_maintenance = models.ForeignKey(chassis_maintenance)
    service = models.ForeignKey(service, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return u'%s'% (self.id)

class chassis_maintenance_Service(models.Model):
    chassis_maintenance = models.ForeignKey(chassis_maintenance)
    service = models.CharField(max_length=150)

    def __unicode__(self):
        return u'%s'% (self.id)

class chassis_maintenance_SG(models.Model):
    chassis_maintenance = models.ForeignKey(chassis_maintenance)
    services_group = models.ForeignKey(services_group, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)
#RADIO
class radio_maintenance_S(models.Model):
    radio_maintenance = models.ForeignKey(radio_maintenance)
    service = models.ForeignKey(service, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return u'%s'% (self.id)

class radio_maintenance_SG(models.Model):
    radio_maintenance = models.ForeignKey(radio_maintenance)
    services_group = models.ForeignKey(services_group, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

#STRORAGE TANK
class storage_tank_maintenance_S(models.Model):
    storage_tank_maintenance = models.ForeignKey(storage_tank_maintenance)
    service = models.ForeignKey(service, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

class storage_tank_maintenance_SG(models.Model):
    storage_tank_maintenance = models.ForeignKey(storage_tank_maintenance)
    services_group = models.ForeignKey(services_group, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

#CARBURETION TANK
class carburetion_tank_S(models.Model):
    carburetion_tank_maintenance = models.ForeignKey(carburetion_tank_maintenance)
    service = models.ForeignKey(service, on_delete=models.SET_NULL, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

class carburetion_tank_SG(models.Model):
    carburetion_tank_maintenance = models.ForeignKey(carburetion_tank_maintenance)
    services_group = models.ForeignKey(services_group, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.id)