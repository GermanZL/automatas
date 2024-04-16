## Telegram Bot Botsillo
Procedemos a iniciar el bot con el comando /start y el bot te saludara

El código cuenta con 4 expresiones regulares curiosidad, frase célebre, conversión de Celsius a Fahrenheit y suscripción de correo

#### 1.- Expresión de curiosidad:  
curiosidad_expresion_regular = re.compile(r"curiosidad|sabias\s*que", re.IGNORECASE)
<img src="img/cap1"> 
#### 2.- Expresión de frase célebre:
frase_celebre_expresion_regular = re.compile(r"frase(s)?\s*celebre(s)?", re.IGNORECASE)
<img src="img/cap2">
#### 3.- Expresión de conversión: 
conversion_celsius_a_fahrenheit_expresion_regular = re.compile(r"convierte\s*(\d+(?:\.\d+)?)\s*celcius\s*a\s*F", re.IGNORECASE)
<img src="img/cap3">
#### 4.- Expresión de correo: 
suscripcion_noticias_expresion_regular = re.compile(r"correo|suscribir|noticias", re.IGNORECASE)
<img src="img/cap4">
