from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, Optional

class SafetyLevel(Enum):
    STANDARD = auto()
    HIGH_PRECISION = auto()
    HUMAN_COLLABORATIVE = auto()
    EMERGENCY_STOP = auto()

class AgentStatus(Enum):
    IDLE = "IDLE"
    WORKING = "WORKING"
    PLANNING = "PLANNING"
    ERROR = "ERROR"

@dataclass
class Task:
    """
    Represents a discrete mission for an agent.
    """
    objective: str
    constraints: Dict[str, Any] = field(default_factory=dict)
    timeout: int = 300
    priority: int = 1

@dataclass
class Telemetry:
    """
    Real-time status update from an agent.
    """
    status: AgentStatus
    position: tuple
    battery: float
    ai_confidence: float
