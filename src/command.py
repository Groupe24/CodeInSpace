# -*- coding: utf-8 -*-
def parse_command(commands, game_stats):
    """
    Parse a command from a player and run it.

    Parameters
    ----------
    command : command from the player (str).
    game_stats : stat of the game (dic).

    Return
    ------
    game_stats : game stat after the command execution (dic).

    Version
    -------
    specification v1. Nicolas Van Bossuyt (10/2/2017)
    implementation v1. Nicolas Van Bossuyt (10/2/2017)
    """
    commands = commands.split(' ')

    for cmd in commands:
        sub_cmd = cmd.split(':')
        ship_name = sub_cmd[0]
        ship_action = sub_cmd[1]

        if ship_action == 'slower' or ship_action == 'faster':
            game_stats = command_change_speed(ship_name, ship_action, game_stats)
        elif ship_action == 'left' or ship_action == 'right':
            game_stats = command_rotate(ship_name, ship_action, game_stats)
        else:
            ship_action = ship_action.split('-')
            coordinate = (int(ship_action[0]), int(ship_action[1]))
            game_stats = command_attack(ship_name, coordinate, game_stats)

    return game_stats

def command_change_speed(ship, change, game_stats):
    """
    Increase the speed of a ship.

    Parameters
    ----------
    ship : name of the ship to Increase the speed (str).
    change : the way to change the speed <"slower"|"faster"> (str).
    game_stats : stats of the game (dic).

    Returns
    -------
    game_stats : the game after the command execution (dic)
    """
    type = game_stats['ship'][ship]['type']

    # Make the ship move faster.
    if change == 'faster' and gamestats['ship'][ship]['speed'] < gamestats['model_ship'][type]['max_speed']:
        game_stats['ship'][ship]['speed']+=1

    # make the ship move slower.
    elif change == 'slower' and gamestats['ship'][ship]['speed'] > 0:
        game_stats['ship'][ship]['speed']-=1

    # show a message when is a invalide change.
    else:
        print 'you cannot make that change on the speed of this ship'

    return game_stats

def command_rotate(ship, direction, game_stats):
    """
    Rotate the ship.

    Parameters
    ----------
    ship : name of the ship to Increase the speed.
    direction : the direction to rotate the ship <"left"|"right">(str)
    game_stats : stats of the game (dic).

    Returns
    -------
    new_game_stats : the game after the command execution.
    """
    raise NotImplementedError

def command_attack(ship, coordinate, game_stats):
    """
    Rotate the ship.

    Parameters
    ----------
    ship : name of the ship to Increase the speed.
    coordinate : coordinate of the tile to attack (tuple(int,int)).
    game_stats : stats of the game (dic).

    Returns
    -------
    new_game_stats : the game after the command execution.
    """
    raise NotImplementedError
