# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'chassis'
        db.create_table('main_chassis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('line', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('license_plates', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('mileage', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('state', self.gf('django.db.models.fields.CharField')(default='N', max_length=10)),
        ))
        db.send_create_signal('main', ['chassis'])

        # Adding model 'storage_tank'
        db.create_table('main_storage_tank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('water_nominal_cap', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('capArt', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(default='N', max_length=10)),
        ))
        db.send_create_signal('main', ['storage_tank'])

        # Adding model 'carburetion_tank'
        db.create_table('main_carburetion_tank', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('capacity', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('state', self.gf('django.db.models.fields.CharField')(default='N', max_length=10)),
        ))
        db.send_create_signal('main', ['carburetion_tank'])

        # Adding model 'radio'
        db.create_table('main_radio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('state', self.gf('django.db.models.fields.CharField')(default='N', max_length=10)),
        ))
        db.send_create_signal('main', ['radio'])

        # Adding model 'vehicle'
        db.create_table('main_vehicle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('chassis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.chassis'])),
            ('storage_tank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.storage_tank'], null=True, blank=True)),
            ('carburetion_tank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.carburetion_tank'], null=True, blank=True)),
            ('radio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.radio'], null=True, blank=True)),
            ('vehicle_type', self.gf('django.db.models.fields.CharField')(default='TR', max_length=10)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['vehicle'])

        # Adding model 'garage'
        db.create_table('main_garage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('office_phone', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('main', ['garage'])

        # Adding model 'radio_maintenance'
        db.create_table('main_radio_maintenance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.garage'])),
            ('radio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.radio'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('main', ['radio_maintenance'])

        # Adding model 'chassis_maintenance'
        db.create_table('main_chassis_maintenance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.garage'])),
            ('chassis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.chassis'])),
            ('mileage', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('main', ['chassis_maintenance'])

        # Adding model 'storage_tank_maintenance'
        db.create_table('main_storage_tank_maintenance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.garage'])),
            ('storage_tank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.storage_tank'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('main', ['storage_tank_maintenance'])

        # Adding model 'carburetion_tank_maintenance'
        db.create_table('main_carburetion_tank_maintenance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('garage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.garage'])),
            ('carburetion_tank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.carburetion_tank'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('main', ['carburetion_tank_maintenance'])

        # Adding model 'service'
        db.create_table('main_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('shrubberies', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['service'])

        # Adding model 'services_group'
        db.create_table('main_services_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('main', ['services_group'])

        # Adding model 'services_group_items'
        db.create_table('main_services_group_items', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('services', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.service'])),
            ('services_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.services_group'])),
        ))
        db.send_create_signal('main', ['services_group_items'])

        # Adding model 'chassis_maintenance_S'
        db.create_table('main_chassis_maintenance_s', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chassis_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.chassis_maintenance'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.service'])),
        ))
        db.send_create_signal('main', ['chassis_maintenance_S'])

        # Adding model 'chassis_maintenance_Service'
        db.create_table('main_chassis_maintenance_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chassis_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.chassis_maintenance'])),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('main', ['chassis_maintenance_Service'])

        # Adding model 'chassis_maintenance_SG'
        db.create_table('main_chassis_maintenance_sg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chassis_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.chassis_maintenance'])),
            ('services_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.services_group'])),
        ))
        db.send_create_signal('main', ['chassis_maintenance_SG'])

        # Adding model 'radio_maintenance_S'
        db.create_table('main_radio_maintenance_s', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('radio_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.radio_maintenance'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.service'])),
        ))
        db.send_create_signal('main', ['radio_maintenance_S'])

        # Adding model 'radio_maintenance_SG'
        db.create_table('main_radio_maintenance_sg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('radio_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.radio_maintenance'])),
            ('services_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.services_group'])),
        ))
        db.send_create_signal('main', ['radio_maintenance_SG'])

        # Adding model 'storage_tank_maintenance_S'
        db.create_table('main_storage_tank_maintenance_s', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage_tank_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.storage_tank_maintenance'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.service'])),
        ))
        db.send_create_signal('main', ['storage_tank_maintenance_S'])

        # Adding model 'storage_tank_maintenance_SG'
        db.create_table('main_storage_tank_maintenance_sg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('storage_tank_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.storage_tank_maintenance'])),
            ('services_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.services_group'])),
        ))
        db.send_create_signal('main', ['storage_tank_maintenance_SG'])

        # Adding model 'carburetion_tank_S'
        db.create_table('main_carburetion_tank_s', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carburetion_tank_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.carburetion_tank_maintenance'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.service'])),
        ))
        db.send_create_signal('main', ['carburetion_tank_S'])

        # Adding model 'carburetion_tank_SG'
        db.create_table('main_carburetion_tank_sg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('carburetion_tank_maintenance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.carburetion_tank_maintenance'])),
            ('services_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.services_group'])),
        ))
        db.send_create_signal('main', ['carburetion_tank_SG'])


    def backwards(self, orm):
        # Deleting model 'chassis'
        db.delete_table('main_chassis')

        # Deleting model 'storage_tank'
        db.delete_table('main_storage_tank')

        # Deleting model 'carburetion_tank'
        db.delete_table('main_carburetion_tank')

        # Deleting model 'radio'
        db.delete_table('main_radio')

        # Deleting model 'vehicle'
        db.delete_table('main_vehicle')

        # Deleting model 'garage'
        db.delete_table('main_garage')

        # Deleting model 'radio_maintenance'
        db.delete_table('main_radio_maintenance')

        # Deleting model 'chassis_maintenance'
        db.delete_table('main_chassis_maintenance')

        # Deleting model 'storage_tank_maintenance'
        db.delete_table('main_storage_tank_maintenance')

        # Deleting model 'carburetion_tank_maintenance'
        db.delete_table('main_carburetion_tank_maintenance')

        # Deleting model 'service'
        db.delete_table('main_service')

        # Deleting model 'services_group'
        db.delete_table('main_services_group')

        # Deleting model 'services_group_items'
        db.delete_table('main_services_group_items')

        # Deleting model 'chassis_maintenance_S'
        db.delete_table('main_chassis_maintenance_s')

        # Deleting model 'chassis_maintenance_Service'
        db.delete_table('main_chassis_maintenance_service')

        # Deleting model 'chassis_maintenance_SG'
        db.delete_table('main_chassis_maintenance_sg')

        # Deleting model 'radio_maintenance_S'
        db.delete_table('main_radio_maintenance_s')

        # Deleting model 'radio_maintenance_SG'
        db.delete_table('main_radio_maintenance_sg')

        # Deleting model 'storage_tank_maintenance_S'
        db.delete_table('main_storage_tank_maintenance_s')

        # Deleting model 'storage_tank_maintenance_SG'
        db.delete_table('main_storage_tank_maintenance_sg')

        # Deleting model 'carburetion_tank_S'
        db.delete_table('main_carburetion_tank_s')

        # Deleting model 'carburetion_tank_SG'
        db.delete_table('main_carburetion_tank_sg')


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
            'shrubberies': ('django.db.models.fields.IntegerField', [], {})
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