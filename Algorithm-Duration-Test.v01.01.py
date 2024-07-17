# -*- coding: utf-8 -*-
"""
WHAT
    testing the algorithm

@author: dasco
"""

from datetime import datetime, date, timedelta


# static inputs
now_nrHoursInFullDay = 8.0
now_workTime = { 
                'Monday':  {'startTime': '08:00', 'endTime': '17:00'},
                'Tuesday': {'startTime': '06:00', 'endTime': '12:00'},
                'Friday':  {'startTime': '10:00', 'endTime': '18:00'},
              }



# input from dt
dt_start = datetime(2024, 7, 15, 9, 10, 0) #, tzinfo=zoneinfo.Zoneinfo(key='UTC'))
dt_end = datetime(2024, 7, 25, 10, 0, 0)



# .......................................................
# +++START CALC

# time of the start of the first day and time of the end of the last day
# timeStart_firstDay = dt_start.time()
# timeEnd_lastDay = dt_end.time()

day_start = dt_start.date()  # now it is a date
day_end   = dt_end.date()
delta = timedelta(days=1)


# initialize duration
now_durationWorkHours = 0.0


print ('Request: ', dt_start, ' -> ', dt_end)


# loop on the day
curr_date = day_start  # initialize
while curr_date <= day_end:
    print ('\n')
    print(curr_date.strftime("%Y-%m-%d"))
    
    # day of the week converted into name
    curr_weekday = curr_date.strftime('%A')
    print (curr_weekday) 

    # check what startTime and endTime today for work
    try:
        curr_workStartTime = now_workTime[curr_weekday]['startTime']
        curr_workEndTime   = now_workTime[curr_weekday]['endTime']
        print (curr_workStartTime, curr_workEndTime)
        
        # build dt of the start work today
        curr_dtStart_string = curr_date.strftime('%Y-%m-%d') + ' ' + curr_workStartTime + ':00'
        #print (curr_dtStart_string)
        today_dtStartWork_dt =  datetime.strptime(curr_dtStart_string, '%Y-%m-%d %H:%M:%S')
        #print (curr_dtStart_dt)
        
        curr_dtEnd_string = curr_date.strftime('%Y-%m-%d') + ' ' + curr_workEndTime + ':00'
        today_dtEndWork_dt = datetime.strptime(curr_dtEnd_string, '%Y-%m-%d %H:%M:%S')
        
        print ('Work times: ', today_dtStartWork_dt, ' -> ', today_dtEndWork_dt)
        
        
        # here we compute the start to consider
        today_considerStart = max(dt_start, today_dtStartWork_dt)
        
        # if (dt_start >= today_dtStartWork_dt):
        #     today_considerStart = dt_start
        # else:
        #     today_considerStart = today_dtStartWork_dt
        
        # compute the end in this day
        today_considerEnd = min(dt_end, today_dtEndWork_dt)
        # if (dt_end <= today_dtEndWork_dt):
        #     today_considerEnd = dt_end
        # else:
        #     today_considerEnd = today_dtEndWork_dt
        
        print ('Consider today = ', today_considerStart, ' -> ', today_considerEnd)
       
        
        
        # compute the duration in this day
        dur_today_hours = (today_considerEnd - today_considerStart).total_seconds() / 3600
        
        # add to now_durationWorkHours
        now_durationWorkHours += dur_today_hours
        
        
        
    except:
        print ('Not found start time')
    
    
    curr_date += delta
    
    
    
print ('\n***FINAL: total hours = ', now_durationWorkHours)


# format in formatted
here_intnr_days = int(now_durationWorkHours // now_nrHoursInFullDay)
here_hours_left = now_durationWorkHours - here_intnr_days*now_nrHoursInFullDay
# here_intnr_days, here_hours_left = divmod(now_durationWorkHours, now_nrHoursInFullDay)

# print (int(here_intnr_days))
# print (here_hours_left)

here_inthours = int(here_hours_left)
here_int_minutes = int(round((here_hours_left - here_inthours)*60, 1))
# print (here_inthours, here_int_minutes)

now_durationWorkTimeFormatted = f"{here_intnr_days}d_{here_inthours}h_{here_int_minutes}m"

print ('*** FINAL formatted = ', now_durationWorkTimeFormatted)
print ('MEMO: hours in a day = ', now_nrHoursInFullDay)


