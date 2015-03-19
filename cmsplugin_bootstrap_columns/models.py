from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField
from django.db import models


class BootstrapRow(CMSPlugin):
    title = models.CharField(max_length=255)
    classes = models.CharField(max_length=255, null=True, blank=True,
                               help_text="""Classes to be applied to this
                               element""", verbose_name="Element Classes")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")

        def __unicode__(self):
        return self.title


class BootstrapColumn(CMSPlugin):
    device_width_range = (
        ('0', 'Not Set',),
        ('1', '1/12',),
        ('2', '2/12',),
        ('3', '3/12',),
        ('4', '4/12',),
        ('5', '5/12',),
        ('6', '6/12',),
        ('7', '7/12',),
        ('8', '8/12',),
        ('9', '9/12',),
        ('10', '10/12',),
        ('11', '11/12',),
        ('12', '12/12',),
    )

    title = models.CharField(max_length=255)
    mobile_device_width = models.CharField(max_length=255,
                                           choices=device_width_range,
                                           help_text="""The column width on
                                           mobile devices (> 768px)""")
    small_device_width = models.CharField(max_length=255,
                                          choices=device_width_range,
                                          help_text="""The column width on
                                          small (tablet) devices (768px - 992px
                                          )""")
    medium_device_width = models.CharField(max_length=255,
                                           choices=device_width_range,
                                           help_text="""The column width on
                                           medium (small screen
                                           computers/laptops) devices (992px -
                                           1200px) """)
    large_device_width = models.CharField(max_length=255,
                                          choices=device_width_range,
                                          help_text="""The column width on
                                          large devices (1200px and over)""")
    hide_on_mobile = models.BooleanField(help_text="""If selected, this
                                                 item will not display on
                                                 mobile devices (> 768px)""")
    hide_on_small = models.BooleanField(help_text="""If selected,
                                                  this item will not display
                                                  on small devices (768px -
                                                  992px)""")
    hide_on_medium = models.BooleanField(help_text="""If selected,
                                                  this item will not display
                                                  on medium devices (992px -
                                                  1200px)""")
    hide_on_large = models.BooleanField(help_text="""If selected,
                                                  this item will not display
                                                  on large devices (1200px and
                                                  over)""")
    content = PlaceholderField('column_placeholder')

    def __unicode__(self):
        return self.title

    @property
    def get_mobile_width(self):
        if self.mobile_device_width != 0:
            return "col-xs-%s" % self.mobile_device_width

    @property
    def get_small_width(self):
        if self.small_device_width != 0:
            return "col-sm-%s" % self.small_device_width

    @property
    def get_medium_width(self):
        if self.medium_device_width != 0:
            return "col-md-%s" % self.medium_device_width

    @property
    def get_large_width(self):
        if self.large_device_width != 0:
            return "col-lg-%s" % self.large_device_width

    @property
    def is_hidden_on_mobile(self):
        if self.hide_on_mobile:
            return "hidden-xs"

    @property
    def is_hidden_on_small(self):
        if self.hide_on_mobile:
            return "hidden-sm"

    @property
    def is_hidden_on_medium(self):
        if self.hide_on_mobile:
            return "hidden-md"

    @property
    def is_hidden_on_large(self):
        if self.hide_on_mobile:
            return "hidden-lg"

    @property
    def get_column_classes(self):
        return "%s %s %s %s %s %s %s %s" % (self.get_mobile_width,
                                            self.get_small_width,
                                            self.get_medium_width,
                                            self.get_large_width,
                                            self.is_hidden_on_mobile,
                                            self.is_hidden_on_small,
                                            self.is_hidden_on_medium,
                                            self.is_hidden_on_large)
