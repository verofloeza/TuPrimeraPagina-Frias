# Proyecto: Sistema de Solicitudes de Reparaciones

## Descripción
Esta aplicación está diseñada para gestionar servicios de reparaciones. Permite a los usuarios registrar, gestionar y buscar solicitudes de reparaciones y administrar roles y usuarios relacionados con el sistema.

---

## Funcionalidades Principales

1. **Inicio de Sesión (Login):**
   - En la raíz del proyecto (`/`) se va a encontrar el formulario de login, que permite a los usuarios autenticarse para acceder al sistema.

2. **Gestión de Usuarios:**
   - Accediendo a la ruta `/usuarios/` se despliega un CRUD completo para la gestión de usuarios.
   - **Columna "Activo":**
     - Cada usuario tiene un indicador de estado en la columna "Activo". Al hacer clic sobre este indicador, el estado cambia entre "Activo" e "Inactivo".

3. **Gestión de Roles:**
   - Desde el módulo "Roles", los administradores pueden:
     - **Agregar Roles:** Crear nuevos roles necesarios para el proyecto.
     - **Eliminar Roles:** Eliminar roles existentes del sistema.

4. **Gestión de Solicitudes de Repuestos:**
   - Este módulo permite visualizar todas las solicitudes realizadas y realizar operaciones CRUD:
     - **Crear:** Registrar nuevas solicitudes.
     - **Leer:** Consultar las solicitudes existentes.
     - **Actualizar:** Modificar información de una solicitud.
     - **Eliminar:** Eliminar solicitudes innecesarias.

5. **Búsqueda Avanzada en Solicitudes de Repuestos:**
   - Permite buscar solicitudes específicas utilizando los siguientes filtros:
     - **Por Título y Descripción:** Encuentra solicitudes que coincidan con palabras clave.
     - **Por Fecha:** Filtra solicitudes realizadas en un rango de fechas específico.



