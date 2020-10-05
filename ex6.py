import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.linspace(0, 10, 100)

print(x)


# Plot the data
plt.plot(x, 1, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()
