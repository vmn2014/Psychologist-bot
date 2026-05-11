"""Mood diary handler."""

from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("mood"))
async def cmd_mood(message: types.Message) -> None:
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="😊 Отлично", callback_data="mood_5")],
            [types.InlineKeyboardButton(text="🙂 Хорошо", callback_data="mood_4")],
            [types.InlineKeyboardButton(text="😐 Нормально", callback_data="mood_3")],
            [types.InlineKeyboardButton(text="😕 Не очень", callback_data="mood_2")],
            [types.InlineKeyboardButton(text="😢 Плохо", callback_data="mood_1")],
        ]
    )
    await message.answer("📊 Как ты себя чувствуешь сейчас?", reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith("mood_"))
async def on_mood_selected(callback: types.CallbackQuery) -> None:
    mood = int(callback.data.split("_")[1])
    labels = {
        5: "Отлично 😊",
        4: "Хорошо 🙂",
        3: "Нормально 😐",
        2: "Не очень 😕",
        1: "Плохо 😢",
    }
    await callback.message.edit_text(
        f"✅ Записано: {labels[mood]}\n\n"
        f"Спасибо за отметку! Отслеживание настроения помогает замечать паттерны.\n\n"
        f"Хочешь добавить заметку о том, что влияет на твоё состояние?"
    )
    await callback.answer()
