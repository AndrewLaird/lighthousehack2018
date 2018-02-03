from django.contrib import admin

from lighthousedjango.models import Event,Calendar,User,Settings

admin.site.register(Event)
admin.site.register(Calendar)
admin.site.register(User)
admin.site.register(Settings)