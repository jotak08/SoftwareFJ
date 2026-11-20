 <div align="center">

# 💻 SOFTWARE FJ

### Sistema de Gestión de Clientes, Servicios y Reservas

**Proyecto académico desarrollado en Python**

<p>
  <img src="https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Paradigma-POO-6f42c1" alt="POO">
  <img src="https://img.shields.io/badge/Estado-En%20desarrollo-orange" alt="Estado">
</p>

</div>

---

## 📌 Descripción

**Software FJ** es una aplicación de consola desarrollada en Python que permite gestionar clientes, administrar diferentes tipos de servicios y controlar el ciclo de vida de las reservas.

El proyecto aplica los principios fundamentales de la **Programación Orientada a Objetos (POO)**, mediante clases, objetos, encapsulamiento, herencia, abstracción y polimorfismo.

## 🎯 Objetivos

- Implementar una estructura de software modular y organizada.
- Aplicar los principios de la programación orientada a objetos.
- Validar la información de clientes y servicios.
- Gestionar reservas mediante diferentes estados.
- Controlar errores mediante excepciones personalizadas.
- Registrar eventos del sistema mediante logs.

## ⚙️ Funcionalidades

| Módulo | Descripción |
|---|---|
| 👤 Clientes | Registro y validación de información de clientes. |
| 🏢 Salas | Gestión de reservas de salas y cálculo de costos. |
| 💻 Equipos | Alquiler de equipos según cantidad y duración. |
| 📚 Asesorías | Administración de servicios de asesoría. |
| 📅 Reservas | Registro, búsqueda, confirmación, cancelación y procesamiento. |
| ⚠️ Excepciones | Manejo de errores personalizados y controlados. |
| 📝 Logs | Registro de eventos y errores del sistema. |

## 🧠 Conceptos de programación aplicados

- **Encapsulamiento:** protección y validación de atributos.
- **Herencia:** reutilización de características entre clases.
- **Abstracción:** definición de clases y métodos abstractos.
- **Polimorfismo:** implementación de comportamientos específicos en diferentes servicios.
- **Excepciones:** control de situaciones inesperadas.
- **Modularidad:** separación del código por responsabilidades.

## 📂 Estructura del proyecto

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
└── README.md
```

## 🚀 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/USUARIO/SoftwareFJ.git
```

Reemplaza `USUARIO` por tu nombre de usuario de GitHub.

### 2. Entrar en la carpeta

```bash
cd SoftwareFJ
```

### 3. Ejecutar el programa

Asegúrate de tener Python instalado y ejecuta:

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

## 🛠️ Tecnologías utilizadas

- **Lenguaje:** Python.
- **Control de versiones:** Git.
- **Repositorio remoto:** GitHub.
- **Entorno de desarrollo:** Visual Studio Code.

## 🎓 Contexto académico

Proyecto desarrollado como parte de la formación académica del programa de **Ingeniería de Sistemas de la Universidad Nacional Abierta y a Distancia (UNAD)**, en el área de programación.

## 👨‍💻 Autor

Estudiante de Ingeniería de Sistemas — UNAD.

---

<div align="center">

**SOFTWARE FJ**

*Aprendiendo, construyendo y mejorando mediante el desarrollo de software.*

</div>