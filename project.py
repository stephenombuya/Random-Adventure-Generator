import random
import os
from datetime import datetime

class AdventureAutomator:
    def __init__(self, log_directory='adventure_logs'):
        self.log_directory = log_directory
        os.makedirs(log_directory, exist_ok=True)

    def generate_adventure_scenario(self):
        """Creatively generates a unique adventure scenario."""
        locations = ['Misty Mountains', 'Forgotten Temple', 'Underwater Cave', 'Floating Islands']
        characters = ['Quantum Wizard', 'Cyber Ninja', 'Steampunk Detective', 'Cosmic Archaeologist']
        challenges = ['Solve an ancient riddle', 'Hack a sentient mainframe', 'Negotiate with time-traveling beings', 'Recover a quantum artifact']
        
        scenario = {
            'location': random.choice(locations),
            'protagonist': random.choice(characters),
            'mission': random.choice(challenges),
            'difficulty': random.randint(1, 10)
        }
        return scenario

    def log_adventure(self, scenario):
        """Logs the generated adventure scenario to a timestamped file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.log_directory, f'adventure_{timestamp}.txt')
        
        with open(filename, 'w') as log_file:
            log_file.write("🚀 ADVENTURE LOG 🚀\n")
            log_file.write(f"Location: {scenario['location']}\n")
            log_file.write(f"Protagonist: {scenario['protagonist']}\n")
            log_file.write(f"Mission: {scenario['mission']}\n")
            log_file.write(f"Difficulty: {scenario['difficulty']}/10\n")

    def automate_adventures(self, num_adventures=5):
        """Automatically generate and log multiple adventure scenarios."""
        for _ in range(num_adventures):
            scenario = self.generate_adventure_scenario()
            self.log_adventure(scenario)
            print(f"Generated adventure in {scenario['location']} for {scenario['protagonist']}")

def main():
    adventure_automator = AdventureAutomator()
    adventure_automator.automate_adventures()

if __name__ == "__main__":
    main()