import logging
import re
import random

from telegram import Update, ForceReply # type: ignore
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters # type: ignore

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Expresiones regulares
conversion_celsius_a_fahrenheit_expresion_regular = re.compile(r"convierte\s*(\d+(?:\.\d+)?)\s*celcius\s*a\s*F", re.IGNORECASE)
frase_celebre_expresion_regular = re.compile(r"frase(s)?\s*celebre(s)?", re.IGNORECASE)
suscripcion_noticias_expresion_regular = re.compile(r"correo|suscribir|noticias", re.IGNORECASE)
curiosidad_expresion_regular = re.compile(r"curiosidad|sabias\s*que", re.IGNORECASE)
correo_expresion_regular = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message if it matches any regular expression."""
    message_text = update.message.text

    if conversion_celsius_a_fahrenheit_expresion_regular.search(message_text):
        # Conversión de Celsius a Fahrenheit
        match = conversion_celsius_a_fahrenheit_expresion_regular.search(message_text)
        if match:
            celsius = float(match.group(1))
            fahrenheit = (celsius * 9/5) + 32
            await update.message.reply_text(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

    elif frase_celebre_expresion_regular.search(message_text):
        # Frases célebres
        famous_quotes = [
            "La única manera de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
            "La vida es lo que pasa mientras estás ocupado haciendo otros planes. - John Lennon",
            "No cuentes los días, haz que los días cuenten. - Muhammad Ali",
            "La creatividad es la inteligencia divirtiéndose. - Albert Einstein",
            "No esperes por la ocasión. Créala. - George Bernard Shaw"
        ]
        selected_quote = random.choice(famous_quotes)
        await update.message.reply_text(selected_quote)

    elif suscripcion_noticias_expresion_regular.search(message_text):
        # Suscripción a noticias
        await update.message.reply_text("Por favor, ingresa tu correo para suscribirte a nuestro boletín de noticias.")

    elif correo_expresion_regular.search(message_text):
        # Respuesta después de recibir un correo electrónico
        await update.message.reply_text("Gracias por suscribirte a nuestro boletín de noticias. Te mantendremos informado.")

    elif curiosidad_expresion_regular.search(message_text):
        # Curiosidades aleatorias
        random_fact = random.choice([
            "El agua caliente se congela más rápido que el agua fría bajo ciertas condiciones.",
            "Los koalas tienen huellas dactilares muy similares a las humanas.",
            "El corazón de una ballena azul es tan grande que una persona podría nadar a través de sus arterias.",
            "El sonido de un trueno puede medir hasta 120 decibeles.",
            "La miel no se echa a perder, incluso después de miles de años.",
        ])
        await update.message.reply_text(random_fact)

    else:
        await update.message.reply_text("No entendí tu mensaje.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token("7168656909:AAFmiCtKA2cjD7Jv7Eg4n0ISvNJpi8KG5ws").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
