# 📌 Portfolio Personal con Flask

Este es un proyecto de portafolio personal desarrollado con **Flask** y **Bootstrap**, que permite mostrar información personal, formación académica, experiencia laboral y proyectos realizados. Además, incluye funcionalidades para agregar, editar y eliminar proyectos dinámicamente.

## 🚀 Tecnologías Utilizadas
- **Python** con **Flask** como framework backend.
- **SQLite** como base de datos para almacenar proyectos.
- **HTML, CSS y Bootstrap** para el diseño de la interfaz.
- **Git y GitHub** para control de versiones y despliegue del código.

## 📂 Estructura del Proyecto
```
Portfolio_Galeria/
├── app.py  # Código principal en Flask
├── portfolio.db  # Base de datos SQLite (se genera automáticamente)
├── static/
│   ├── uploads/  # Carpeta donde se guardan las imágenes
│   ├── css/  # Archivo de estilos
│   ├── js/  # Scripts opcionales
├── templates/
│   ├── index.html  # Página principal con la galería de proyectos
│   ├── upload.html  # Página para subir nuevos proyectos
│   ├── edit.html  # Página para editar proyectos
└── README.md  # Archivo de documentación
```

## 📖 Características del Proyecto
- 📌 **Sección de información personal:** Datos personales, formación académica y experiencia laboral.
- 🖼️ **Galería de proyectos:** Muestra proyectos con imagen y descripción.
- ➕ **Agregar proyectos:** Subida de imágenes y descripciones.
- ✏️ **Editar proyectos:** Modificación del título y descripción de los proyectos.
- 🗑️ **Eliminar proyectos:** Opción de borrar proyectos con su imagen asociada.

## 🛠️ Instalación y Ejecución
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/mi-portafolio.git
   cd mi-portafolio
   ```

2. **Crear un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install flask
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```
   La aplicación estará disponible en `http://127.0.0.1:5000/`

## 📌 Uso de la Aplicación
- **Desde la página principal**, puedes ver la información personal y la galería de proyectos.
- **Para agregar un proyecto**, haz clic en "Subir nuevo proyecto" y completa el formulario.
- **Para editar un proyecto**, haz clic en el botón "Editar" de un proyecto existente.
- **Para eliminar un proyecto**, haz clic en el botón "Eliminar".

## 📜 Licencia
Este proyecto es de uso libre y puede ser modificado según tus necesidades.

## 📬 Contacto
- 📧 Email: luismiphita@gmail.com
- 📍 Ubicación: Alcorcón, España

---
Si tienes sugerencias o mejoras, ¡no dudes en contribuir o ponerte en contacto! 🚀
