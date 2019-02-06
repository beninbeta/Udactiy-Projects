#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def remember(self, my_move):
        pass


class RandomPlayer(Player):
        def move(self):
            return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        player_choice = input("What is your pick: ").lower()
        while player_choice not in moves:
            player_choice = input("Rock, paper, scissors only: ").lower()
        return player_choice


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def __init__(self):
        self.move_temp = random.choice(moves)

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        self.move_temp = their_move

    def remember(self, my_move):
        moves = []
        moves.append(my_move)
        return moves


class CyclePlayer(Player):
    def __init__(self):
        self.move_temp = random.choice(moves)
        self.moves = []

    def move(self):
        return self.move_temp

    def learn(self, my_move, their_move):
        # This is a much beter way to do this than what is asked for
        # Making it random instead of predetermined is better for play
        # while self.move_temp == my_move:
            # self.move_temp = random.choice(moves)
        # return self.move_temp
        if my_move == 'rock':
            self.move_temp = "paper"
        elif my_move == "paper":
            self.move_temp = "scissors"
        else:
            self.move_temp = "rock"
        return self.move_temp

    def remember(self, my_move):
        self.moves.append(my_move)
        return self.moves


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # self.rp = rp
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("It's a tie!")
        else:
            if beats(move1, move2):
                self.p1.score += 1
                print("P1 Wins!!!")
            else:
                self.p2.score += 1
                print("P2 Wins!!!")
        print(f"Current Score: P1: {self.p1.score} P2: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(self.p1.remember(move1))

    def play_game(self):
        print("Game start!")
        while True:
            try:
                games = int(input("How mnay games would you like to play? "))
                break
            except ValueError:
                print("Please enter a number.")
        for round in range(games):
            print(f"Round {round + 1}:")
            self.play_round(round + 1)
        if self.p1.score < self.p2.score:
            print(f"P2 wins {self.p2.score}:{self.p1.score}")
        elif self.p1.score > self.p2.score:
            print(f"P1 wins {self.p1.score}:{self.p2.score}")
        else:
            print(f"It's a tie P1 {self.p1.score}: p2 {self.p2.score}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()
