import numpy as np
import matplotlib.pyplot as plt

x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.01, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise
y = np.square(x_data) - 0.5

# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x_data, y_data)
ax.plot(x_data, y, color="red")
plt.show()
