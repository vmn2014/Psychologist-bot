"""Prometheus metrics for bot monitoring."""

from prometheus_client import Counter, Histogram, Info, start_http_server

# Bot info
BOT_INFO = Info("psy_support_bot", "Bot information")

# Message counters
MESSAGES_TOTAL = Counter(
    "bot_messages_total",
    "Total messages processed",
    ["handler", "language"],
)

# Safety events
SAFETY_EVENTS_TOTAL = Counter(
    "bot_safety_events_total",
    "Total safety events",
    ["risk_level", "risk_type"],
)

# LLM calls
LLM_CALLS_TOTAL = Counter(
    "bot_llm_calls_total",
    "Total LLM API calls",
    ["model", "status"],
)

LLM_LATENCY = Histogram(
    "bot_llm_latency_seconds",
    "LLM API call latency",
    ["model"],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0],
)

# Mood entries
MOOD_ENTRIES_TOTAL = Counter(
    "bot_mood_entries_total",
    "Total mood entries created",
    ["mood_score"],
)

# Errors
ERRORS_TOTAL = Counter(
    "bot_errors_total",
    "Total errors",
    ["error_type"],
)

# Active users (gauge would need external storage)
ACTIVE_USERS = Counter(
    "bot_active_users_total",
    "Unique active users",
)


def start_metrics_server(port: int = 8000) -> None:
    """Start Prometheus metrics HTTP server."""
    start_http_server(port)
    print(f"Metrics server started on port {port}")


def record_message(handler: str, language: str) -> None:
    MESSAGES_TOTAL.labels(handler=handler, language=language).inc()


def record_safety_event(risk_level: int, risk_type: str) -> None:
    SAFETY_EVENTS_TOTAL.labels(risk_level=str(risk_level), risk_type=risk_type).inc()


def record_llm_call(model: str, status: str, latency: float) -> None:
    LLM_CALLS_TOTAL.labels(model=model, status=status).inc()
    LLM_LATENCY.labels(model=model).observe(latency)


def record_mood_entry(mood_score: int) -> None:
    MOOD_ENTRIES_TOTAL.labels(mood_score=str(mood_score)).inc()


def record_error(error_type: str) -> None:
    ERRORS_TOTAL.labels(error_type=error_type).inc()
