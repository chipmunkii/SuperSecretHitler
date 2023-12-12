from main import Parties, Roles, Policies
import random
import communist

# Policy functions
def third_fascist(game):
    #print("Playing fascist policy", game.enacted_policies[Parties.Fascist.value])
    #print("The fascists now win if hitler becomes chancellor")
    game.third_fascist = True
    return Parties.No_Party

def fascist_play(game):
    #print("Playing fascist policy", game.enacted_policies[Parties.Fascist.value])
    return Parties.No_Party

def fascist_bullet(game):
    #print("Playing fascist policy", game.enacted_policies[Parties.Fascist.value])
    #print("The president must now execute a player")
    victim = game.execute_player(game.players[game.current_government[0]].choose_execution(game))
    if (victim.role == Roles.Hitler):
        #print("Hitler was eliminated")
        return Parties.Liberal
    return Parties.No_Party

def fascist_bullet_veto(game):
    #print("Playing fascist policy", game.enacted_policies[Parties.Fascist.value])
    #print("The president must now execute a player")
    game.veto_power = True
    victim = game.execute_player(game.players[game.current_government[0]].choose_execution(game))
    if (victim.role == Roles.Hitler):
        #print("Hitler was eliminated")
        return Parties.Liberal
    return Parties.No_Party

def fascist_win(game):
    #print("Playing fascist policy", game.enacted_policies[Parties.Fascist.value])
    return Parties.Fascist

def liberal_play(game):
    #print("Playing liberal policy", game.enacted_policies[Parties.Liberal.value])
    return Parties.No_Party

def liberal_win(game):
    #print("Playing liberal policy", game.enacted_policies[Parties.Liberal.value])
    return Parties.Liberal

def communist_play(game):
    return Parties.No_Party

def communist_convert(game):
    while (True):
        target = random.randint(0, len(game.players) - 1)
        if (game.players[target].role != Roles.Communist):
            if (game.players[target].party != Parties.Fascist):
                game.players[target] = communist.Communist(target, Roles.Communist, Parties.Communist)
            return Parties.No_Party

def five_year_plan(game):
    # add 2 communist and 1 liberal to the policy deck
    game.policy_deck += [Policies.Liberal, Policies.Communist, Policies.Communist]
    random.shuffle(game.policy_deck)
    return Parties.No_Party

def communist_win(game):
    return Parties.Communist