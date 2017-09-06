from django.forms import ModelForm
from .models import Event_reminder

class Event_reminderForm(ModelForm):
	class Meta:
		model = Event_reminder
		fields = ('title','event_date','description')