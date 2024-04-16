# Tarea 2.3

### Expresión regular para validar una contraseña fuerte:
```markdown
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$
```
![evidencia](https://github.com/GermanZL/automatas/blob/master/Tareas/Tarea%202.2/img/contr.jpeg)

Esta expresión regular valida un password que cumpla con los siguientes criterios:
- Debe contener al menos 1 letra minúscula.
- Debe contener al menos 1 letra mayúscula.
- Debe contener al menos 1 número.
- Debe contener al menos 1 carácter especial.
- Debe tener una longitud mínima de 8 caracteres.

### Expresión regular para validar un Nombre de usuario:

```markdown
^[a-zA-Z0-9_-]{3,16}$
```
![evidencia](https://github.com/GermanZL/automatas/blob/master/Tareas/Tarea%202.2/img/nomb.jpeg)

Esta expresión regular valida un nombre de usuario que cumpla con los siguientes criterios:
- Debe tener una longitud de entre 3 y 16 caracteres.
- Puede contener letras (mayúsculas o minúsculas), números, guiones medios o guiones bajos.

Zerón Lopez German Eduardo - 21200642
