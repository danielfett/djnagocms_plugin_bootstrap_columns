from django.contrib import admin


class BootstrapColumnPluginAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title','element_style', 'element_id',
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
            'fields': ('mobile_device_pull', 'small_device_offset',
                       'medium_device_pull', 'large_device_offset')
        }),
        ('Viewport Push', {
            'fields': ('mobile_device_push', 'small_device_offset',
                       'medium_device_push', 'large_device_offset')
        }),
    )
