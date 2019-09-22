# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
x = np.array(range(100))
y = x ** 2

# Create the plot
plt.plot(x,y)

# Show the plot
plt.show()

#it seems that plotlib saves the plots here