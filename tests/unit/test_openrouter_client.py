"""Tests for OpenRouter client."""

import pytest

from app.ai.openrouter_client import OpenRouterClient


@pytest.mark.asyncio
async def test_healthcheck() -> None:
    client = OpenRouterClient()
    result = await client.healthcheck()
    assert isinstance(result, bool)
    await client.close()
