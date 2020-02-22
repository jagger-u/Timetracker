from django.shortcuts import render, redirect
from .models import DailyAct, ourDays
from django.http import HttpResponseRedirect, JsonResponse
from datetime import datetime, date 
from . import timetracker_funcs as trs

def home(request):
  timeData = []
  for i in ourDays.objects.all().order_by('-day_date'):
    tagsList = []
    for ii in i.day_tags.all():
      tagsList.append(ii.name)
    print(tagsList)
    timeData.append({'Id':i.id,'Date':i.day_date,'Total':str(i.dayTotal())[:-3],'Tags':tagsList})
  
  context = { 'timeData': timeData, }
  return render(request, 'timetracker/home.html', context)

def insert(request):
  context = { 'dailyAct': DailyAct.objects.all().order_by('-id')[:8], }
  return render(request, 'timetracker/insert.html', context)

def add(request):
  if (request.method == 'POST'):
    #Receiving data
    act_comments = request.POST['comments']
    tag_name = request.POST['tag_name']
    # tag_id = request.POST['tag_id']
    act_name1 = request.POST['act_name1']
    act_name2 = request.POST['act_name2']
    act_name3 = request.POST['act_name3']
    long_string1 = request.POST['long_string1']
    long_string2 = request.POST['long_string2']
    long_string3 = request.POST['long_string3']
    # Time formatting
    tY = int(request.POST['tDate'].split('-')[0])
    tM = int(request.POST['tDate'].split('-')[1])
    tD = int(request.POST['tDate'].split('-')[2])
    act_date = date(tY, tM, tD)
    # Sending to Database
    trs.send_to_database(act_name1, long_string1, act_date, act_comments, tag_name, DailyAct, ourDays)
    trs.send_to_database(act_name2, long_string2, act_date, act_comments, tag_name, DailyAct, ourDays)
    trs.send_to_database(act_name3, long_string3, act_date, act_comments, tag_name, DailyAct, ourDays) 
    return redirect('/insert')
  else:
    return redirect('/insert')

def stats(request):
  return render(request, 'timetracker/statistics.html')

def resultsData(request):
  timeData = []
  for i in ourDays.objects.all().order_by('-day_date'):
    timeData.append({i.day_date[-5:]:(i.dayTotal().seconds/60)})
  return JsonResponse(timeData, safe=False)

def calendar(request):
  return render(request, 'timetracker/calendar.html')

def particles(request):
  return render(request, 'timetracker/particles.html')




































  # def add(request):
#   if (request.method == 'POST'):
#     sthour = int(request.POST['sthour'])
#     stmin = int(request.POST['stmin'])
#     fnhour = int(request.POST['fnhour'])
#     fnmin = int(request.POST['fnmin'])
#     tY = int(datetime.now().year)                         #yeah this is terrible...
#     tM = int(datetime.now().month)
#     tD = int(datetime.now().day)
#     tAct = request.POST['tAct']
#     startTime = str(datetime(tY,tM,tD,sthour,stmin))[:-3]
#     endTime = str(datetime(tY,tM,tD,fnhour,fnmin))[:-3]
#     act = DailyAct(act_name=tAct, start_time=startTime, end_time=endTime)
#     act.save()
#     return redirect('/insert')
#   else:
#     context = {
#       'Activities': DailyAct.objects.all(),
#     }
#   return render(request, 'timetracker/home.html', context)