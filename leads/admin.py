from django.contrib import admin

from .models import User, Agent, Lead


admin.site.register(Agent)
admin.site.register(Lead)
