import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from scoring import calculate_worth, analyze_handle
from utils import check_availability, suggest_handles, get_handle_history, check_fraud

# Your token is set directly here
BOT_TOKEN = "8331440932:AAHVTLYI2xy-FxySGDR68aOR74-6aBfm5CE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to LuxHandle — Telegram’s Elite Username Gateway!\n"
        "Send /worth @handle to check value instantly.\n"
        "Unlock premium features with /upgrade."
    )

async def worth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].startswith("@"):
        await update.message.reply_text("Usage: /worth @handle")
        return
    handle = args[0]
    score, breakdown = calculate_worth(handle)
    available = check_availability(handle)
    msg = (
        f"💎 **{handle}**\n"
        f"Availability: {'✅ Available' if available else '❌ Taken'}\n"
        f"Worth Score: {score}/75\n"
        "Breakdown:\n" +
        "\n".join(f"• {k}: {v}" for k, v in breakdown.items())
    )
    await update.message.reply_text(msg, parse_mode="Markdown")

async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].startswith("@"):
        await update.message.reply_text("Usage: /analyze @handle")
        return
    handle = args[0]
    analysis = analyze_handle(handle)
    await update.message.reply_text(analysis, parse_mode="Markdown")

async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].startswith("@"):
        await update.message.reply_text("Usage: /claim @handle")
        return
    handle = args[0]
    available = check_availability(handle)
    await update.message.reply_text(
        f"{handle} is {'✅ Available' if available else '❌ Taken'}"
    )

async def suggest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].startswith("@"):
        await update.message.reply_text("Usage: /suggest @handle")
        return
    handle = args[0]
    suggestions = suggest_handles(handle)
    await update.message.reply_text(
        "Smart suggestions:\n" + "\n".join(suggestions)
    )

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].startswith("@"):
        await update.message.reply_text("Usage: /history @handle")
        return
    handle = args[0]
    history = get_handle_history(handle)
    await update.message.reply_text(history)

async def fraud(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args or not args[0].startswith("@"):
        await update.message.reply_text("Usage: /fraud @handle")
        return
    handle = args[0]
    result = check_fraud(handle)
    await update.message.reply_text(result)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("worth", worth))
    app.add_handler(CommandHandler("analyze", analyze))
    app.add_handler(CommandHandler("claim", claim))
    app.add_handler(CommandHandler("suggest", suggest))
    app.add_handler(CommandHandler("history", history))
    app.add_handler(CommandHandler("fraud", fraud))
    print("Bot started. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()