from main import Policies
import player

class Fascist(player.Player):

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
        return 1