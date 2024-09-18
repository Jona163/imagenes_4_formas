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
