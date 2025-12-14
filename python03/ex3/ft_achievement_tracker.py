#! /usr/bin/env python3

def get_data() -> None:
    """
    Returns data dict to use in later functions
    """
    data = {
        "alice": [
            "first_blood",
            "pixel_perfect",
            "speed_runner",
            "first_blood",
            "first_blood",
        ],
        "bob": [
            "level_master",
            "boss_hunter",
            "treasure_seeker",
            "level_master",
            "level_master",
        ],
        "charlie": [
            "treasure_seeker",
            "boss_hunter",
            "combo_king",
            "first_blood",
            "boss_hunter",
            "first_blood",
            "boss_hunter",
            "first_blood",
        ],
        "diana": [
            "first_blood",
            "combo_king",
            "level_master",
            "treasure_seeker",
            "speed_runner",
            "combo_king",
            "combo_king",
            "level_master",
        ],
        "eve": [
            "level_master",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
        ],
        "frank": [
            "explorer",
            "boss_hunter",
            "first_blood",
            "explorer",
            "first_blood",
            "boss_hunter",
        ],
    }
    return data


def all_achivements(players: list[set]) -> set:
    """
    Takes a list of achievments (sets) and returns the achievments
    held by any player
    (union of sets)
    """
    all = set()
    for player in players:
        all = all.union(player)
    return all


def common_achivements(players: list[set]) -> set:
    """
    Takes a list of achievments (sets) and returns the achievments held
    by all players
    (intersection of sets)
    """
    if len(players) == 0:
        return set()
    common = players[0]
    for i in range(1, len(players)):
        common = common.intersection(players[i])
    return common


def rare_achivements(players: list[set]) -> set:
    """
    Takes a list of achievments (sets) and returns the achievments held
    by only one player
    (difference and union of sets)
    """
    rare = set()
    for i in range(len(players)):
        aux = players[i]
        for j in range(len(players)):
            if i == j:
                continue
            aux = aux.difference(players[j])
        rare = rare.union(aux)
    return rare


def main() -> None:
    """
    main function to test all the above ones
    takes data from get_data and uses the rest of functions to analize
    the achievments
    """
    print("=== Achievement Tracker System ===\n")
    data = get_data()
    alice = set(data["alice"])
    bob = set(data["bob"])
    charlie = set(data["charlie"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    all = all_achivements([alice, bob, charlie])
    print(f"All unique achievements: {all}")
    print(f"Total unique achievements: {len(all)}")

    common = common_achivements([alice, bob, charlie])
    print(f"Common to all players: {common}")

    rare = rare_achivements([alice, bob, charlie])
    print(f"Rare achievements (1 player): {rare}")

    common_ab = common_achivements([alice, bob])
    print(f"Alice vs Bob common: {common_ab}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
