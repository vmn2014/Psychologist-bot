"""Deterministic crisis detection with keyword matching."""

import re

from app.db.models import RiskLevel

# Level 4 triggers - imminent risk
LEVEL_4_PATTERNS = [
    r"\bхочу умереть\b",
    r"\bхочу покончить с собой\b",
    r"\bсобираюсь умереть\b",
    r"\bпланирую суицид\b",
    r"\bу меня есть план\b.*\b(умереть|покончить|свой)\b",
    r"\bсейчас убью\b",
    r"\bсейчас покончу\b",
    r"\bпередозировка\b",
    r"\bвыпил таблеток\b",
    r"\bперерезать вены\b",
    r"\bпрыгнуть с\b",
    r"\bповешусь\b",
    r"\bубью человека\b",
    r"\bхочу убить\b",
    r"\bголоса говорят\b.*\b(убей|умри|сделай)\b",
    r"\bменя контролируют\b.*\b(убить|навредить)\b",
]

# Level 3 triggers - possible crisis
LEVEL_3_PATTERNS = [
    r"\bне хочу жить\b",
    r"\bне вижу смысла жить\b",
    r"\bлучше бы я умер\b",
    r"\bвсе было бы лучше без меня\b",
    r"\bсамоповреждение\b",
    r"\bрежу себя\b",
    r"\bбью себя\b",
    r"\bпаническая атака\b",
    r"\bне могу дышать\b.*\b(паника|страх)\b",
    r"\bменя преследуют\b",
    r"\bза мной следят\b",
    r"\bменя отравляют\b",
    r"\bне сплю [0-9]+ дней\b",
    r"\bбез сна [0-9]+ дней\b",
    r"\bменя бьют\b",
    r"\bменя избивают\b",
    r"\bнасилие дома\b",
    r"\bизнасиловани[ея]\b",
    r"\bдомашнее насилие\b",
]


def deterministic_crisis_check(text: str) -> tuple[RiskLevel, str | None]:
    """Check text for crisis indicators. Returns (risk_level, matched_pattern)."""
    text_lower = text.lower()

    for pattern in LEVEL_4_PATTERNS:
        if re.search(pattern, text_lower):
            return RiskLevel.IMMINENT_RISK, pattern

    for pattern in LEVEL_3_PATTERNS:
        if re.search(pattern, text_lower):
            return RiskLevel.POSSIBLE_CRISIS, pattern

    return RiskLevel.NO_RISK, None
