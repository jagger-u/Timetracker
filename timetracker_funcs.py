# This function is need to do the string formatting.
# I have refactored this as much as possible as of 2/2/2020.
# Still, we may need to improve the code. 
from datetime import datetime
from .models import Tag
def send_to_database(act_name, long_string, act_date, act_comments, tag_name, table, ourdays):
  if (long_string):

    # Avoiding duplicate tags
    certainTag, notcreated = Tag.objects.get_or_create(name=tag_name)
    if notcreated:
      Tag(name=tag_name)

    # Avoiding duplicate dates
    certainDay, notcreated = ourdays.objects.get_or_create(day_date=act_date)
    the_id = Tag.objects.get(name=tag_name).id    #guessed, trial and error.... it works anyways
    certainDay.day_tags.add(str(the_id))      #need to be str..... it works anyways
    if notcreated:
      ourdays(day_date=act_date)

    # Get startList, and endList. We are separating the string.
    list = []
    startList = []
    endList = []

    for idx, each in enumerate(long_string.split(',')):
      list.extend(long_string.split(',')[idx].split('-'))

    startlist = list[0:len(list):2]
    endlist = list[1:len(list):2]
    newlist1 = []
    newlist2 = []

    for idx, each in enumerate(startlist):
      newlist1.extend(startlist[idx].split(':'))
    for idx, each in enumerate(endlist):
      newlist2.extend(endlist[idx].split(':'))

    startHours = newlist1[0:len(newlist1):2]
    endHours = newlist2[0:len(newlist2):2]
    startMin = newlist1[1:len(newlist1):2]
    endMin = newlist2[1:len(newlist2):2]

    for idx in range(len(startHours)):
      startList.append(str(datetime(act_date.year,act_date.month,act_date.day,int(startHours[idx]),int(startMin[idx])))[:-3])
      endList.append(str(datetime(act_date.year,act_date.month,act_date.day,int(endHours[idx]),int(endMin[idx])))[:-3])

    # Send each activity data to table
    for idx in range(len(startHours)):
      act = table(act_name=act_name, start_time=startList[idx], end_time=endList[idx], act_date=act_date, act_comments=act_comments)
      act.save()

