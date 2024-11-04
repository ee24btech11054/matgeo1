import ctypes
import subprocess
import numpy as np
import matplotlib.pyplot as plt

def call_c_program():
    subprocess.run(["gcc", "intersect.c", "-o", "intersect","-lm"])
    # Run the C program and capture the output
    result = subprocess.run(["./intersect"], capture_output=True, text=True)
    return result.stdout

def plot_figure(intersection_point):
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = np.sqrt(32) * np.cos(theta)
    y_circle = np.sqrt(32) * np.sin(theta)

    # Line data (extended into the third quadrant)
    x_line = np.linspace(-6, 6, 100)
    y_line = x_line

    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.plot(x_circle, y_circle, label='Circle: $x^2 + y^2 = 32$', color='blue')
    plt.plot(x_line, y_line, label='Line: $y = x$', color='orange')

    # Extract intersection points for filling the sector
    intersection_x1, intersection_y1 = intersection_points[0]  # First intersection point
    intersection_x2, intersection_y2 = intersection_points[1]  # Second intersection point

    # Create sector area data
    sector_theta = np.linspace(0, np.arctan2(intersection_y1, intersection_x1), 100)
    x_sector = np.concatenate([[0], np.sqrt(32) * np.cos(sector_theta)])
    y_sector = np.concatenate([[0], np.sqrt(32) * np.sin(sector_theta)])

    # Fill the sector area
    plt.fill(x_sector, y_sector, color='lightblue', alpha=0.5, label='Area of Interest')

    # Plotting intersection points and the origin
    for point, label in zip(intersection_points, ['P (4, 4)', 'Q (-4, -4)']):
        plt.scatter(*point, color='red')
        plt.annotate(label, point, textcoords="offset points", xytext=(-10,10), ha='center')

    # Label the origin
    origin = (0, 0)
    plt.scatter(*origin, color='green')
    plt.annotate('Origin (0, 0)', origin, textcoords="offset points", xytext=(-10,10), ha='center')

    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.title('Area Enclosed in the First Quadrant')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.grid()
    plt.savefig('circlenline.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    output = call_c_program()
    print(output)  # Print the center and intersection points

    # Assuming the known intersection points (from the C code output)
    intersection_points = [(4, 4), (-4, -4)]  # Modify based on actual output if needed
    plot_figure(intersection_points)
