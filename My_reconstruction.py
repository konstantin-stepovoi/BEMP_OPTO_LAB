import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Запрашиваем у пользователя имя файла для загрузки
file_name = input("Введите имя файла для загрузки восстановленных изображений (например, 'reconstructed_images.txt'): ")

# Загружаем данные из текстового файла
try:
    reconstructed_images = np.loadtxt(file_name)  # Загружаем восстановленные изображения
except Exception as e:
    print(f"Ошибка при загрузке файла: {e}")
    exit()  # Завершаем выполнение программы в случае ошибки

# Определяем параметры срезов
n_slices = reconstructed_images.shape[0]  # Общее количество срезов
initial_slice = n_slices // 2  # Начальный срез

# Создаем фигуру и ось для отображения
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # Оставляем место для ползунка

# Отображаем первый срез
img = ax.imshow(reconstructed_images[initial_slice].reshape(151, 151), cmap='gray')  # Реконструируем 2D изображение
ax.set_title(f'Reconstructed Slice at index {initial_slice}')
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
    img.set_data(reconstructed_images[slice_index].reshape(151, 151))  # Обновляем данные изображения
    ax.set_title(f'Reconstructed Slice at index {slice_index}')  # Обновляем заголовок
    cbar.update_normal(img)  # Обновляем цветовую шкалу
    plt.draw()  # Перерисовываем фигуру

# Привязываем функцию обновления к ползунку
slice_slider.on_changed(update)

# Показываем фигуру
plt.show()
