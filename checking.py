# from django.db import models
# from .models import DailyAct
from datetime import datetime, date, timedelta 
list = [{'Date':'2020-10-12','Total':'200','Tags':['Normal','Busy']}, {'Date':'2020-10-15','Total':'0','Tags':['Unknown']},{'Date':'2020-10-15','Total':'0','Tags':'null'}]
# print("List: {}\nDict1: {}, Dict2: {}".format(list, dict1, dict2))

for i, dict in enumerate(list):
  print(" ")
  print(dict['Date'])
  # print(k['Date'])