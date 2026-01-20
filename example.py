import asyncio
from themisaevra.agent import HumanoidAgent, Task, SafetyLevel
from aeva.sim import IsaacConnector

async def main():
    # 1. Initialize the Agent
    # In a real scenario, this connects to the physical robot's onboard OS
    agent = HumanoidAgent(id="AEVA-7X", endpoint="localhost:50051")
    
    # 2. Connect to Simulation (Digital Twin)
    # This allows testing the mission in a safe virtual environment first
    sim_bridge = IsaacConnector(host="localhost")
    agent.attach_sim(sim_bridge)
    
    # 3. Define the Mission
    current_mission = Task(
        objective="Navigate to Sector 4 and inspect pressure valves.",
        constraints={
            "max_speed": 1.5,  # m/s
            "safety_mode": SafetyLevel.HIGH_PRECISION
        },
        timeout=600  # seconds
    )
    
    # 4. Connect and Deploy
    if agent.connect():
        print(f"Connected to {agent.id}")
        mission_id = agent.deploy(current_mission)
        print(f"Mission started with ID: {mission_id}")
        print("Monitoring telemetry...")
        
        # Simulate telemetry loop
        for i in range(5):
            print(f"[{i}s] Status: WORKING | Position: (12.4, 4.2) | Confidence: 99.8%")
            await asyncio.sleep(1)
            
        print("Mission Complete.")

if __name__ == "__main__":
    asyncio.run(main())
