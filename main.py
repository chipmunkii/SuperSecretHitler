from enum import Enum
import game
import board
import track

class Roles(Enum):
    Hitler = 0
    Fascist = 1
    Liberal = 2
    Communist = 3
    total = 3
    def __eq__(self, other):
        return self.value == other.value

class Parties(Enum):
    No_Party = -1
    Fascist = 0
    Liberal = 1
    Communist = 2
    BOARD_PARTIES = 3
    total = 3
    def __eq__(self, other):
        return self.value == other.value

class Policies(Enum):
    Fascist = Parties.Fascist.value
    Liberal = Parties.Liberal.value
    Communist = Parties.Communist.value
    total = 2
    def __eq__(self, other):
        return self.value == other.value

import track_actions as ta

def main():

    # Create decks
    standard_deck = [Policies.Fascist] * 11 + [Policies.Liberal] * 6 #+ [Policies.Communist] * 8
    
    # Create Tracks
    fascist_5p = track.Track(Parties.Fascist, [ta.fascist_play, ta.fascist_play, ta.third_fascist, ta.fascist_bullet, ta.fascist_bullet_veto, ta.fascist_win])
    liberal_track = track.Track(Parties.Liberal, [ta.liberal_play, ta.liberal_play, ta.liberal_play, ta.liberal_play, ta.liberal_win])
    communist_5p = track.Track(Parties.Communist, [ta.communist_play, ta.communist_convert, ta.five_year_plan, ta.communist_play, ta.communist_win])

    # Create Boards
    standard_5p_lf = board.Board([fascist_5p, liberal_track]) #standard 5 player board liberal/fascist
    #g = game.Game([Roles.Liberal, Roles.Liberal, Roles.Liberal, Roles.Liberal, Roles.Liberal], standard_deck, standard_5p_lf)
    wins = [0] * Parties.total.value
    for i in range(1000):
        g = game.Game([Roles.Hitler, Roles.Fascist, Roles.Liberal, Roles.Liberal, Roles.Liberal], standard_deck.copy(), standard_5p_lf)
        wins[g.run().value] += 1
    print_results(wins)
    

def print_results(wins):
    if (wins[Parties.Fascist.value] != 0):
        print("Fascist wins:", wins[Parties.Fascist.value])
    if (wins[Parties.Liberal.value] != 0):
        print("Liberal wins:", wins[Parties.Liberal.value])
    if (wins[Parties.Communist.value] != 0):
        print("Communist wins:", wins[Parties.Communist.value])


if __name__ == "__main__":
    main()