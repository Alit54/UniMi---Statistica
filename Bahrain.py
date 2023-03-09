import matplotlib.pyplot as plt
import pandas as pd
from timple.timedelta import strftimedelta
import fastf1
import fastf1.plotting
from fastf1.core import Laps

# load a session and its telemetry data
session = fastf1.get_session(2023, 'Bahrain Grand Prix', 'R')
session.load()

#get Alonso pace
alonso = session.laps.pick_driver('VER')

fig, ax = plt.subplots()

#MODIFY
ax.barh(alonso.index, alonso['LapTime'])
ax.set_xticks(alonso.index-113)

# show fastest at the top
ax.invert_yaxis()

# draw vertical lines behind the bars
ax.set_axisbelow(True)
ax.xaxis.grid(True, which='major', linestyle='--', color='black', zorder=-1000)

#lap_time_string = strftimedelta(pole_lap['LapTime'], '%m:%s.%ms')

#plt.suptitle(f"{session.event['EventName']} {session.event.year} Qualifying\n"
#             f"Fastest Lap: {lap_time_string} ({pole_lap['Driver']})")

plt.show()