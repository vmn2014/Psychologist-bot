"""Main chat handler with safety checks."""

from aiogram import Router, types
from aiogram.filters import Command

from app.ai.openrouter_client import OpenRouterClient
from app.config import settings
from app.db.models import RiskLevel
from app.safety.crisis_detector import deterministic_crisis_check
from app.safety.safety_classifier import SafetyClassifier
from app.safety.safety_protocols import get_crisis_response

router = Router()


@router.message(Command("chat"))
async def cmd_chat(message: types.Message) -> None:
    await message.answer(
        "Я здесь. Расскажи, что у тебя на душе. Я выслушаю и помогу разобраться."
    )


@router.message()
async def handle_message(message: types.Message) -> None:
    if not message.text:
        return

    user_text = message.text.strip()

    # Step 1: Deterministic crisis check
    risk_level, pattern = deterministic_crisis_check(user_text)

    if risk_level >= RiskLevel.POSSIBLE_CRISIS:
        await message.answer(get_crisis_response(risk_level))
        return

    # Step 2: LLM safety classification (for non-obvious cases)
    client = OpenRouterClient()
    classifier = SafetyClassifier(client)

    try:
        classification = await classifier.classify(user_text)
        if classification.risk_level >= RiskLevel.POSSIBLE_CRISIS:
            await message.answer(get_crisis_response(classification.risk_level))
            await client.close()
            return
    except Exception:
        # If classifier fails, continue with normal flow but be cautious
        pass

    # Step 3: Normal support flow
    await message.chat.do_action("typing")

    try:
        response = await client.chat_completion(
            messages=[
                {"role": "system", "content": settings.default_model},
                {"role": "user", "content": user_text},
            ],
            temperature=0.4,
            max_tokens=700,
        )
        await message.answer(response.content)
    except Exception as e:
        await message.answer(
            "Извините, произошла ошибка при обработке запроса. "
            "Попробуйте позже или обратитесь за помощью."
        )
    finally:
        await client.close()
