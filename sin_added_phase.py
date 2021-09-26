import numpy as np
import math
import matplotlib.pyplot as plt
import streamlit as st

angle = np.arange(0,361)
# Set Amplitude
amp = 10
pi = math.pi
# constant phas
const_phase = pi/3
# added phase
added_phase = pi/6
# Angle in Radians
angle_rad = angle*pi/180 + const_phase

# Cosine and Sine curves
value_sine = [amp*math.sin(angles) for angles in angle_rad]
value_sine_added_phase = [amp*math.sin(angles + added_phase) for angles in angle_rad]

fig, ax = plt.subplots(3,1)
fig.suptitle('Sine with constant and added phases, {} rad'.format(str(const_phase)))

ax[0].plot(angle_rad, value_sine, color = 'b',)
ax[0].plot(angle_rad, value_sine_added_phase, color= 'r')

ax[1].plot(angle_rad, value_sine, color = 'b')
ax[2].plot(angle_rad, value_sine_added_phase,color= 'r')
ax[2].set_xlabel('radian angle')

plt.show()
st.pyplot(fig)