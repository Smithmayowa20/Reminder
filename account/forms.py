from django import forms 
from .models import Event_reminder,Year

year_choices = [str(2000 + int(i)) for i in range(1,100)]
YEAR_CHOICES = tuple(year_choices)
class Event_reminderForm(forms.ModelForm):
	event_date = forms.DateField(widget = forms.SelectDateWidget(years = YEAR_CHOICES))
	class Meta:
		model = Event_reminder
		fields = ('title','event_date','description')
		
class YearForm(forms.ModelForm):
	class Meta:
		model = Year
		fields = ('year',)