import fastf1 as f1

from util import seasonCalendar

f1.api.Cache.enable_cache('f1cache')

raceWeekends = []

for x in seasonCalendar.keys():
    raceWeekends.append(f1.get_session(2021, x))