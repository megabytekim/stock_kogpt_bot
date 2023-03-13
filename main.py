from telegram import Update
from telegram.ext import Application, ContextTypes, CommandHandler


class BuiltInTelegramBot:
    def __init__(self, token):
        self.token = token
        self.application = Application.builder().token(token).build()
        self.add_handlers()

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Hello and welcome to the BuiltIn Telegram bot!'
        )

    @staticmethod
    async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="""
         The BuiltIn Telegram bot supports the following commands:
          - /start: Welcoming users
          - /help: List of supported commands (you are here)
          - /first_name: Reports the user's first name
          - /last_name: Reports the user's last name
         """
        )

    def add_handlers(self):
        start_handler = CommandHandler('start', self.start)
        help_handler = CommandHandler('help', self.help)
        self.application.add_handler(start_handler)
        self.application.add_handler(help_handler)

    def run(self):
        self.application.run_polling()


if __name__ == '__main__':
    with open("./token.txt") as f:
        lines = f.readlines()
        token = lines[0].strip()
    bot = BuiltInTelegramBot(token)
    bot.run()


