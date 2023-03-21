#importing package
import matplotlib.pyplot as plt
import numpy as np
#Create the data
x = [-0.9,-0.8,-0.7,-0.6,-0.5,0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y = [np.sin(val) for val in x]
z = [np.sin(val)/val for val in x]
# Plot the curve and create labels
plt.plot(x, x, label = "Curve 1")
plt.plot(x, y, label = "Curve 2")
plt.plot(x, z, label = "Curve 3")

plt.legend() # Apply the given label
plt.show() # Let us see the curves
