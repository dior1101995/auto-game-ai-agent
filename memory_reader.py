import random

class MemoryReader:
    def read(self):
        #1 Fake dữ liệu memory (giả lập)
        
        return {
            "hp": random.randint(20, 100),
            "mana": random.randint(10, 100)
        }
