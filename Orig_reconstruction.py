import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Открываем .mat файл
file_path = 'suture/Reconstruction/Reconstructed.mat'  # Замените на путь к вашему файлу
with h5py.File(file_path, 'r') as f:
    # Получаем массив R
    R = f['R'][:]  # Загружаем данные из группы R

# Определяем параметры срезов
n_slices = R.shape[2]  # Общее количество срезов
initial_slice = n_slices // 2  # Начальный срез

# Создаем фигуру и ось для отображения
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # Оставляем место для ползунка

# Отображаем первый срез
img = ax.imshow(R[:, :, initial_slice], cmap='gray')
ax.set_title(f'Slice at index {initial_slice}')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Добавляем цветовую шкалу
cbar = plt.colorbar(img, ax=ax)

# Создаем ползунок для изменения индекса среза
ax_slider = plt.axes([0.25, 0.1, 0.5, 0.03])  # [left, bottom, width, height]
slice_slider = Slider(ax_slider, 'Slice', 0, n_slices - 1, valinit=initial_slice, valfmt='%0.0f')

# Функция для обновления изображения при изменении ползунка
def update(val):
    slice_index = int(slice_slider.val)  # Получаем текущее значение ползунка
    img.set_data(R[:, :, slice_index])  # Обновляем данные изображения
    ax.set_title(f'Slice at index {slice_index}')  # Обновляем заголовок
    cbar.update_normal(img)  # Обновляем цветовую шкалу
    plt.draw()  # Перерисовываем фигуру

# Привязываем функцию обновления к ползунку
slice_slider.on_changed(update)

# Показываем фигуру
plt.show()