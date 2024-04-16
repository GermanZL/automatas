# Telegram Bot Botsillo
Procedemos a iniciar el bot con el comando /start y el bot te saludara

El código cuenta con 4 expresiones regulares curiosidad, frase célebre, conversión de Celsius a Fahrenheit y suscripción de correo

## 1.- Expresión de curiosidad:  
curiosidad_expresion_regular = re.compile(r"curiosidad|sabias\s*que", re.IGNORECASE)

![evidencia](https://github.com/GermanZL/automatas/blob/master/Tareas/Tarea%202.2/img/cap1.jpeg)
## 2.- Expresión de frase célebre:
frase_celebre_expresion_regular = re.compile(r"frase(s)?\s*celebre(s)?", re.IGNORECASE)

![evidencia](https://github.com/GermanZL/automatas/blob/master/Tareas/Tarea%202.2/img/cap2.jpeg)
## 3.- Expresión de conversión: 
conversion_celsius_a_fahrenheit_expresion_regular = re.compile(r"convierte\s*(\d+(?:\.\d+)?)\s*celcius\s*a\s*F", re.IGNORECASE)

![evidencia](https://github.com/GermanZL/automatas/blob/master/Tareas/Tarea%202.2/img/cap3.jpeg)
## 4.- Expresión de correo: 
suscripcion_noticias_expresion_regular = re.compile(r"correo|suscribir|noticias", re.IGNORECASE)

![evidencia](https://github.com/GermanZL/automatas/blob/master/Tareas/Tarea%202.2/img/cap4.jpeg)

Zeron Lopez German Eduardo - 21200642
