from django.contrib import admin

from erma_app.models import UserProfileInfo
from erma_app.models import AccessRecord, Topic, Webpage
# Register your models here.

admin.site.register(UserProfileInfo)

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
