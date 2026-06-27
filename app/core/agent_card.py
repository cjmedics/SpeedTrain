import json
from functools import lru_cache
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
AGENT_CARD_PATH = PROJECT_ROOT / "croo-agent.json"


@lru_cache
def load_agent_card() -> dict:
    with AGENT_CARD_PATH.open(encoding="utf-8") as file:
        return json.load(file)

