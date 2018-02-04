from django.contrib import admin

from lighthousedjango.models import Event,User,Calendar


admin.site.register(Event)
admin.site.register(Calendar)
admin.site.register(User)
