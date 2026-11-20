 <div align="center">
  <img src="https://frontapps.unad.edu.co/logo-unad-acreditacion-min.png" alt="Logo oficial de la Universidad Nacional Abierta y a Distancia - UNAD" width="430">

  <br>

  # SOFTWARE FJ

  ### Sistema de Gestión de Clientes, Servicios y Reservas

  **Proyecto académico — Ingeniería de Sistemas-Curso Programación**

  <p>
    <img src="https://img.shields.io/badge/Lenguaje-Python-blue?logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Programación-Orientada%20a%20Objetos-6f42c1" alt="POO">
    <img src="https://img.shields.io/badge/Universidad-UNAD-green" alt="UNAD">
    <img src="https://img.shields.io/badge/Estado-Desarrollado-success" alt="Estado">
  </p>

  
</div>

---

## 📖 1. Introducción

**Software FJ** es un proyecto académico desarrollado en Python como parte del proceso de aprendizaje del curso **Programación (213023)**, correspondiente al tercer período del programa de Ingeniería de Sistemas de la Universidad Nacional Abierta y a Distancia (UNAD).

El proyecto surge como un ejercicio práctico orientado a aplicar los fundamentos de la programación y, especialmente, los principios de la **Programación Orientada a Objetos (POO)** en el desarrollo de una solución informática.

La aplicación permite gestionar clientes, administrar diferentes tipos de servicios y controlar las reservas mediante operaciones de registro, consulta, confirmación, cancelación y procesamiento.

Durante su desarrollo se aplicaron conceptos como encapsulamiento, herencia, abstracción, polimorfismo, modularidad, validación de datos y manejo de excepciones.

## 🎓 2. Contexto institucional y académico

### Curso de Programación

Este proyecto se desarrolla tomando como fundamento los conocimientos trabajados en el curso **Programación (código 213023)**.

A través de Software FJ se busca llevar los conceptos de programación a un escenario práctico, organizando una solución mediante clases, objetos y módulos que representan entidades y procesos de un sistema de gestión.

El desarrollo permite fortalecer habilidades como:

- Análisis y solución de problemas mediante código.
- Diseño de clases y objetos.
- Aplicación de los principios de la programación orientada a objetos.
- Organización y modularización del software.
- Validación de información y control de errores.
- Pruebas de funcionamiento y depuración.

## 🎯 3. Objetivos del proyecto

### Objetivo general

Desarrollar una aplicación de consola en Python para gestionar clientes, servicios y reservas, aplicando los fundamentos de la programación orientada a objetos y buenas prácticas de organización del código.

### Objetivos específicos

- Implementar clases que representen las entidades principales del sistema.
- Aplicar encapsulamiento y validaciones para proteger la información.
- Utilizar herencia y abstracción para estructurar los diferentes tipos de servicios.
- Implementar polimorfismo para calcular y describir los servicios.
- Administrar el ciclo de vida de las reservas.
- Crear excepciones personalizadas para controlar situaciones de error.
- Implementar registros de eventos mediante el módulo de logging.
- Verificar el comportamiento del sistema mediante pruebas de operaciones válidas e inválidas.

## ⚙️ 4. Descripción y funcionalidades

Software FJ permite realizar las siguientes operaciones:

| Módulo | Funcionalidad |
|---|---|
| 👤 Clientes | Creación y validación de información de clientes. |
| 🏢 Reservas de salas | Gestión de salas, capacidad y cálculo de costos. |
| 💻 Alquiler de equipos | Administración de cantidades, duración y tarifas. |
| 📚 Asesorías | Gestión de servicios de asesoría y cálculo de costos. |
| 📅 Reservas | Registro, búsqueda, confirmación, cancelación y procesamiento. |
| ⚠️ Excepciones | Control de errores mediante excepciones personalizadas. |
| 📝 Logs | Registro de eventos y errores del sistema. |

## 🧠 5. Conceptos de programación aplicados

El desarrollo del proyecto integra los siguientes conceptos:

### Programación Orientada a Objetos

- **Clases y objetos:** representación de clientes, servicios y reservas.
- **Encapsulamiento:** protección de atributos mediante propiedades y validaciones.
- **Herencia:** reutilización de características entre clases relacionadas.
- **Abstracción:** definición de estructuras generales mediante clases abstractas.
- **Polimorfismo:** implementación de comportamientos específicos para cada tipo de servicio.

### Manejo de errores y excepciones

- Creación de excepciones personalizadas.
- Uso de `try`, `except`, `else` y `finally`.
- Encadenamiento de excepciones.
- Control de errores sin interrumpir innecesariamente la ejecución del programa.

### Organización y buenas prácticas

- Separación de responsabilidades mediante módulos y paquetes.
- Validación de parámetros.
- Registro de eventos mediante `logging`.
- Pruebas de escenarios correctos e incorrectos.

## 🏗️ 6. Arquitectura y estructura del proyecto

El proyecto está organizado en diferentes paquetes para separar las responsabilidades de cada componente.

```text
SoftwareFJ/
│
├── excepciones/
│   ├── __init__.py
│   └── errores.py
│
├── gestion/
│   ├── __init__.py
│   ├── reserva.py
│   └── reservas.py
│
├── modelos/
│   ├── __init__.py
│   ├── alquiler_equipos.py
│   ├── asesoria.py
│   ├── cliente.py
│   ├── entidad.py
│   ├── reserva_salas.py
│   └── servicios.py
│
├── configuracion.py
├── main.py
├── pruebas_excepciones.py
├── pruebas_operaciones.py
├── prueba.txt
├── .gitignore
└── README.md
```

### Descripción de los paquetes

- **modelos:** contiene las clases principales del sistema, como clientes, entidades y servicios.
- **gestion:** contiene la lógica para administrar las reservas.
- **excepciones:** define los errores personalizados del proyecto.
- **configuracion.py:** configura el registro de eventos mediante logging.
- **main.py:** punto de entrada y ejecución principal de la aplicación.
- **pruebas_operaciones.py:** verifica las operaciones de gestión de reservas.
- **pruebas_excepciones.py:** demuestra el manejo de excepciones y errores.

## 🚀 7. Instalación y ejecución

### Requisitos

- Python 3 instalado.
- Git.
- Un editor de código, preferiblemente Visual Studio Code.

### 1. Clonar el repositorio

```bash
git clone https://github.com/jotak08/SoftwareFJ.git
```

### 2. Ingresar al directorio

```bash
cd SoftwareFJ
```

### 3. Ejecutar la aplicación

```bash
python main.py
```

### 4. Ejecutar las pruebas

Pruebas de operaciones:

```bash
python pruebas_operaciones.py
```

Pruebas de excepciones:

```bash
python pruebas_excepciones.py
```

## 🧪 8. Pruebas del sistema

Se desarrollaron pruebas para verificar el comportamiento del sistema en diferentes escenarios.

Entre las operaciones verificadas se encuentran:

- Registro de reservas válidas.
- Búsqueda de reservas existentes.
- Confirmación de reservas.
- Prevención de confirmaciones duplicadas.
- Procesamiento de reservas.
- Control de reservas canceladas.
- Búsqueda de identificadores inexistentes.
- Validación de identificadores duplicados.
- Manejo de excepciones.
- Continuidad de ejecución después de errores controlados.

Estas pruebas permiten comprobar que el sistema responde adecuadamente tanto ante operaciones correctas como ante situaciones no permitidas.

## 🛠️ 9. Tecnologías y herramientas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje de programación. |
| Visual Studio Code | Entorno de desarrollo. |
| Git | Control de versiones. |
| GitHub | Almacenamiento y publicación del repositorio. |

## 📚 10. Referencias institucionales

- Universidad Nacional Abierta y a Distancia — UNAD. [Portal institucional](https://www.unad.edu.co/).

## 👨‍💻 11. Autor y proyecto académico

**Autor:** Jose Luis Ramirez

**Programa:** Ingeniería de Sistemas

**Institución:** Universidad Nacional Abierta y a Distancia — UNAD

**Curso:** Programación — Código 213023

**Proyecto:** Software FJ

**Repositorio:** [github.com/jotak08/SoftwareFJ](https://github.com/jotak08/SoftwareFJ)

---

<div align="center">

### UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA — UNAD

**Ingeniería de Sistemas**



**SOFTWARE FJ · Proyecto académico**

</div>