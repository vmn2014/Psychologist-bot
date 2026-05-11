"""LLM-based safety classification."""

import json
from typing import Any

from app.ai.openrouter_client import OpenRouterClient
from app.ai.prompts.safety_classifier_prompt import SAFETY_CLASSIFIER_PROMPT
from app.db.models import RiskLevel


class SafetyClassification:
    def __init__(self, data: dict[str, Any]) -> None:
        self.risk_level = RiskLevel(data.get("risk_level", 0))
        self.risk_type = data.get("risk_type", "none")
        self.confidence = data.get("confidence", 0.0)
        self.reason = data.get("reason", "")
        self.requires_crisis_response = data.get("requires_crisis_response", False)
        self.requires_professional_referral = data.get(
            "requires_professional_referral", False
        )


class SafetyClassifier:
    def __init__(self, client: OpenRouterClient) -> None:
        self.client = client

    async def classify(self, user_message: str, context: str = "") -> SafetyClassification:
        messages = [
            {"role": "system", "content": SAFETY_CLASSIFIER_PROMPT},
            {
                "role": "user",
                "content": f"Контекст: {context}\n\nСообщение пользователя: {user_message}",
            },
        ]

        response = await self.client.chat_completion(
            messages=messages,
            temperature=0.0,
            max_tokens=200,
            response_format={"type": "json_object"},
        )

        try:
            data = json.loads(response.content)
            return SafetyClassification(data)
        except (json.JSONDecodeError, KeyError, ValueError):
            # Fallback to safe classification
            return SafetyClassification(
                {
                    "risk_level": 2,
                    "risk_type": "unknown",
                    "confidence": 0.0,
                    "reason": "Failed to parse classifier response",
                    "requires_crisis_response": False,
                    "requires_professional_referral": True,
                }
            )
