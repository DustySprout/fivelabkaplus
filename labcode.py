class RaceHorse:
    def __init__(self, name, speed, age):
        self.name = name
        self.speed = speed
        self.age = age
        self.placeInRace = None

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Speed: {self.speed}, Place: {self.placeInRace})"


class Race:
    def __init__(self):
        self.horses = []

    def add_horse(self, horse):
        if 3 <= horse.age <= 7:
            self.horses.append(horse)

    def remove_horse(self, horse):
        if horse in self.horses:
            self.horses.remove(horse)

    def find_winner(self):
        if not self.horses:
            return None

        avg_age = sum(horse.age for horse in self.horses) / len(self.horses)
        fastest_horse = max(self.horses, key=lambda horse: horse.speed)
        closest_to_avg_age_horses = sorted(
            self.horses,
            key=lambda horse: abs(horse.age - avg_age)
        )

        # Enumerate and assign places to the first three horses
        for i, horse in enumerate(closest_to_avg_age_horses[:3]):
            horse.placeInRace = i + 1

        return fastest_horse

    def sort_by_speed(self):
        self.horses.sort(key=lambda horse: horse.speed, reverse=True)

    def display_info(self):
        for horse in self.horses:
            print(horse)


def main():
    horse1 = RaceHorse("Жозеф", 40, 4)
    horse2 = RaceHorse("Микола", 50, 5)
    horse3 = RaceHorse("Море", 45, 6)
    horse4 = RaceHorse("Форта", 60, 3)
    horse5 = RaceHorse("Каму", 55, 7)

    race = Race()
    race.add_horse(horse1)
    race.add_horse(horse2)
    race.add_horse(horse3)
    race.add_horse(horse4)
    race.add_horse(horse5)

    print("Учасники гонки:")
    race.display_info()

    race.sort_by_speed()
    print("\nСортування по швидкості:")
    race.display_info()

    winner = race.find_winner()
    print("\nНайшвидший кінь:", winner.name)

    print("\nРезультати гонки:")
    race.display_info()


if __name__ == "__main__":
    main()


