# Thx @ShreyasSubhedar for the beautiful code (https://github.com/ShreyasSubhedar/fcc-time-calculator/commits/master/time_calculator.py)

def add_time(start, duration, week=None):
  # split start week and AmPm
  start_time, ap = start.split()
  start_hour, start_min = start_time.split(':')
  start_hour = int(start_hour)
  start_min = int(start_min)

  # turn into 24
  if ap == "PM":
    start_hour = start_hour + 12

  # transfer duration
  duration_hour, duration_min = duration.split(':')
  duration_hour = int(duration_hour)
  duration_min = int(duration_min)

  # calculate total time and new time
  total_min = start_min + duration_min
  extra_hour = total_min // 60
  new_time_min = total_min % 60
  total_hour = start_hour + duration_hour + extra_hour
  new_time_hour = (total_hour % 24) % 12
  if new_time_hour == 0:
    new_time_hour = 12
    
  total_day = total_hour // 24

  # find AM and PM
  new_ap = ""
  if total_hour % 24 <= 11:
    new_ap = "AM"
  else:
    new_ap = "PM"

  # make display format for min
  if new_time_min <=9:
    display_min = "0" + str(new_time_min)
  else:
    display_min = str(new_time_min)


  # output
  week_dict = {"Sunday":0, "Monday":1, "Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5, "Saturday":6}

  if week == None:
    if total_day == 0:
      new_time = str(new_time_hour) + ":" + display_min + ' ' + new_ap
    elif total_day == 1:
      new_time = str(new_time_hour) + ":" + display_min + ' ' + new_ap + " (next day)"
    else:
      #days = total_hour % 24
      new_time = str(new_time_hour) + ":" + display_min + ' ' + new_ap + " (" + str(total_day) + " days later)"
    return new_time
  else:
    week = week.lower().capitalize()
    new_week = (week_dict[week] + total_day) % 7
    for i, j in week_dict.items():
      if j == new_week:
        new_week = i
        break
    if total_day == 0:
      new_time = str(new_time_hour) + ":" + display_min + ' ' + new_ap + ', ' + new_week
    elif total_day == 1:
      new_time = str(new_time_hour) + ":" + display_min + ' ' + new_ap + ', ' + new_week + " (next day)" 
    else:
      new_time = str(new_time_hour) + ":" + display_min + ' ' + new_ap + ', ' + new_week + " (" + str(total_day) + " days later)" 
    return new_time
