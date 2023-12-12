from main import Roles
from main import Parties
from main import Policies
import player as player
import liberal as liberal
import fascist as fascist
import communist as communist

import random

PRESIDENT = 0
CHANCELLOR = 1

class Game:

    def __init__(self, player_roles, policies, board):
        # Game variables
        self.veto_power = False
        self.special_election = False
        self.third_fascist = False
        self.last_government = None
        self.current_government = [0, -1]
        self.government_failures = 0

        self.board = board # Keeps track of the board actions for each party
        self.enacted_policies = [0] * Parties.BOARD_PARTIES.value # keeps track of the number of policies played

        self.player_roles = player_roles.copy()
        self.create_players(player_roles)
        

        self.policy_deck = policies
        self.policy_discard = []
        random.shuffle(policies)
    

    def run(self):
        winner = Parties.No_Party
        
        while (winner == Parties.No_Party):
            #print("\nCurrent Board:", self.enacted_policies)
            #print([p.value for p in self.policy_deck])
            #print([p.value for p in self.policy_discard])
            #print(self.last_government, self.current_government)
            self.current_government[CHANCELLOR] = self.players[self.current_government[PRESIDENT]].choose_chancellor(self)
            #print(self.current_government[PRESIDENT], "is choosing", self.current_government[CHANCELLOR], "as chancellor.")
            #TODO: Implement voting

            if (self.third_fascist and self.players[self.current_government[CHANCELLOR]].role == Roles.Hitler):
                #print(self.current_government[CHANCELLOR], "is Hitler. Fascists win.")
                winner = Parties.Fascist
                return winner # May need to move this line in the future

            # Now presdient draws policies and then discards
            hand = [self.policy_deck.pop(), self.policy_deck.pop(), self.policy_deck.pop()]
            #print(hand)
            self.policy_discard.append(hand.pop(self.players[self.current_government[PRESIDENT]].discard_policy(self, hand)))
            #print(hand)
            #TODO: Handle chancellor play
            chancellor_action = self.players[self.current_government[CHANCELLOR]].enact_policy(self, hand)
            if (chancellor_action == -1):
                self.government_failures += 1
                if (self.government_failures == 3):
                    return Parties.Fascist
            else:
                enact = hand.pop(chancellor_action)
                self.enacted_policies[enact.value] += 1
                winner = self.board.enact_policy(self, enact, self.enacted_policies[enact.value] - 1)

            # Add remaining cards to discard
            self.policy_discard += hand

            #prepare the next government
            self.last_government = [self.current_government[PRESIDENT], self.current_government[CHANCELLOR]]
            
            self.current_government[CHANCELLOR] = -1
            self.current_government[PRESIDENT] += 1
            if (self.current_government[PRESIDENT] >= len(self.players)):
                self.current_government[PRESIDENT] = 0

            #TODO: Reshuffle discard pile if there are 2 or less cards in deck
            
            if (len(self.policy_deck) <= 2):
                self.policy_deck += self.policy_discard
                self.policy_discard = []
                random.shuffle(self.policy_deck)

        return winner
    
    def create_players(self, player_roles):
        random.shuffle(player_roles)
        self.players = [-1] * len(player_roles)
        for i in range(len(player_roles)):
            if (player_roles[i] == Roles.Liberal):
                self.players[i] = liberal.Liberal(i, Roles.Liberal, Parties.Liberal)
            if (player_roles[i] == Roles.Communist):
                self.players[i] = communist.Communist(i, Roles.Communist, Parties.Communist)
            else:
                self.players[i] = fascist.Fascist(i, player_roles[i], Parties.Fascist)

        for player in self.players:
            player.initialize_suspicions(self)

    # returns the player that was executed
    def execute_player(self, player):
        #print("Executing player", player)
        executed = self.players.pop(player)
        # Re order the players given one is eliminated
        for i in range(len(self.players)):
            self.players[i].index = i
        # re order current and last government
        for i in range(2):
            if (self.current_government[i] == player):
                self.current_government[i] = -1
            elif (self.current_government[i] > player):
                self.current_government[i] -= 1
            if (self.last_government[i] == player):
                self.last_government[i] = -1
            elif (self.last_government[i] > player):
                self.last_government[i] -= 1

        return executed