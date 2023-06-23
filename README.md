# Análisis preliminar de datos con ChatGPT

This project is a `Django` application made to comply with challenge provided
by [Digitalia Tec](https://digitaliatec.com/).

## The challenge

### Objetivo

Desarrollar una aplicación que utilice la API de ChatGPT para realizar una interpretación básica de los datos cargados
por el usuario.
La interpretación deberá ser lo suficientemente descriptiva para que el usuario pueda entender la naturaleza de los
datos y sugerir posibles direcciones para un análisis más profundo.

### Autenticación y autorización

Desarrolla un endpoint de autenticación que permita a los usuarios ingresar su API Key de ChatGPT para pruebas.
Este proceso deberá manejar la verificación y validación de las claves de API proporcionadas.

### Interfaz de carga de datos

Implementa un endpoint que permita a los usuarios subir archivos de datos en formato CSV. Esta funcionalidad debe
manejar la validación y procesamiento de archivos `.csv`, así como la extracción de datos para su uso en ChatGPT.

### Interpretación de datos con ChatGPT

Utiliza la API de ChatGPT para leer las columnas del CSV subido, entender la información y proporcionar una descripción
inicial de los datos.
Esto incluye identificar el tipo de información en cada columna (por ejemplo, numérica, categórica), el rango de
valores, y cualquier patrón observable.
Además, ChatGPT debe ser capaz de sugerir posibles análisis a realizar con los datos, basándose en su comprensión
inicial.
Ten en cuenta que el objetivo no es que ChatGPT realice un análisis exhaustivo de los
datos, sino que proporcione un resumen inicial y sugerencias para análisis futuros.

### Interfaz de usuario

Desarrolla una interfaz de usuario básica para permitir la interacción con la aplicación.
Esta interfaz debe permitir la entrada de la API Key, la carga de archivos `.csv` y la visualización de los resultados
de la interpretación de datos proporcionada por ChatGPT.

### Recomendación

Cuando utilices ChatGPT, es importante que dividas el proceso en diferentes prompts con contexto, para asegurar que las
respuestas sean pertinentes y útiles.

## Approach

- Crear una página registro que recibe una API key y hace un fetch de la lista de modelos de OpenAI para validar la
  llave.
- Un modelo que guarde el archivo y el query inicial.
- Un modelo que guarde los mensajes tanto del query como de la respuesta.

## Improvements

- Mejorar la navegación y la vista para que el formulario cambie luego de subir el archivo y muestro solo el chat entre
  el usuario y OpenAI.
- Mejorar el prompt inicial para que genere respuestas adecuadas tanto en lectura de usuario como en lectura de
  software.
- Generar pruebas y cobertura del programa.
