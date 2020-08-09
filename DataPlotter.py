import numpy as np
import matplotlib.pyplot as plt
import pickle

# We load the data
with open('data_dict.pickle', 'rb') as file:
    data_dict = pickle.load(file)

# We store some general characteristics of the data
attributes_keys = list(data_dict.keys())
date_keys = list(data_dict[attributes_keys[0]].keys())
N = len(date_keys)
max_height = np.max([float(data_dict["Height (m)"][date_key]) for date_key in date_keys])
min_height = np.min([float(data_dict["Height (m)"][date_key]) for date_key in date_keys])
max_period = np.max([float(data_dict["Period (s)"][date_key]) for date_key in date_keys])
min_period = np.min([float(data_dict["Period (s)"][date_key]) for date_key in date_keys])

heights = [float(data_dict["Height (m)"][date_key]) for date_key in date_keys]
periods = [float(data_dict["Period (s)"][date_key]) for date_key in date_keys]
angles = [float(data_dict["Direction (°)"][date_key]) for date_key in date_keys]
#We convert the angles from degrees to radians
angles = [np.deg2rad(a) for a  in angles]


# Compute areas and colors (for now, area is set just to be proportional to the height of each wave)
area = [100*h for h in heights]
colors = heights

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
waveprint_circular_plot = ax.scatter(angles, periods, c=colors, s=area, cmap='hsv', alpha=0.8, edgecolor = "black")
fig.colorbar(waveprint_circular_plot, extend="both", label = "Height (m)")

#If we want to set custom lables
# ax.set_xticklabels(['E', 'N', 'W', 'S'])
# lines, labels = plt.thetagrids(range(0, 360, int(360/4)))

lines, labels = plt.thetagrids(range(0, 360, int(360/10)))

plt.show()