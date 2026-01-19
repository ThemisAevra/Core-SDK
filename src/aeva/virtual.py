import time
import random
import logging
from dataclasses import dataclass
from typing import List, Optional

# Setup Logging
logging.basicConfig(level=logging.INFO, format='[AEVA.CORE] %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Telemetry:
    position: List[float] # x, y, z
    battery: float
    status: str

class VirtualAgent:
    """
    A local simulation of an AEVA agent for development and testing.
    Does not require physical hardware.
    """
    def __init__(self, agent_id: str):
        self.id = agent_id
        self.position = [0.0, 0.0, 0.0]
        self.battery = 100.0
        self.status = "IDLE"
        logger.info(f"Initialized VirtualAgent<{self.id}>")

    def connect(self):
        """Simulate connection handshake."""
        logger.info("Connecting to local message bus...")
        time.sleep(0.5)
        logger.info("Connected. Heartbeat: 120Hz")
        return True

    def move_to(self, x: float, y: float, z: float):
        """Simulate physical movement with latency."""
        self.status = "MOVING"
        logger.info(f"Target received: [{x}, {y}, {z}]")
        logger.info("Computing Kinematics (RRT*)...")
        time.sleep(1.0) # Simulate computation
        
        steps = 5
        for i in range(steps):
            self.position[0] += (x - self.position[0]) / (steps - i)
            self.position[1] += (y - self.position[1]) / (steps - i)
            self.position[2] += (z - self.position[2]) / (steps - i)
            self.battery -= 0.1
            self._emit_telemetry()
            time.sleep(0.2)
            
        self.status = "IDLE"
        logger.info("Target Reached.")

    def run_vision_scan(self):
        """Simulate a Spatial-Net inference pass."""
        logger.info("Acquiring RGB-D Frame...")
        time.sleep(0.2)
        objects = ["Pallet", "Human", "Forklift"]
        detected = random.choice(objects)
        confidence = random.uniform(0.8, 0.99)
        logger.info(f"Spatial-Net Detection: '{detected}' ({confidence:.2f}%)")
        return {"object": detected, "confidence": confidence}

    def _emit_telemetry(self):
        t = Telemetry(self.position, self.battery, self.status)
        print(f"  >>> TELEMETRY: Pos={t.position} | Bat={t.battery:.1f}% | State={t.status}")

if __name__ == "__main__":
    # Self-test
    bot = VirtualAgent("sim-01")
    bot.connect()
    bot.move_to(1.5, 2.0, 0.0)
    bot.run_vision_scan()
