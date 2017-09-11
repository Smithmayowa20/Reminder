from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Event_reminder
from registration.forms import RegistrationFormUniqueEmail
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import Event_reminderForm, YearForm
from django.utils import timezone
import calendar
import datetime
'''
#Create a plain text calendar
	c= calendar.TextCalendar(calendar.THURSDAY)
    str= c.formatmonth(2015,1,0,0)
    print str

#Create an HTML formatted calendar
	hc = calendar.HTMLCalendar(calendar.THURSDAY)
	str = hc.formatmonth(2015, 1)
	print str
#loop over the days of a month
#zeroes indicate that the day of the week is in a next month or overlapping month
   for i in c.itermonthdays(2015,4):
      print i

#The calendar can give info based on local such a names of days and months (full and abbreviated forms)
	for name in calendar.month_name:
	    print name
	for day in calendar.day_name:
	    print day
#calculate days based on a rule: For instance an audit day on the second Monday of every month
#Figure out what days that would be for each month, we can use the script as shown here
	for month in range(1,13):
	  # It retrieves a list of weeks that represent the month
  mycal = calendar.monthcalendar(2020, month)
	  # The second MONDAY has to be within the first two weeks
	  week1 = mycal[1]
	  week2 = mycal[2]
  if week1[calendar.MONDAY] != 0:
	    auditday = week1[calendar.MONDAY]
  else:
    # if the second MONDAY isn't in the first week, it must be in the second week
	    auditday = week2[calendar.MONDAY]
	  print "%10s %2d" % (calendar.month_name[month], auditday)'''


def get_data(request,year=2017):
	month_dict = {}
	month_begining = calendar.TextCalendar(calendar.SUNDAY)
	for month in range(1,13):
		list1 = [i for i in month_begining.itermonthdays(year,month)]
		event_list = [("{}-{}-{}".format(year,month,i)) for i in month_begining.itermonthdays(year,month) if i != 0]
		#event_list1 = [[("{}-{}-{}".format(year,month,i))] for i in month_begining.itermonthdays(year,month) if i != 0]
		event = Event_reminder.objects.filter(user=request.user, event_date__in=event_list)
		month_dict[("event_{}".format(month))] = [(i.get_month_day_year()) for i in event]
		month_dict[("event_list_{}".format(month))] = event
		days_needed = ((7*6) - len(list1))
		if days_needed > 0 :
			c = [0 for i in range(days_needed)]
			list1 += c
		first_week = list1[:7]
		second_week = list1[7:14]
		third_week = list1[14:21]
		fourth_week = list1[21:28]
		fifth_week = list1[28:35]
		sixth_week = list1[35:]
		days = [day[:2] for day in calendar.day_name]
		list2 = [days,first_week,second_week,third_week,fourth_week,fifth_week,sixth_week]
		month_dict[("month_{}".format(month))] = list2
	month_dict["year"] = year
	return(month_dict)
		
		
@login_required
def home_page(request,year=datetime.datetime.now().year):
	date_year = datetime.datetime.now().year
	date_day = datetime.datetime.now().day
	date_month = datetime.datetime.now().month
	context = get_data(request,int(year))
	context["day"] = date_day
	context["month"] = date_month
	context["standard_year"] = date_year
	form_class = Event_reminderForm
	form_class1 = YearForm
	if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
		form = form_class(request.POST, request.FILES)
		form1 = form_class1(request.POST, request.FILES)
		if form.is_valid():
			thing = form.save(commit=False)
			thing.user = request.user
			thing.create_event()
			return redirect('home_page')
		if form1.is_valid():
			form_year = form1.save(commit=False)
			year = int(form_year.year)
			return redirect('home_page', year=year)
	else:
		form = form_class()
		form1 = form_class1()
		context['form'] = form
		context['form1'] = form1
		return(render(request,'account/home_page.html',context))
	
	
def landing_page(request):
	return (render(request,'account/landing_page.html'))