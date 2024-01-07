"""
This is a labb 5
"""
class RaceHorse:
    """
    Class a racehorse

    Attributes:
    - name (str): The name of the horse.
    - speed (int): The speed of the horse.
    - age (int): The age of the horse.
    - place_in_race (int): The place of the horse in the race.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, name, speed, age):
        self.name = name
        self.speed = speed
        self.age = age
        self.place_in_race = None

    def __str__(self):
        """
        String of the RaceHorse obj.
        """
        return f"{self.name} (Age: {self.age}, Speed: {self.speed}, Place: {self.place_in_race})"


class Race:
    """
    Class a race.

    with attributes
    - horses (list): List of RaceHorse.
    """

    def __init__(self):
        self.horses = []

    def add_horse(self, horse):
        """
        Adding horses meeting the
        age criteria below.
        """
        if 3 <= horse.age <= 7:
            self.horses.append(horse)

    def remove_horse(self, horse):
        """
        Remove horses from the race.
        """
        if horse in self.horses:
            self.horses.remove(horse)

    def find_winner(self):
        """
        Finding the winner basing on who is the fastest horse
        and who is closest to the average age.
        """
        if not self.horses:
            return None

        avg_age = sum(horse.age for horse in self.horses) / len(self.horses)
        fastest_horse = max(self.horses, key=lambda horse: horse.speed)
        closest_to_avg_age_horses = sorted(
            self.horses,
            key=lambda horse: abs(horse.age - avg_age)
        )

        for i, horse in enumerate(closest_to_avg_age_horses[:3]):
            horse.place_in_race = i + 1

        return fastest_horse

    def sort_by_speed(self):
        """
        Sort the horses by their speed in sorted order.
        """
        self.horses.sort(key=lambda horse: horse.speed, reverse=True)

    def display_info(self):
        """
        Displaying horzes information.
        """
        for horse in self.horses:
            print(horse)


def main():
    """
       Main function demonstrating the Race and RaceHorse classes.
    """
    horse1 = RaceHorse("Жозеф", 40, 7)
    horse2 = RaceHorse("Микола", 50, 5)
    horse3 = RaceHorse("Море", 62, 6)
    horse4 = RaceHorse("Форта", 58, 5)
    horse5 = RaceHorse("Bomax", 55, 5)

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
