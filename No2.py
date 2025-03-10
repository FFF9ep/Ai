import matplotlib.pyplot as plt


def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1
    dx2 = 2 * dx
    dy2 = 2 * dy

    if dy < 0:
        dy2 = -dy2
        stepy = -1
    else:
        stepy = 1

    if dx < 0:
        dx2 = -dx2
        stepx = -1
    else:
        stepx = 1

    if dx > dy:
        p = dy2 - dx
        while x1 != x2:
            points.append((x1, y1))
            x1 += stepx
            if p > 0:
                y1 += stepy
                p += dy2 - dx2
            else:
                p += dy2
    else:
        p = dx2 - dy
        while y1 != y2:
            points.append((x1, y1))
            y1 += stepy
            if p > 0:
                x1 += stepx
                p += dx2 - dy2
            else:
                p += dx2

    points.append((x1, y1))
    return points


x1, y1 = 2, 1
x2, y2 = 5, 6

points = bresenham_line(x1, y1, x2, y2)

x_vals, y_vals = zip(*points)
plt.plot(x_vals, y_vals, marker='o')
plt.title("Bresenham's Line Algorithm: (2,1) to (5,6)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
