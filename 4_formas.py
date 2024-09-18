# Autor: Jonathan Hernández
# Fecha: 18 Septiembre 2024
# Descripción: Código para procesamiento de imagenes con Sobel 20 formas.
# GitHub: https://github.com/Jona163

# Cargar la imagen
image = Image.open('chems1.jpg')
image = np.array(image)

# Función para mostrar la imagen
def plot_image(image, title, ax):
    ax.imshow(image)
    ax.set_title(title, fontsize=10)
    ax.axis('off')


# Crear matrices de transformación
# 1. Traslación
def translation_matrix(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])


# 2. Rotación
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta), 0],
                     [np.sin(theta), np.cos(theta), 0],
                     [0, 0, 1]])


# 3. Escalamiento
def scaling_matrix(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])


# 4. Cizallado
def shearing_matrix(kx, ky):
    return np.array([[1, kx, 0],
                     [ky, 1, 0],
                     [0, 0, 1]])


# Función para aplicar la transformación
def apply_transformation(image, matrix):
    if len(image.shape) == 3:  # Imágenes RGB
        transformed_image = np.zeros_like(image)
        for i in range(image.shape[2]):  # Aplicar a cada canal
            inverse_matrix = np.linalg.inv(matrix)[:2, :2]
            offset = np.linalg.inv(matrix)[:2, 2]
            transformed_image[..., i] = affine_transform(image[..., i], inverse_matrix, offset=offset, output_shape=image.shape[:2])
            else:  # Imágenes en escala de grises
        inverse_matrix = np.linalg.inv(matrix)[:2, :2]
        offset = np.linalg.inv(matrix)[:2, 2]
        transformed_image = affine_transform(image, inverse_matrix, offset=offset, output_shape=image.shape)
     return transformed_image

# Configurar las subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Título general para el conjunto de imágenes
fig.suptitle('Transformaciones Imágenes', fontsize=16)


# Aplicar las transformaciones
# 1. Traslación (50 píxeles en x y 30 en y)
translation = translation_matrix(50, 30)
translated_image = apply_transformation(image, translation)
plot_image(translated_image, 'Traslación (50 px en X, 30 px en Y)', axs[0, 0])

# 2. Rotación (45 grados)
rotation = rotation_matrix(np.radians(45))
rotated_image = apply_transformation(image, rotation)
plot_image(rotated_image, 'Rotación 45°', axs[0, 1])


# 3. Escalamiento (1.5x en X y 0.5x en Y)
scaling = scaling_matrix(1.5, 0.5)
scaled_image = apply_transformation(image, scaling)
plot_image(scaled_image, 'Escalamiento (1.5x en X, 0.5x en Y)', axs[1, 0])

# 4. Cizallado (0.5 en X, 0.2 en Y)
shearing = shearing_matrix(0.5, 0.2)
sheared_image = apply_transformation(image, shearing)
plot_image(sheared_image, 'Cizallado (0.5 en X, 0.2 en Y)', axs[1, 1])


# Ajustar el layout para evitar solapamientos
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

