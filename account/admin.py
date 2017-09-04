from django.contrib import admin

# Register your models here.
from .models import Event_reminder

class Event_reminderAdmin(admin.ModelAdmin):
	model = Event_reminder
	list_display = ('event_date','title','description','user')
	
admin.site.register(Event_reminder,Event_reminderAdmin)