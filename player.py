from main import Roles
from main import Parties
from main import Policies
import random

class Player:

    def __init__(self, index, role, party):
        self.name = "Player 1"
        self.index = index
        self.role = role
        self.party = party

        # Predictions of who has what role
        self.predictions = []

        # Biases on how people have played
        self.suspicions = []

    def initialize_suspicions(self, game):
        self.predictions = [[0] * len(game.player_roles)] * len(game.player_roles)
        ratio = 1 / len(game.player_roles)
        for p in range(len(game.players)):
            for r in range(len(game.player_roles)):
                self.predictions[p][r] = ratio
                
        self.suspicions = [[0] * len(game.player_roles)] * len(game.player_roles)
        
        # Apply own role to predictions


    #returns the index of the policy to discard as president
    def discard_policy(self, game, policies):
        return random.randint(0,2)
    
    # returns the index of the policy to enact as chancellor
    def enact_policy(self, game, policies):
        return random.randint(0,1)

    # returns 1 to vote yes, otherwise returns 0
    def get_vote(self, game, chancellor):
        return 1
    
    # returns the index of the player to be chancellor player array in game
    def choose_chancellor(self, game):
        options = list(range(len(game.players)))
        #remove current player and last government from chancellor options
        options.remove(self.index)
        if (game.last_government != None):
            if (game.last_government[0] != self.index and game.last_government[0] != -1 and len(game.players) > 4):
                options.remove(game.last_government[0] )
            if (game.last_government[1] != self.index and game.last_government[1] != -1 and len(game.players) > 3):
                options.remove(game.last_government[1] )
        #print("Players", len(game.players), "last government", game.last_government)
        #print("Chancellor options:", options)
        return options[random.randint(0, len(options) - 1)]
    
    def choose_execution(self, game):
        options = list(range(len(game.players)))
        #remove current player and last government from chancellor options
        options.remove(self.index)
        # Choose a random player
        return options[random.randint(0, len(options) - 1)]
    
    def accept_veto(self, game, policies):
        return True