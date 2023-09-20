# assignment7_solution.py
#
# by: Kevin Goebbert
# date: 1 November 2022
# 
# Write a Python program that reads (5 points) in a sounding data file from the
# Wyoming sounding archive and print the raw data to standard output.
# The program input should be the sounding location (three-letter
# identifier) and date/time in YYYYMMDDHH.
# 
# Program Name: **soundings.py**
# 
# Program Input: Sounding Location and Date/Time
# 
# Program Output: Sounding Text File **(\<station
# ID\>\_YYYYMMDD\_HH.txt**) and Skew-T Image **(\<station
# ID\>\_YYYYMMDD\_HH.png**)

from datetime import datetime

import matplotlib.pyplot as plt
import metpy.calc as mpcalc
from metpy.plots import Hodograph, SkewT
from metpy.units import pandas_dataframe_to_unit_arrays, units
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
from siphon.simplewebservice.wyoming import WyomingUpperAir

station = input('Input Location: ')
input_date = input('Input Date/Time (YYYYMMDDHH): ')

date = datetime.strptime(input_date, '%Y%m%d%H')
#station = 'SGF'

df = WyomingUpperAir.request_data(date, station)

data = pandas_dataframe_to_unit_arrays(df)

p = data['pressure']
ip100 = p >= 100 * units.hPa

p = p[ip100]
T = data['temperature'][ip100]
Td = data['dewpoint'][ip100]
uwnd = data['u_wind'][ip100]
vwnd = data['v_wind'][ip100]
height = data['height'][ip100]

theta = mpcalc.potential_temperature(p, T)
relh = mpcalc.relative_humidity_from_dewpoint(T, Td)
mixing_ratio = mpcalc.mixing_ratio_from_relative_humidity(p, T, relh)
wind_speed = mpcalc.wind_speed(uwnd, vwnd)
wind_direction = mpcalc.wind_direction(uwnd, vwnd)

lclp, lclT = mpcalc.lcl(p[0], T[0], Td[0])
lfcp, lfcT = mpcalc.lfc(p, T, Td)
elp, elT = mpcalc.el(p, T, Td)
parcel_temperature = mpcalc.parcel_profile(p, T[0], Td[0])
lifted_index = mpcalc.lifted_index(p, T, parcel_temperature)
total_totals = mpcalc.total_totals_index(p, T, Td)
cape, cin = mpcalc.cape_cin(p, T, Td, parcel_temperature)

with open(f'K{station}_{date:%Y%m%d%H}_data.txt', 'w') as f:
    f.write(f'K{station} Observations at {date:%HZ %d %B %Y}\n')
    f.write('-------------------------------------------------\n')
    f.write('  PRES  TEMP  DWPT  RELH   MIXR  DRCT  SKNT  THTA\n')
    f.write('  hPa    C     C     %     g/kg   deg  knot   K  \n')
    f.write('-------------------------------------------------\n')
    for i in np.arange(p.shape[0]):
        f.write(f'{p[i].m:6.1f} {T[i].m:5.1f} {Td[i].m:5.1f} {relh[i].to("percent").m:5.1f} '
                f'{mixing_ratio[i].to("g/kg").m:6.1f} {wind_direction[i].m:5.0f}'
                f'{wind_speed[i].m:5.0f} {theta[i].m:6.1f}\n')
    f.write('\n')
    f.write('Station information and sounding indicies\n')
    f.write('\n')
    f.write(f'Station identifier: {station}\n')
    f.write(f'Observation time: {date:%y$m$d/%H%M}\n')
    f.write(f'Lifted Index: {lifted_index[0].m:.1f} C\n')
    f.write(f'Total Totals Index: {total_totals.m:.1f}\n')
    f.write(f'SBCAPE: {cape.m:.1f} J/kg\n')
    f.write(f'SBCIN: {cin.m:.1f} J/kg\n')
    f.write(f'LCL: {lclp.m:.0f} hPa\n')
    f.write(f'LFC: {lfcp.m:.0f} hPa\n')
    f.write(f'EL: {elp.m:.0f} hPa\n')
    f.write('\n')
    
    flag = 0
    if cape >= 1500 * units('J / kg'): flag += 1
    if cin >= -125 * units('J / kg'): flag += 1
    if lifted_index <= -2 * units.delta_degC: flag += 1

    if flag >= 2:
        f.write("WARNING: SEVERE THUNDERSTORMS ARE POSSIBLE!")
    else:
        f.write("NOTE: Severe Thunderstorms Not Likely To Occur.")

fig = plt.figure(1, figsize=(12, 12))
skew = SkewT(fig, rotation=45)

skew.plot(p, T, 'tab:red')
skew.plot(p, Td, 'tab:green')
skew.plot(p, parcel_temperature, 'black')

skew.plot_barbs(p, uwnd, vwnd)

skew.plot_dry_adiabats(t0=np.arange(220, 530, 10)*units.K, alpha=0.25)
skew.plot_moist_adiabats(colors='tab:green', alpha=0.25)
skew.plot_mixing_lines(pressure=np.arange(1000, 100, -1)*units.hPa,
                       colors='tab:blue', ls='dotted', alpha=0.5)

skew.ax.set_xlim(-30, 35)
skew.ax.set_ylim(1000, 100)

skew.shade_cape(p, T, parcel_temperature)
skew.shade_cin(p, T, parcel_temperature, dewpoint=Td)

# Create a hodograph
ax_hod = inset_axes(skew.ax, '25%', '25%', loc='upper left')
h = Hodograph(ax_hod, component_range=wind_speed.max().m)
h.add_grid(increment=20)
ih6 = height <= 6 * units.km
h.plot_colormapped(uwnd[ih6], vwnd[ih6], height[ih6])

skew.ax.set_title(f'Station: K{station}', loc='left')
skew.ax.set_title(f'Valid:{date} UTC', loc='right')
plt.savefig(f'K{station}_{date:%Y%m%d%H}_sounding.png', dpi=150, bbox_inches='tight')
