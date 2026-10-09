import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Get token from environment variable
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /start is issued."""
    await update.message.reply_text(
        "Welcome to the Crypto Info Bot!\n\n"
        "I provide cryptocurrency information and market updates.\n"
        "Use /help to see available commands.\n\n"
        "⚠️ Disclaimer: This bot does not provide financial advice."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a help message."""
    await update.message.reply_text(
        "Available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/price <symbol> - Get price (e.g., /price BTC)\n"
        "/news - Latest crypto headlines\n"
        "/disclaimer - Important legal notice"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /price command."""
    if not context.args:
        await update.message.reply_text("Usage: /price <symbol>\nExample: /price BTC")
        return
    
    symbol = context.args[0].upper()
    # Placeholder - replace with actual data source
    await update.message.reply_text(
        f"📊 {symbol} Price Information\n\n"
        f"Current price: $--,---\n"
        f"24h Change: --%\n\n"
        f"⚠️ Prices are for informational purposes only."
    )

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /news command."""
    await update.message.reply_text(
        "📰 Latest Crypto Headlines\n\n"
        "1. [Headline placeholder]\n"
        "2. [Headline placeholder]\n"
        "3. [Headline placeholder]\n\n"
        "⚠️ News summaries are informational only."
    )

async def disclaimer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send disclaimer."""
    await update.message.reply_text(
        "⚠️ IMPORTANT DISCLAIMER\n\n"
        "This bot provides information for educational purposes only. "
        "Nothing here constitutes financial advice. "
        "Cryptocurrency investments carry significant risk. "
        "Always do your own research and consult a financial advisor."
    )

def main():
    """Start the bot."""
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set")
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("disclaimer", disclaimer))
    
    print("Bot is starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
