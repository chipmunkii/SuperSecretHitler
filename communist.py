from main import Policies
import player

class Communist(player.Player):

    #returns the index of the policy to discard as president
    def discard_policy(self, game, policies):
        #print(policies)
        if (policies[0] == Policies.Liberal):
            return 0
        if (policies[1] == Policies.Liberal):
            return 1
        return 2
    
    # returns the index of the policy to enact as chancellor
    def enact_policy(self, game, policies):
        #print(policies)
        if (policies[0] == Policies.Liberal):
            return 0
        if (game.veto_power == False or policies[1] == Policies.Liberal):
            return 1
        if (game.players[game.current_government[0]].accept_veto(game, policies)):
            return -1
        return 1