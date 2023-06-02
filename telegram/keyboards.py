from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Create the main keyboard with ℹ️Info and 🚫 Ban control buttons
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('ℹ️Info'))
# keyboard.add(KeyboardButton('🚫 Ban control'))

# Create the ban control keyboard with 🟢 ON, 🔴 OFF, and 🔙 Back buttons
ban_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
ban_keyboard.add(KeyboardButton('🟢 ON'), KeyboardButton('🔴 OFF'))
ban_keyboard.add(KeyboardButton('🔙 Back'))
# Info keyboard with *️⃣ Summary and 🪪 Licenses buttons and 🔙 Back button
# info_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# info_keyboard.add
# (KeyboardButton('*️⃣ Summary'), KeyboardButton('🪪 Licenses'))
# info_keyboard.add(KeyboardButton('🔙 Back'))
