"""Mood diary handler."""

from aiogram import Router, types
from aiogram.filters import Command

from app.bot.handlers.i18n import get_text, get_user_language

router = Router()


@router.message(Command("mood"))
async def cmd_mood(message: types.Message) -> None:
    lang = get_user_language(message.from_user)
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text=get_text("mood.levels.5", lang), callback_data="mood_5")],
            [types.InlineKeyboardButton(text=get_text("mood.levels.4", lang), callback_data="mood_4")],
            [types.InlineKeyboardButton(text=get_text("mood.levels.3", lang), callback_data="mood_3")],
            [types.InlineKeyboardButton(text=get_text("mood.levels.2", lang), callback_data="mood_2")],
            [types.InlineKeyboardButton(text=get_text("mood.levels.1", lang), callback_data="mood_1")],
        ]
    )
    await message.answer(get_text("mood.question", lang), reply_markup=keyboard)


@router.callback_query(lambda c: c.data.startswith("mood_"))
async def on_mood_selected(callback: types.CallbackQuery) -> None:
    lang = get_user_language(callback.from_user)
    mood = int(callback.data.split("_")[1])
    mood_label = get_text(f"mood.levels.{mood}", lang)
    await callback.message.edit_text(
        get_text("mood.saved", lang, mood=mood_label)
    )
    await callback.answer()
