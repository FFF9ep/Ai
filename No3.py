import matplotlib.pyplot as plt


def bresenham_circle(x_center, y_center, radius):
    points = []

    x = 0
    y = radius
    p = 3 - 2 * radius

    def plot_circle_points(xc, yc, x, y):
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))

    plot_circle_points(x_center, y_center, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 4 * x + 6
        else:
            y -= 1
            p += 4 * (x - y) + 10
        plot_circle_points(x_center, y_center, x, y)

    return points


x_center, y_center, radius = 0, 0, 5

points = bresenham_circle(x_center, y_center, radius)

x_vals, y_vals = zip(*points)
plt.plot(x_vals, y_vals, marker='o')
plt.title(
    f"Bresenham's Circle Algorithm: Center({x_center}, {y_center}), Radius {radius}")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
