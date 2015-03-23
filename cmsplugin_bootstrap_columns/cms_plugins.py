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
