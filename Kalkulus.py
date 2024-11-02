import numpy as np
import matplotlib.pyplot as plt

# Persamaan garis
x_garis = np.linspace(-3, 2, 100)
y_garis = -x_garis + 1

# Persamaan parabola
x_parabola = np.linspace(-3, 1, 100)
y_parabola = (x_parabola + 1)**2

# Titik potong dengan sumbu x dan y
titik_potong_x = -1
titik_potong_y = 1

# Titik puncak parabola
titik_puncak_x = 1
titik_puncak_y = 0

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_garis, y_garis, label='y = -x + 1')
plt.plot(x_parabola, y_parabola, label='y = (x + 1)^2')

# Menandai titik potong dengan sumbu x
plt.scatter([titik_potong_x], [0], color='red')
plt.text(titik_potong_x + 0.1, -0.5, f'({titik_potong_x}, 0)', color='red')

# Menandai titik potong dengan sumbu y
plt.scatter([0], [titik_potong_y], color='green')
plt.text(0.1, titik_potong_y + 0.5, f'(0, {titik_potong_y})', color='green')

# Menandai titik puncak parabola
plt.scatter([titik_puncak_x], [titik_puncak_y], color='purple')
plt.text(titik_puncak_x + 0.1, titik_puncak_y + 0.5,
         f'({titik_puncak_x}, {titik_puncak_y})', color='purple')

# Menambahkan label dan legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Grafik Persamaan Garis dan Parabola')
plt.legend()
plt.grid(True)
plt.show()
