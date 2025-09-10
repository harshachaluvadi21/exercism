"""
Functions for implementing the rules of the classic arcade game Pac-Man.
"""


def eat_ghost(power_pellet_active, touching_ghost):
    """
    Pac-Man can eat a ghost only if power pellet is active and he is touching a ghost.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """
    Pac-Man scores when touching a power pellet or a dot.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored?
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """
    Pac-Man loses the game if he touches a ghost without an active power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Pac-Man wins the game if all dots have been eaten and he hasn't lost.

    :param has_eaten_all_dots: bool - has the player eaten all dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
