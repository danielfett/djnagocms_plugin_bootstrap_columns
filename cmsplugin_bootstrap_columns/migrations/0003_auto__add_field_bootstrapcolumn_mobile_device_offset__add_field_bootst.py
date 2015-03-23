# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BootstrapColumn.mobile_device_offset'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'mobile_device_offset',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.small_device_offset'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'small_device_offset',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.medium_device_offset'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'medium_device_offset',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.large_device_offset'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'large_device_offset',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.mobile_device_pull'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'mobile_device_pull',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.small_device_pull'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'small_device_pull',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.medium_device_pull'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'medium_device_pull',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.large_device_pull'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'large_device_pull',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.mobile_device_push'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'mobile_device_push',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.small_device_push'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'small_device_push',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.medium_device_push'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'medium_device_push',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'BootstrapColumn.large_device_push'
        db.add_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'large_device_push',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BootstrapColumn.mobile_device_offset'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'mobile_device_offset')

        # Deleting field 'BootstrapColumn.small_device_offset'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'small_device_offset')

        # Deleting field 'BootstrapColumn.medium_device_offset'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'medium_device_offset')

        # Deleting field 'BootstrapColumn.large_device_offset'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'large_device_offset')

        # Deleting field 'BootstrapColumn.mobile_device_pull'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'mobile_device_pull')

        # Deleting field 'BootstrapColumn.small_device_pull'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'small_device_pull')

        # Deleting field 'BootstrapColumn.medium_device_pull'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'medium_device_pull')

        # Deleting field 'BootstrapColumn.large_device_pull'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'large_device_pull')

        # Deleting field 'BootstrapColumn.mobile_device_push'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'mobile_device_push')

        # Deleting field 'BootstrapColumn.small_device_push'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'small_device_push')

        # Deleting field 'BootstrapColumn.medium_device_push'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'medium_device_push')

        # Deleting field 'BootstrapColumn.large_device_push'
        db.delete_column(u'cmsplugin_bootstrap_columns_bootstrapcolumn', 'large_device_push')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'cmsplugin_bootstrap_columns.bootstrapcolumn': {
            'Meta': {'object_name': 'BootstrapColumn', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'element_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'element_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hide_on_large': ('django.db.models.fields.BooleanField', [], {}),
            'hide_on_medium': ('django.db.models.fields.BooleanField', [], {}),
            'hide_on_mobile': ('django.db.models.fields.BooleanField', [], {}),
            'hide_on_small': ('django.db.models.fields.BooleanField', [], {}),
            'large_device_offset': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'large_device_pull': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'large_device_push': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'large_device_width': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'medium_device_offset': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'medium_device_pull': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'medium_device_push': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'medium_device_width': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobile_device_offset': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobile_device_pull': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobile_device_push': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobile_device_width': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'small_device_offset': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'small_device_pull': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'small_device_push': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'small_device_width': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsplugin_bootstrap_columns.bootstrapcontainer': {
            'Meta': {'object_name': 'BootStrapContainer', '_ormbases': ['cms.CMSPlugin']},
            'classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'element_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'element_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_fluid': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cmsplugin_bootstrap_columns.bootstraprow': {
            'Meta': {'object_name': 'BootstrapRow', '_ormbases': ['cms.CMSPlugin']},
            'classes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'element_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'element_style': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cmsplugin_bootstrap_columns']