import matplotlib.pyplot as plt


def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    increment_x = dx / steps
    increment_y = dy / steps

    x, y = x1, y1
    points = [(x, y)]

    for _ in range(int(steps)):
        x += increment_x
        y += increment_y
        points.append((round(x), round(y)))

    return points


x1, y1 = 0, 0
x2, y2 = 4, 6

points = dda(x1, y1, x2, y2)

x_vals, y_vals = zip(*points)
plt.plot(x_vals, y_vals, marker='o')
plt.title("DDA Line Drawing Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
