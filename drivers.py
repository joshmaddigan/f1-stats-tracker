from f1_api import get_session

class Driver:
    def __init__(self, name, points=0, team=None, wins=0, podiums=0, poles=0, laps_led=0):
        self.name = name
        self.points = points
        self.team = team
        self.wins = wins
        self.podiums = podiums
        self.poles = poles
        self.laps_led = laps_led

    def __str__(self):
        return f"Driver: {self.name}, Team: {self.team}, Points: {self.points}, Wins: {self.wins}, Podiums: {self.podiums}, Poles: {self.poles}, Laps Led: {self.laps_led}"
        

session = get_session(2026, 'Miami', 'R')
print(session.results[['Abbreviation', 'Position', 'GridPosition', 'Points', 'Laps']])

#         ## Drivers ##
# Lewis_Hamilton = Driver("Lewis Hamilton", points=290, team="Mercedes", wins=2, podiums=7, poles=2, laps_led=258)

# print(Lewis_Hamilton)