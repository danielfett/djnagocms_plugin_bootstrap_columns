from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PlaceholderField
from django.db import models


class BootStrapContainer(CMSPlugin):
    title = models.CharField(max_length=255)
    classes = models.CharField(max_length=255, null=True, blank=True,
                               help_text="""Classes to be applied to this
                               element""", verbose_name="Element Classes")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")

    element_style = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""HTML styles to be applied to
                                     this element""",
                                     verbose_name="Element style")
    is_fluid = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self.title)

    @property
    def get_is_fluid(self):
        print self.is_fluid
        if self.is_fluid is True:
            return "container-fluid"
        else:
            return "container"


class BootstrapRow(CMSPlugin):
    title = models.CharField(max_length=255)
    classes = models.CharField(max_length=255, null=True, blank=True,
                               help_text="""Classes to be applied to this
                               element""", verbose_name="Element Classes")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")

    element_style = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""HTML styles to be applied to
                                     this element""",
                                     verbose_name="Element style")

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self.title)


class BootstrapColumn(CMSPlugin):
    device_count_range = (
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
                                           choices=device_count_range,
                                           help_text="""The column width on
                                           mobile devices (> 768px)""")
    small_device_width = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          help_text="""The column width on
                                          small (tablet) devices (768px - 992px
                                          )""")
    medium_device_width = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           help_text="""The column width on
                                           medium (small screen
                                           computers/laptops) devices (992px -
                                           1200px) """)
    large_device_width = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          help_text="""The column width on
                                          large devices (1200px and over)""")
    element_style = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""HTML styles to be applied to
                                     this element""",
                                     verbose_name="Element style")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")
    element_class = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""classes to be applied to this
                                     element""", verbose_name="Element classes"
                                     )
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
    mobile_device_offset = models.CharField(max_length=255,
                                            choices=device_count_range,
                                            blank=True,
                                            help_text="""The column offset on
                                            mobile devices (> 768px)""")
    small_device_offset = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           blank=True,
                                           help_text="""The column offset on
                                           small (tablet) devices (768px -
                                           992px)""")

    medium_device_offset = models.CharField(max_length=255,
                                            choices=device_count_range,
                                            blank=True,
                                            help_text="""The column offset on
                                            medium (small screen
                                            computers/laptops) devices (992px -
                                            1200px) """)
    large_device_offset = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           blank=True,
                                           help_text="""The column offset on
                                           large devices (1200px and over)""")
    mobile_device_pull = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column pull on
                                          mobile devices (> 768px)""")
    small_device_pull = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column pull on
                                         small (tablet) devices (768px - 992px
                                         )""")
    medium_device_pull = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column pull on
                                          medium (small screen
                                          computers/laptops) devices (992px -
                                          1200px) """)
    large_device_pull = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column pull on
                                         large devices (1200px and over)""")

    mobile_device_push = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column push on
                                          mobile devices (> 768px)""")
    small_device_push = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column push on
                                         small (tablet) devices (768px - 992px
                                         )""")
    medium_device_push = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column push on
                                          medium (small screen
                                          computers/laptops) devices (992px -
                                          1200px) """)
    large_device_push = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column push on
                                         large devices (1200px and over)""")

    content = PlaceholderField('column_placeholder')

    def __unicode__(self):
        return unicode(self.title)

    def __str__(self):
        return unicode(self.title)

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
    def get_mobile_offset(self):
        if self.mobile_device_offset != 0:
            return "col-xs-offset-%s" % self.mobile_device_offset

    @property
    def get_small_offset(self):
        if self.small_device_offset != 0:
            return "col-sm-offset-%s" % self.small_device_offset

    @property
    def get_medium_offset(self):
        if self.medium_device_offset != 0:
            return "col-md-offset-%s" % self.medium_device_offset

    @property
    def get_large_offset(self):
        if self.large_device_offset != 0:
            return "col-lg-offset-%s" % self.large_device_offset

    @property
    def get_mobile_pull(self):
        if self.mobile_device_pull != 0:
            return "col-xs-pull-%s" % self.mobile_device_pull

    @property
    def get_small_pull(self):
        if self.small_device_pull != 0:
            return "col-sm-pull-%s" % self.small_device_pull

    @property
    def get_medium_pull(self):
        if self.medium_device_pull != 0:
            return "col-md-pull-%s" % self.medium_device_pull

    @property
    def get_large_pull(self):
        if self.large_device_pull != 0:
            return "col-lg-pull-%s" % self.large_device_pull

    @property
    def get_mobile_push(self):
        if self.mobile_device_push != 0:
            return "col-xs-push-%s" % self.mobile_device_push

    @property
    def get_small_push(self):
        if self.small_device_push != 0:
            return "col-sm-push-%s" % self.small_device_push

    @property
    def get_medium_push(self):
        if self.medium_device_push != 0:
            return "col-md-push-%s" % self.medium_device_push

    @property
    def get_large_push(self):
        if self.large_device_push != 0:
            return "col-lg-push-%s" % self.large_device_push

    @property
    def is_hidden_on_mobile(self):
        if self.hide_on_mobile:
            return "hidden-xs"

    @property
    def is_hidden_on_small(self):
        if self.hide_on_small:
            return "hidden-sm"

    @property
    def is_hidden_on_medium(self):
        if self.hide_on_medium:
            return "hidden-md"

    @property
    def is_hidden_on_large(self):
        if self.hide_on_large:
            return "hidden-lg"

    @property
    def get_column_widths(self):
        return "%s %s %s %s" % (self.get_mobile_width,
                                self.get_small_width,
                                self.get_medium_width,
                                self.get_large_width)

    @property
    def get_column_pulls(self):
        return "%s %s %s %s" % (self.get_mobile_pull,
                                self.get_small_pull,
                                self.get_medium_pull,
                                self.get_large_pull)

    @property
    def get_column_pushes(self):
        return "%s %s %s %s" % (self.get_mobile_push,
                                self.get_small_push,
                                self.get_medium_push,
                                self.get_large_push)

    @property
    def get_column_offsets(self):
        return "%s %s %s %s" % (self.get_mobile_offset,
                                self.get_small_offset,
                                self.get_medium_offset,
                                self.get_large_offset)

    @property
    def get_column_classes(self):
        return "%s %s %s %s %s" % (self.get_column_widths,
                                   self.get_column_pulls,
                                   self.get_column_pushes,
                                   self.get_column_offsets,
                                   self.element_class)
