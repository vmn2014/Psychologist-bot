"""Safety protocols and crisis responses."""

from app.db.models import RiskLevel


CRISIS_RESPONSE_TEMPLATE = """Похоже, сейчас может быть небезопасный момент. Я не могу заменить экстренную помощь, но могу быть рядом в переписке.

Пожалуйста, сделай сейчас 3 вещи:
1. Позвони в местную экстренную службу или кризисную линию.
2. Напиши или позови человека рядом: "Мне сейчас небезопасно одному, побудь со мной".
3. Отложи подальше всё, чем можно себе навредить.

Ответь одним словом: ты сейчас один/одна?"""

ELEVATED_DISTRESS_RESPONSE = """Я слышу, что тебе очень тяжело. Это важно и серьёзно.

Я могу помочь с маленькими шагами прямо сейчас, но если тебе плохо уже долго или становится хуже, пожалуйста, обратись к специалисту.

Хочешь, сделаем одно короткое упражнение для стабилизации?"""


def get_crisis_response(risk_level: RiskLevel, lang: str = "en") -> str:
    """Get crisis response in user's language."""
    from app.bot.handlers.i18n import get_text

    if risk_level == RiskLevel.IMMINENT_RISK:
        return get_text("crisis.response", lang)
    elif risk_level == RiskLevel.POSSIBLE_CRISIS:
        return get_text("crisis.elevated", lang)
    return ""


def get_safety_plan_template(lang: str = "en") -> str:
    """Get safety plan template in user's language."""
    from app.bot.handlers.i18n import get_text

    title = get_text("safety_plan.title", lang)
    items = get_text("safety_plan.items", lang)
    start = get_text("safety_plan.start_filling", lang)

    if isinstance(items, list):
        items_text = "\n".join(items)
    else:
        items_text = str(items)

    return f"{title}\n\n{items_text}\n\n{start}"
