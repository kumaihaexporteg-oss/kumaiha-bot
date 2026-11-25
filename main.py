import os
import telebot
import smtplib
from email.mime.text import MIMEText

BOT_TOKEN = os.getenv("BOT_TOKEN")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا بيك في KUMAIHA Export Bot 🔥\n\nعشان تبعت ايميل ابعت:\n\n/send الايميل | الموضوع | الرسالة\n\nمثال:\n/send test@gmail.com | اهلا | دي رسالة تجريبية")

@bot.message_handler(commands=['send'])
def send_email(message):
    try:
        text = message.text.replace('/send ', '')
        to_email, subject, body = text.split('|')
        msg = MIMEText(body.strip())
        msg['Subject'] = subject.strip()
        msg['From'] = YOUR_EMAIL
        msg['To'] = to_email.strip()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(YOUR_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        bot.reply_to(message, "✅ اتبعت بنجاح لـ " + to_email.strip())
    except:
        bot.reply_to(message, "❌ غلط في الصيغة، ابعت زي كده:\n/send test@gmail.com | الموضوع | الرسالة")

print("البوت شغال...")
bot.polling()
