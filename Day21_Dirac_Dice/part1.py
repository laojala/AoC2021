class DiracDice:

    def __init__(self, players: dict):
        self.players = players  # dictionary containing list of ["position", "score"] for each player
        self.rounds = 0
        self.dice = 0
        self.dice_rolls = 0

    def print_players(self):
        print(f'round: {self.rounds}, {self.players}, {self.dice_rolls}')

    def turn(self, break_point):
        self.rounds += 1

        for p in self.players:
            self.dice_rolls += 3
            # count moves with arithmetic sum and set new dice position
            dice_at_start = self.dice + 1
            dice_at_stop = self.dice + 3
            self.dice = self.dice + 3
            steps = int(((dice_at_start + dice_at_stop) / 2) * 3)

            # set new position and count points
            position = self.players[p][0]

            remaining_steps = int(steps % 10)
            for step in range(remaining_steps):
                if position == 10:
                    position = 1
                else:
                    position += 1

            self.players[p][0] = position
            # add points
            self.players[p][1] += position

            if self.players[p][1] >= break_point:
                return False # do not continue playing
        return True

    def play_until(self, score):
        play = True
        while play:
            play = self.turn(score)

    def part1(self):
        return min(self.players["p1"][1], self.players["p2"][1]) * self.dice_rolls


participants = DiracDice({"p1": [8, 0], "p2": [4, 0]})

participants.play_until(1000)
part1 = participants.part1()
participants.print_players()
print(part1)
assert part1 == 504972
