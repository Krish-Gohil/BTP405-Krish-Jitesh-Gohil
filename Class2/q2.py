import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80])
xpoints = np.array(["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"])

plt.plot(xpoints, ypoints)
plt.show()
