def add_time(start, duration, day=False):
  week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

  time = {
    "hours": 0,
    "minutes": 0,
    "daysInt": 0,
    "days": "",
    "actualDayIndex": 0
  }


  if (day):
    for i, val in enumerate(week):
      if (val.lower() == day.lower()):
        time["actualDayIndex"] = i;
        break;

  tempTime = start.split(" ");
  temp = tempTime[0].split(":");
  time["hours"] = int(temp[0]);
  time["minutes"] = int(temp[1]);
  if (tempTime[1] == 'PM'):
    time["hours"] += 12;
  
  tempDuration = duration.split(":");
  time["hours"] += int(tempDuration[0]);
  time["minutes"] += int(tempDuration[1]);

  while(time["minutes"] >= 60):
    time["hours"] += 1;
    time["minutes"] -= 60;
  
  while(time["hours"] >= 24):
    time["hours"] -= 24;
    time["daysInt"] += 1;

  if (time["hours"] >= 12) :
    time["format"] = "PM";
    time["hours"] -= 12;
  else:
    time["format"] = "AM";
  
  if (time["hours"] == 0):
    time["hours"] = 12;
  
  time["hours"] = str(time["hours"]);
  if (time["minutes"] < 10):
    time["minutes"] = '0' + str(time["minutes"]);
  else:
    time["minutes"] = str(time["minutes"]);
  
  if (time["daysInt"] > 0):
    if (time["daysInt"] == 1):
      time["days"] = "(next day)";
    else:
      time["days"] = "(" + str(time["daysInt"]) + " days later)";

  moreDays = time["daysInt"];

  while(moreDays > 0):
    if (time["actualDayIndex"] >= len(week) - 1):
      time["actualDayIndex"] = 0;
    else:
      time["actualDayIndex"] += 1;
    moreDays -= 1;
    
  finalString = time["hours"] + ":" + time["minutes"] + " " + time["format"];

  if (day):
    if (time["daysInt"] > 0):
      finalString += ", " + week[time["actualDayIndex"]];
    else:
      finalString += ", " + day;

  if (time["days"] != ""):
    finalString += " " + time["days"];
  
  return finalString;
  