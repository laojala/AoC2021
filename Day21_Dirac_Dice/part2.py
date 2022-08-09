
class Wins:
    def __init__(self):
        self.P1 = 0
        self.P2 = 0

    def P1_wins(self):
        self.P1 += 1

    def P2_wins(self):
        self.P2 += 1

    def __repr__(self):
        return f"P1 wins: {self.P1}, P2 wins: {self.P2}"


class DiracDice:

    def __init__(self, players: dict, wins: Wins, rolls=0, next_roll=0):
        self.players = players  # dictionary containing list of ["position", "score"] for each player
        self.wins = wins
        self.rolls = rolls  # counter for rolls in a round
        self.next_roll = next_roll  # dice value at next roll

    def print_players(self):
        print(f"{self.players}, {self.wins}")

    def add_step_and_points(self, p,steps):
        position = self.players[p][0]

        for step in range(steps):
            if position == 10:
                position = 1
            else:
                position += 1

        self.players[p][0] = position
        # add points
        self.players[p][1] += position

    def turn(self, break_point):

        for p in self.players:

            rolls = self.rolls+1


            DiracDice(self.players.copy(), self.wins, rolls, 1).play_until(21)
            DiracDice(self.players.copy(), self.wins, rolls, 2).play_until(21)
            DiracDice(self.players.copy(), self.wins, rolls, 3).play_until(21)

            step = self.next_roll

            self.add_step_and_points(p,step)

            round_finished = False
            if self.rolls == 3:
                round_finished = True
                self.rolls = 0

            if round_finished and self.players[p][1] >= break_point:
                return False    # do not continue playing if not winning

            if self.next_roll == 0:
                self.print_players()
                exit()

        return True

    def set_winner(self):
        if self.players["p1"][1] > self.players["p2"][1]:
            self.wins.P1_wins()
        else:
            self.wins.P2_wins()

    def play_until(self, score=21):
        play = True
        while play:
            play = self.turn(score)
        self.set_winner()


win_counter = Wins()
participants = DiracDice({"p1": [8, 0], "p2": [4, 0]}, win_counter)
participants.print_players()
participants.play_until(21)
participants.print_players()


