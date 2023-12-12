
class Board():

    def __init__(self, tracks):
        self.tracks = tracks

    def enact_policy(self, game, party, index):
        for track in self.tracks:
            if (track.party == party):
                return track.policy_actions[index](game)
            
        print("Board.py Error: No track for party", party)
        return -1