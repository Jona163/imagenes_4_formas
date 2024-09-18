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
