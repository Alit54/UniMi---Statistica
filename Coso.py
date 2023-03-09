import fastf1
from fastf1.core import Laps

# load a session and its telemetry data
session = fastf1.get_session(2023, 'Bahrain Grand Prix', 'Q')
session.load()

laps = session.laps
print(laps)
list_fastest_laps = list()
for driver in laps:
    lap = laps.pick_driver(driver).pick_fastest()
    list_fastest_laps.append(lap)

fastest_laps = Laps(list_fastest_laps).sort_values(by='LapTime').reset_index(drop=True)
print(fastest_laps)