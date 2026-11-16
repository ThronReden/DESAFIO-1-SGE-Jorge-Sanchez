# Registro de desarrollo

Autor: Jorge Sánchez

## 1. Descripción general

Módulo de Odoo (nombre técnico: modulo\_desafio, versión 0.1, categoría Tools) para el desafío 1 de SGE. Gestiona videojuegos y estudios desarrolladores, y por otro lado empleados y departamentos. Depende únicamente del módulo base y está marcado como aplicación, con el menú raíz "Los Valves".

## 2. Arquitectura general

El módulo sigue la estructura estándar de Odoo (modelo, vista, acción, menú):

- models/: una clase Python por modelo. El archivo `__init__.py` carga estudio, videojuego, empleado y departamento.
- views/: un XML por modelo con vista de lista, vista de formulario y la acción que las enlaza (modo list,form). Un XML adicional, menu.xml, define los menús.
- security/ir.model.access.csv: permisos de acceso a los modelos.
- demo.xml: datos de demostración, en la raíz del módulo.
- `__manifest__.py`: declara el módulo y el orden de carga de los ficheros de datos (seguridad, vistas de videojuego, estudio, empleado y departamento, y menús al final).
- Manual de usuario.md: manual de uso para el usuario final, en la raíz del módulo.

Los modelos están agrupados en dos bloques independientes, relacionados internamente por claves foráneas:

- Bloque de catálogo: Estudio (1) - (N) Videojuego.
- Bloque de personal: Departamento (1) - (N) Empleado, más la relación inversa Departamento (jefe) - (1) Empleado.

No hay relación entre ambos bloques.

## 3. Modelos creados

### modulo\_desafio.estudio (Estudio desarrollador)

- nombre (Char, obligatorio): se usa como nombre visible del registro.
- descripcion (Text).
- logo (Image).
- videojuego\_ids (One2many a videojuego, inverso estudio\_id).
- Restricciones: nombre no vacío y de al menos 3 caracteres.

### modulo\_desafio.videojuego (Videojuego)

- nombre (Char, obligatorio): etiqueta "Título"; nombre visible del registro.
- logo (Image) y descripcion (Text).
- fecha\_lanzamiento (Date, obligatorio).
- estudio\_id (Many2one a estudio, obligatorio, ondelete restrict).
- precio (Float, obligatorio, 10,2) y descuento (Float, 5,2, porcentaje).
- precio\_final (Float calculado): precio por (1 - descuento/100); si no hay descuento, es igual al precio.
- Restricciones: nombre no vacío, precio mayor o igual que 0, descuento entre 0 y 100.

### modulo\_desafio.departamento (Departamento)

- nombre (Char, obligatorio): nombre visible del registro.
- descripcion (Text).
- jefe\_id (Many2one a empleado, ondelete set null).
- empleado\_ids (One2many a empleado, inverso departamento\_id).
- Restricciones: nombre no vacío.

### modulo\_desafio.empleado (Empleado)

- nombre y apellidos (Char, obligatorios).
- nombre\_completo (Char calculado): nombre y apellidos concatenados; es el nombre visible del registro.
- fecha\_nacimiento (Date, obligatoria).
- email (Char, obligatorio).
- salario (Float, obligatorio).
- departamento\_id (Many2one a departamento, ondelete restrict).
- Restricciones: nombre y apellidos no vacíos, fecha de nacimiento no futura, email con arroba y punto, salario mayor o igual que 0.

## 4. Vistas creadas

Cada modelo tiene tres elementos en su fichero de vistas: vista de lista, vista de formulario y acción de ventana (view\_mode list,form).

- videojuego\_views.xml: lista con logo, nombre, lanzamiento, estudio, precio, descuento y precio final. Formulario con logo, título, descripción, lanzamiento, estudio, precio, descuento y precio final de solo lectura.
- estudio\_views.xml: lista con logo, nombre y descripción. Formulario con logo, nombre, descripción y lista incrustada de sus videojuegos.
- empleado\_views.xml: lista con nombre, apellidos, fecha de nacimiento, email, salario y departamento. Formulario con esos mismos campos.
- departamento\_views.xml: lista con nombre, descripción y jefe. Formulario con nombre, descripción, jefe y lista incrustada de sus empleados.
- menu.xml: menú raíz "Los Valves" con cuatro opciones hijas: Videojuegos (secuencia 10), Estudios (20), Empleados (30) y Departamentos (40).

## 5. Seguridad

El fichero ir.model.access.csv concede lectura, escritura, creación y borrado sobre los cuatro modelos al grupo base.group\_user (usuarios internos). No hay grupos ni reglas de registro propias.

## 6. Datos de demostración

demo.xml carga 2 estudios (Los Valves y Pixel Norte Games), 4 videojuegos, 2 departamentos (Desarrollo y Arte y Diseño) y 8 empleados, 4 por departamento. Al final asigna un jefe a cada departamento, ya que los empleados deben existir antes.

## 7. Decisiones de diseño

- ondelete restrict en estudio\_id y en departamento\_id: impide borrar un estudio con videojuegos o un departamento con empleados.
- ondelete set null en jefe\_id: si se borra al jefe, el departamento queda sin jefe.
- Las validaciones se hacen con @api.constrains en cada modelo, con mensajes de error en castellano.
- Los campos calculados (precio\_final y nombre\_completo) no se almacenan; se recalculan al consultarlos.
