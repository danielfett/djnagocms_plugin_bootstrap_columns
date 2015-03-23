from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import BootStrapContainer
from .models import BootstrapRow
from .models import BootstrapColumn


class BootStrapContainerPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['BootstrapRowPlugin']
    model = BootStrapContainer
    module = "Bootstrap"
    name = "Bootstrap Container"
    render_template = "cmsplugin_bootstrap_columns/container.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(BootStrapContainerPlugin)


class BootstrapRowPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['BootstrapColumnPlugin']
    model = BootstrapRow
    module = "Bootstrap"
    name = "Bootstrap Row"
    render_template = "cmsplugin_bootstrap_columns/row.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(BootstrapRowPlugin)


class BootstrapColumnPlugin(CMSPluginBase):
    allow_children = True
    fieldsets = (
        (None, {
            'fields': ('title', 'element_style', 'element_id',
                       'mobile_device_width', 'small_device_width',
                       'medium_device_width', 'large_device_width')
        }),
        ('Hide on Viewport Size ', {
            'fields': ('hide_on_mobile', 'hide_on_small', 'hide_on_medium',
                       'hide_on_large')
        }),
        ('Viewport Offset', {
            'fields': ('mobile_device_offset', 'small_device_offset',
                       'medium_device_offset', 'large_device_offset')
        }),
        ('Viewport Pull', {
            'fields': ('mobile_device_pull', 'small_device_pull',
                       'medium_device_pull', 'large_device_pull')
        }),
        ('Viewport Push', {
            'fields': ('mobile_device_push', 'small_device_push',
                       'medium_device_push', 'large_device_push')
        }),
    )
    model = BootstrapColumn
    module = "Bootstrap"
    name = "Bootstrap Column"
    render_template = "cmsplugin_bootstrap_columns/column.html"
    require_parent = True
    parent_classes = ['BootstrapRowPlugin', 'BootStrapColumnPlugin']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['placeholder'] = placeholder
        return context

plugin_pool.register_plugin(BootstrapColumnPlugin)
