from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Event_reminder(models.Model):
	event_date = models.DateField(help_text="month/day/year",
		blank=True,null=True)
	title = models.CharField(max_length = 32,
		blank=True,null=True)
	description = models.TextField(
		blank=True,null=True)
	user = models.ForeignKey(User,
		blank=True,null=True)
	created_date = models.DateTimeField(
		default=timezone.now)
	updated_date = models.DateTimeField(
		blank=True,null=True)
		
	def str(self):
		return self.title
		
	def create_event(self):
		self.save()
		self.updated_date = timezone.now()
		
	def get_month_day_year(self):
		datetime = str(self.event_date)
		year_month_day = datetime.split("-")
		year = int(year_month_day[0])
		month = int(year_month_day[1])
		day = int(year_month_day[2])
		return (day)
		