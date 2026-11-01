class VacuumAgent:
    def __init__(self):
        self.location = 'A'

    def act(self, status):
        if status == 'Dirty':
            return 'Suck'
        return 'Right' if self.location == 'A' else 'Left'


class VacuumEnvironment:
    def __init__(self):
        self.states = {
            'A': input("Enter status of A (Dirty/Clean): "),
            'B': input("Enter status of B (Dirty/Clean): ")
        }

    def run(self, agent, steps=4):
        print("\nInitial State:", self.states)

        for i in range(1, steps + 1):
            status = self.states[agent.location]
            action = agent.act(status)

            print(f"Step {i}: {agent.location}, {status} -> {action}")

            if action == 'Suck':
                self.states[agent.location] = 'Clean'
            else:
                agent.location = 'B' if action == 'Right' else 'A'

        print("\nFinal State:", self.states)


agent = VacuumAgent()
environment = VacuumEnvironment()
environment.run(agent)
