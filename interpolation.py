# -*- coding: utf-8 -*-
"""Interpolation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q4AL-h5GD9YRzaTsCvCowsBGsP7SUP5b
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Ismert feszültség (V) és távolság (cm) adatok a dokumentáció alapján
voltages = np.array([2.3, 1.0, 0.5, 0.3])  # Kimeneti feszültségek
distances = np.array([20, 50, 100, 150])   # Hozzá tartozó távolságok

# Interpoláció létrehozása
distance_from_voltage = interp1d(voltages, distances, kind='linear', fill_value="extrapolate")

# Függvény a távolság kiszámításához feszültség alapján
def get_distance(voltage):
    return distance_from_voltage(voltage)

# Példa használatra
voltage_input = 1.5  # Például 1.5 V bemeneti feszültség
distance_output = get_distance(voltage_input)
print(f"A távolság {voltage_input} V feszültség esetén: {distance_output} cm")

# Eredeti adatok megjelenítése
plt.plot(distances, voltages, 'o', label='Eredeti adatok')

# Generálj új feszültség értékeket az interpolációhoz
voltage_range = np.linspace(min(voltages), max(voltages), 100)
interpolated_distances = get_distance(voltage_range)

# Interpolált görbe hozzáadása a plothoz
plt.plot(interpolated_distances, voltage_range, '-', label='Interpolált görbe')

# Plot megjelenítése
plt.xlabel('Távolság (cm)')
plt.ylabel('Feszültség (V)')
plt.legend()
plt.show()