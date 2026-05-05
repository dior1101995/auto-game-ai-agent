from vision import VisionSystem
from memory_reader import MemoryReader
from controller import Controller

class GameAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.vision = VisionSystem()
        self.memory = MemoryReader()
        self.controller = Controller()

    def analyze_state(self):
        screen_data = self.vision.capture()
        memory_data = self.memory.read()

        state = {
            "enemy_detected": screen_data.get("enemy", False),
            "hp": memory_data.get("hp", 100)
        }
        return state

    def decide_action(self, state):
        # Multi-step reasoning đơn giản
        if state["hp"] < 30:
            return "heal"
        elif state["enemy_detected"]:
            return "attack"
        else:
            return "move"

    def execute1(self, action):
        if action == "attack":
            self.controller.attack()
        elif action == "move":
            self.controller.move()
        elif action == "heal":
            self.controller.heal()
    def execute(self, action):
        if action == "attack":
            self.controller.attack()
        elif action == "move":
            self.controller.move()
        elif action == "heal":
            self.controller.heal()
    def run_step(self):
        state = self.analyze_state()
        action = self.decide_action(state)
        self.execute(action)

        print(f"[AGENT-{self.agent_id}] Action: {action} | HP: {state['hp']}")
