"""Start handler with consent flow."""

from aiogram import Router, types
from aiogram.filters import Command

from app.bot.handlers.i18n import get_text, get_user_language
from app.config import settings

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    lang = get_user_language(message.from_user)

    start_text = (
        f"{get_text('start.greeting', lang)}\n\n"
        f"{get_text('start.capabilities', lang)}\n\n"
        f"{get_text('start.disclaimer', lang)}\n\n"
        f"{get_text('start.crisis_warning', lang)}\n\n"
        f"{get_text('start.consent', lang)}"
    )

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text=get_text("start.buttons.continue", lang),
                    callback_data="consent_agree",
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("start.buttons.crisis", lang),
                    callback_data="crisis_help",
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("start.buttons.privacy", lang),
                    callback_data="privacy_policy",
                )
            ],
        ]
    )
    await message.answer(start_text, reply_markup=keyboard)


@router.callback_query(lambda c: c.data == "consent_agree")
async def on_consent_agree(callback: types.CallbackQuery) -> None:
    lang = get_user_language(callback.from_user)
    await callback.message.edit_text(
        get_text("start.thanks", lang, default="Спасибо за доверие. Выбери, с чего начнём:"),
        reply_markup=main_menu_keyboard(lang),
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "crisis_help")
async def on_crisis_help(callback: types.CallbackQuery) -> None:
    lang = get_user_language(callback.from_user)
    await callback.message.edit_text(
        "🆘 " + get_text("crisis.response", lang),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="🔙 " + get_text("menu.back", lang, default="Назад"),
                        callback_data="back_to_start",
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


def main_menu_keyboard(lang: str = "en") -> types.InlineKeyboardMarkup:
    return types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.chat", lang), callback_data="mode_chat"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.anxiety", lang), callback_data="mode_anxiety"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.sad", lang), callback_data="mode_sad"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.mood", lang), callback_data="mode_mood"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.exercises", lang), callback_data="mode_exercises"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.safety_plan", lang), callback_data="safety_plan"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text=get_text("menu.settings", lang), callback_data="settings"
                )
            ],
        ]
    )
