# Manual de usuario - Los Valves

Autor: Jorge Sánchez

## 1. ¿Qué es esta aplicación?

Los Valves es una aplicación de Odoo para gestionar los videojuegos de un catálogo, los estudios que los desarrollan, y los empleados y departamentos de la empresa.

## 2. Cómo entrar

Una vez instalado el módulo, abre Odoo y pulsa en la aplicación "Los Valves" del menú principal. Arriba verás cuatro opciones: Videojuegos, Estudios, Empleados y Departamentos.

Todos los usuarios internos pueden ver, crear, modificar y borrar registros en las cuatro secciones.

## 3. Cómo se usa cualquier sección

Todas las secciones funcionan igual:

- Al entrar se muestra una lista con los registros existentes.
- Para crear uno nuevo, pulsa el botón "Nuevo", rellena los campos y guarda.
- Para ver o modificar uno existente, haz clic sobre él en la lista, cambia lo que necesites y guarda.
- Para borrarlo, marca la casilla del registro en la lista (o ábrelo) y usa el menú "Acciones" > "Eliminar".
- Para volver a la lista desde una ficha, pulsa el nombre de la sección en la parte superior.

## 4. Videojuegos

Campos de la ficha:

- Nombre del videojuego (obligatorio, no puede estar vacío).
- Logo (opcional): imagen del videojuego.
- Lanzamiento (obligatorio): fecha de lanzamiento.
- Estudio (obligatorio): estudio que lo ha desarrollado. Puede existir previamente o ser creado dinámicamente en la sección Estudios.
- Precio (obligatorio): no puede ser negativo.
- Descuento (%): opcional, un valor entre 0 y 100.
- Precio final: se calcula solo a partir del precio y el descuento. No se puede editar.

Ejemplo: un juego de 25,00 con un 15% de descuento tendrá un precio final de 21,25.

## 5. Estudios

Campos de la ficha:

- Nombre del estudio (obligatorio, mínimo 3 caracteres).
- Logo (opcional).
- Descripción (opcional).
- Videojuegos: lista de los juegos de ese estudio. Se rellena sola al crear videojuegos y asignarles el estudio.

Un estudio que tenga videojuegos no se puede borrar. Primero hay que borrar sus videojuegos o asignarlos a otro estudio.

## 6. Empleados

Campos de la ficha:

- Nombre (obligatorio).
- Apellidos (obligatorio).
- Fecha de nacimiento (obligatorio, no puede ser una fecha futura).
- Email (obligatorio).
- Salario (obligatorio, no puede ser negativo, pobres empleados...).
- Departamento (opcional): departamento al que pertenece. Puede existir previamente o ser creado dinámicamente en la sección Departamentos.

## 7. Departamentos

Campos de la ficha:

- Nombre (obligatorio, no puede estar vacío).
- Descripción (opcional).
- Jefe del departamento (opcional): se elige entre los empleados existentes.
- Empleados: lista de los empleados del departamento. Se rellena sola al asignar el departamento en la ficha de cada empleado.

Un departamento que tenga empleados no se puede borrar. Primero hay que cambiar de departamento a sus empleados. Si se borra un empleado que era jefe, el departamento se queda sin jefe.

## 8. Orden recomendado para introducir datos

1. Crear los estudios.
2. Crear los videojuegos y asignarles su estudio.
3. Crear los departamentos.
4. Crear los empleados y asignarles su departamento.
5. Volver a los departamentos y elegir el jefe de cada uno.

## 9. Mensajes de error habituales

- "El nombre no puede estar vacío": el nombre es obligatorio y no puede contener solo espacios.
- "El nombre del estudio debe tener al menos 3 caracteres".
- "El precio no puede ser negativo" / "El salario no puede ser negativo".
- "El descuento debe estar entre 0 y 100".
- "La fecha de nacimiento no puede ser futura".
- Error al eliminar un estudio o un departamento: todavía tiene videojuegos o empleados asociados (ver apartados 5 y 7).
