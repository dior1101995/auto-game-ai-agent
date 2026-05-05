import time
from agent import GameAgent
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def main():
    config = load_config()
    agents = []

    for i in range(config["num_agents"]):
        agent = GameAgent(agent_id=i)
        agents.append(agent)

    print("[SYSTEM] Starting all agents...")

    while True:
        for agent in agents:
            agent.run_step()
        time.sleep(0.4)

if __name__ == "__main__":
    main()
