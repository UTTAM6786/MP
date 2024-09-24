const TelegramBot = require('node-telegram-bot-api');

// Aapka Telegram Bot Token
const token = "7279522538:AAF93ENv251y8FmOicaelDyTELjCua-cbl4";

// Bot Create Karein
const bot = new TelegramBot(token, { polling: true });

// Auto Reaction Function
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    
    // Check karein agar message 'hello' shamil hai
    if (msg.text && msg.text.toLowerCase().includes('hello')) {
        // Reaction bhejain
        bot.sendMessage(chatId, '👋 Hello!'); // Auto Reaction Message
    }
});
