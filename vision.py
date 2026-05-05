import random

class VisionSystem:
    def capture(self):
        # Fake CV detection
        return {
            "enemy": random.choice([True, False])
        }