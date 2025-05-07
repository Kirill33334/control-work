from skimage import io
import matplotlib.pyplot as plt
from skimage.transform import resize

# Новый URL изображения (с прямым доступом)
url = "https://th.bing.com/th/id/OIP.rSh7nLhjMLt_Ke5jEFEU9AAAAA?cb=iwc1&rs=1&pid=ImgDetMain"
image = io.imread(url)

# Изменение до фиксированных размеров (например, 200x300)
resized_image = resize(image, (100, 150), anti_aliasing=True)

# Создаём 2 подграфика для отображения оригинального и изменённого изображений
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Отображаем оригинальное изображение
ax[0].imshow(image)
ax[0].set_title("Original Image")
ax[0].axis("off")

# Отображаем изменённое изображение
ax[1].imshow(resized_image)
ax[1].set_title("Resized (100x150)")
ax[1].axis("off")

# Показываем график
plt.show()