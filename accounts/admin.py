from django.contrib import admin

# Register your models here.


from django.apps import apps
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import *
from django.contrib.sessions.models import Session

from django.contrib.admin import ModelAdmin, register
from accounts.models import *

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()

for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(ContentType)
admin.site.unregister(Teacher)
admin.site.unregister(Student)
admin.site.unregister(Guardian)
admin.site.unregister(Employee)
admin.site.unregister(Controller)