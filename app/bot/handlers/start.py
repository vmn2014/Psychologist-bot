"""Start handler with consent flow."""

from aiogram import Router, types
from aiogram.filters import Command

from app.config import settings

router = Router()

START_TEXT = f"""Привет. Я {settings.bot_display_name} — AI-помощник для психологической самопомощи и эмоциональной поддержки.

Я могу помочь:
— разобраться в эмоциях и мыслях
— снизить стресс
— сделать CBT/DBT/mindfulness-упражнение
— вести дневник состояния
— составить маленький план действий

Я не врач, не психотерапевт и не кризисная служба. Я не ставлю диагнозы и не назначаю лечение.

Если тебе сейчас небезопасно или есть мысли причинить вред себе/другим, нужно обратиться в экстренную службу, кризисную линию или к человеку рядом.

Продолжая, ты подтверждаешь, что понимаешь эти ограничения."""

CRISIS_BUTTON_TEXT = "🆘 Мне нужна срочная помощь"
CONTINUE_BUTTON_TEXT = "✅ Понимаю, продолжить"
PRIVACY_BUTTON_TEXT = "🔒 Политика приватности"


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text=CONTINUE_BUTTON_TEXT, callback_data="consent_agree"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=CRISIS_BUTTON_TEXT, callback_data="crisis_help"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=PRIVACY_BUTTON_TEXT, callback_data="privacy_policy"
                )
            ],
        ]
    )
    await message.answer(START_TEXT, reply_markup=keyboard)


@router.callback_query(lambda c: c.data == "consent_agree")
async def on_consent_agree(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(
        "Спасибо за доверие. Выбери, с чего начнём:",
        reply_markup=main_menu_keyboard(),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "crisis_help")
async def on_crisis_help(callback: types.CallbackQuery) -> None:
    await callback.message.edit_text(
        "🆘 Если тебе сейчас небезопасно:\n\n"
        "1. Позвони в экстренную службу: 112\n"
        "2. Кризисная линия: 8-800-2000-122\n"
        "3. Напиши или позови человека рядом\n\n"
        "Ты не один. Помощь есть.",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="🔙 Вернуться", callback_data="back_to_start"
                    )
                ]
            ]
        ),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "back_to_start")
async def on_back_to_start(callback: types.CallbackQuery) -> None:
    await cmd_start(callback.message)
    await callback.answer()


def main_menu_keyboard() -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="🗣 Поговорить", callback_data="mode_chat")],
            [
                types.InlineKeyboardButton(
                    text="😰 Мне тревожно", callback_data="mode_anxiety"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="😔 Мне грустно", callback_data="mode_sad"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="📝 Дневник настроения", callback_data="mode_mood"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="🧘 Упражнения", callback_data="mode_exercises"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="📋 План безопасности", callback_data="safety_plan"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="⚙️ Настройки", callback_data="settings"
                )
            ],
        ]
    )
