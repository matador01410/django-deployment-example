from django.contrib import admin
from first_app.models import Webpage
from first_app.models import AccessRecord
from first_app.models import Topic
from first_app.models import User

# Register your models here.

admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(User)

