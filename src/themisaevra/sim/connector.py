class SimConnector:
    """Base class for simulation bridges."""
    def __init__(self):
        pass

    def sync_physics(self, frequency: int = 60):
        pass

class IsaacConnector(SimConnector):
    """Bridge for NVIDIA Isaac Sim."""
    def __init__(self, host: str = "localhost", port: int = 8888):
        super().__init__()
        print("Initializing AEVA <-> Isaac Sim Bridge")

class GazeboConnector(SimConnector):
    """Bridge for Gazebo."""
    def __init__(self, master_uri: str):
        super().__init__()
        print("Initializing AEVA <-> ROS 2 / Gazebo Bridge")
