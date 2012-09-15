# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'service.service_type'
        db.add_column('main_service', 'service_type',
                      self.gf('django.db.models.fields.CharField')(default='CH', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'service.service_type'
        db.delete_column('main_service', 'service_type')


    models = {
        'main.carburetion_tank': {
            'Meta': {'object_name': 'carburetion_tank'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'})
        },
        'main.carburetion_tank_maintenance': {
            'Meta': {'object_name': 'carburetion_tank_maintenance'},
            'carburetion_tank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.carburetion_tank']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.carburetion_tank_s': {
            'Meta': {'object_name': 'carburetion_tank_S'},
            'carburetion_tank_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.carburetion_tank_maintenance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.service']"})
        },
        'main.carburetion_tank_sg': {
            'Meta': {'object_name': 'carburetion_tank_SG'},
            'carburetion_tank_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.carburetion_tank_maintenance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'services_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.services_group']"})
        },
        'main.chassis': {
            'Meta': {'object_name': 'chassis'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_plates': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'line': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mileage': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'})
        },
        'main.chassis_maintenance': {
            'Meta': {'object_name': 'chassis_maintenance'},
            'chassis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.chassis']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mileage': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'main.chassis_maintenance_s': {
            'Meta': {'object_name': 'chassis_maintenance_S'},
            'chassis_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.chassis_maintenance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.service']"})
        },
        'main.chassis_maintenance_service': {
            'Meta': {'object_name': 'chassis_maintenance_Service'},
            'chassis_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.chassis_maintenance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'main.chassis_maintenance_sg': {
            'Meta': {'object_name': 'chassis_maintenance_SG'},
            'chassis_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.chassis_maintenance']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'services_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.services_group']"})
        },
        'main.garage': {
            'Meta': {'object_name': 'garage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'office_phone': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'main.radio': {
            'Meta': {'object_name': 'radio'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'})
        },
        'main.radio_maintenance': {
            'Meta': {'object_name': 'radio_maintenance'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'radio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.radio']"})
        },
        'main.radio_maintenance_s': {
            'Meta': {'object_name': 'radio_maintenance_S'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'radio_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.radio_maintenance']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.service']"})
        },
        'main.radio_maintenance_sg': {
            'Meta': {'object_name': 'radio_maintenance_SG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'radio_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.radio_maintenance']"}),
            'services_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.services_group']"})
        },
        'main.service': {
            'Meta': {'object_name': 'service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'service_type': ('django.db.models.fields.CharField', [], {'default': "'CH'", 'max_length': '10'})
        },
        'main.services_group': {
            'Meta': {'object_name': 'services_group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'main.services_group_items': {
            'Meta': {'object_name': 'services_group_items'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'services': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.service']"}),
            'services_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.services_group']"})
        },
        'main.storage_tank': {
            'Meta': {'object_name': 'storage_tank'},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'capArt': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'}),
            'water_nominal_cap': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'main.storage_tank_maintenance': {
            'Meta': {'object_name': 'storage_tank_maintenance'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'garage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.garage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'storage_tank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.storage_tank']"})
        },
        'main.storage_tank_maintenance_s': {
            'Meta': {'object_name': 'storage_tank_maintenance_S'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.service']"}),
            'storage_tank_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.storage_tank_maintenance']"})
        },
        'main.storage_tank_maintenance_sg': {
            'Meta': {'object_name': 'storage_tank_maintenance_SG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'services_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.services_group']"}),
            'storage_tank_maintenance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.storage_tank_maintenance']"})
        },
        'main.vehicle': {
            'Meta': {'object_name': 'vehicle'},
            'carburetion_tank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.carburetion_tank']", 'null': 'True', 'blank': 'True'}),
            'chassis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.chassis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'radio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.radio']", 'null': 'True', 'blank': 'True'}),
            'storage_tank': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.storage_tank']", 'null': 'True', 'blank': 'True'}),
            'vehicle_type': ('django.db.models.fields.CharField', [], {'default': "'TR'", 'max_length': '10'})
        }
    }

    complete_apps = ['main']