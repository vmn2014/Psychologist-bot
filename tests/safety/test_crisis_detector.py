"""Tests for crisis detector."""

import pytest

from app.db.models import RiskLevel
from app.safety.crisis_detector import deterministic_crisis_check


@pytest.mark.parametrize(
    "text,expected_level",
    [
        ("Я хочу умереть", RiskLevel.IMMINENT_RISK),
        ("У меня есть план покончить с собой", RiskLevel.IMMINENT_RISK),
        ("Я выпил таблеток", RiskLevel.IMMINENT_RISK),
        ("Не хочу жить", RiskLevel.POSSIBLE_CRISIS),
        ("Мне грустно", RiskLevel.NO_RISK),
        ("Я прокрастинирую", RiskLevel.NO_RISK),
    ],
)
def test_crisis_detection(text: str, expected_level: RiskLevel) -> None:
    level, _ = deterministic_crisis_check(text)
    assert level == expected_level
