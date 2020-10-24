from django.contrib import admin
from .models import Role, Function,Candidate,Expert

# Register your models here.
admin.site.register(Role)
admin.site.register(Function)
admin.site.register(Candidate)
admin.site.register(Expert)
