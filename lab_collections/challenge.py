import calendar
from collections import OrderedDict

hi_temps = [107, 108, 107, 105, 103]

days = list(calendar.day_abbr)

del days[-2:]
lv_temps_wk = dict(zip(days, hi_temps))

# print(lv_temps_wk.items())
# lv_temps_wk = sorted(lv_temps_wk.items(), key=lambda item: item[1])
# print(lv_temps_wk)


# ordered_lv_temps_wk = OrderedDict(lv_temps_wk)
# for key, value in ordered_lv_temps_wk.items():
#     print(key, value)

dict_lv_temps_wk = dict(lv_temps_wk)
for key, value in dict_lv_temps_wk.items():
    print(key, value)  
 
