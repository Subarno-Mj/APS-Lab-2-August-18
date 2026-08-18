from data import linear_data, non_linear_data
import matplotlib.pyplot as plt

# Get the data
linear_x, linear_y = linear_data()
nonlinear_x, nonlinear_y = non_linear_data()

# Create the graph
plt.figure(figsize=(10, 6))

# Linear data
plt.scatter(
    linear_x,
    linear_y,
    color="blue",
    label="Linear Data"
)

# Non-linear data
plt.scatter(
    nonlinear_x,
    nonlinear_y,
    color="red",
    label="Non-Linear Data"
)

# Labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear vs Non-Linear Data")

# Show legend and grid
plt.legend()
plt.grid(True)

# Display graph
plt.show()