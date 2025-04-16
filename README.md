# Namaz Time Bot

Bu loyiha Telegram bot bo'lib, foydalanuvchilarga namoz vaqtlarini ko'rsatib beradi. Bot foydalanuvchilarning joylashuviga qarab namoz vaqtlarini aniqlaydi va ularga qulay interfeys orqali ma'lumotlarni taqdim etadi.

## Xususiyatlari
- Namoz vaqtlarini aniqlash.
- Foydalanuvchining joylashuvini avtomatik aniqlash yoki qo'lda kiritish.
- Har bir namoz vaqti uchun eslatma o'rnatish.
- Oddiy va qulay foydalanish interfeysi.

## O'rnatish va Ishlatish

### Talablar
- Python 3.8 yoki undan yuqori versiya.
- Quyidagi kutubxonalar o'rnatilgan bo'lishi kerak:
    - `python-telegram-bot`
    - `requests`
    - `pytz`

### O'rnatish
1. Loyihani klonlang:
     ```bash
     git clone https://github.com/username/namaz-time-bot.git
     cd namaz-time-bot
     ```

2. Virtual muhit yarating va faollashtiring:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # Windows uchun: venv\Scripts\activate
     ```

3. Talab qilinadigan kutubxonalarni o'rnating:
     ```bash
     pip install -r requirements.txt
     ```

4. `.env` faylini yarating va Telegram bot tokenini qo'shing:
     ```env
     BOT_TOKEN=your_telegram_bot_token
     ```

### Ishga tushirish
1. Botni ishga tushiring:
     ```bash
     python bot.py
     ```

2. Telegram orqali botga yozing va foydalanishni boshlang.

## Foydalanish
1. Botni ishga tushirgandan so'ng, Telegram orqali botga `/start` buyrug'ini yuboring.
2. Joylashuvingizni yuboring yoki qo'lda kiritib, namoz vaqtlarini oling.
3. Eslatmalarni sozlash uchun botning ko'rsatmalariga amal qiling.

## Hissa qo'shish
1. Loyihani fork qiling.
2. O'zingizning o'zgartirishlaringizni qiling.
3. Pull request yuboring.

## Litsenziya
Ushbu loyiha [MIT](LICENSE) litsenziyasi ostida tarqatiladi.

## Muallif
Loyihaning muallifi: Abdurazzoq