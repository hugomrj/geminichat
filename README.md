
# Chat con IA usando Flask y Bootstrap 5

Este proyecto utiliza Flask para crear una aplicación web de chat interactivo con una IA, donde puedes hacer preguntas y recibir respuestas generadas automáticamente. La interfaz del chat está diseñada con **Bootstrap 5** y se maneja con **vanilla JavaScript**.

## Requisitos

- Python 3.x
- Virtualenv

## Configuración del Proyecto

### 1. Crear un entorno virtual

Primero, crea un entorno virtual en tu máquina para aislar las dependencias del proyecto:

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

Dependiendo de tu sistema operativo, activa el entorno virtual:

- **Para sistemas basados en Unix (Linux/Mac):**

  ```bash
  source venv/bin/activate
  ```

- **Para sistemas basados en Windows:**

  ```bash
  venv\Scripts\activate
  ```

### 3. Instalar las dependencias

Instala las dependencias necesarias para el proyecto utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Ejecutar el Proyecto

### 1. Iniciar el servidor de desarrollo

Para probar la aplicación localmente, ejecuta el siguiente comando:

```bash
python run.py
```

Esto iniciará el servidor Flask en el puerto 5000 de manera predeterminada. Puedes acceder a la aplicación en tu navegador en la siguiente URL:

```
http://localhost:5000/chat
```


