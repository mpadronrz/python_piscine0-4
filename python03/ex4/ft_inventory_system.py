#! /usr/bin/env python3


def inventory_generator() -> dict:
    """
    Generates the videogame inventory, with players and a catalog of all items
    """
    inventory = {
        "players": {
            "alice": {
                "items": {
                    "pixel_sword": 1,
                    "code_bow": 1,
                    "health_byte": 1,
                    "quantum_ring": 3,
                },
                "total_value": 1875,
                "item_count": 6,
            },
            "bob": {
                "items": {
                    "code_bow": 3,
                    "pixel_sword": 2
                    },
                "total_value": 900,
                "item_count": 5,
            },
            "charlie": {
                "items": {
                    "pixel_sword": 1,
                    "code_bow": 1
                    },
                "total_value": 350,
                "item_count": 2,
            },
            "diana": {
                "items": {
                    "code_bow": 3,
                    "pixel_sword": 3,
                    "health_byte": 3,
                    "data_crystal": 3,
                },
                "total_value": 4125,
                "item_count": 12,
            },
        },
        "catalog": {
            "pixel_sword": {
                "type": "weapon",
                "value": 150,
                "rarity": "common"
                },
            "quantum_ring": {
                "type": "accessory",
                "value": 500,
                "rarity": "rare"
                },
            "health_byte": {
                "type": "consumable",
                "value": 25,
                "rarity": "common"
                },
            "data_crystal": {
                "type": "material",
                "value": 1000,
                "rarity": "legendary"
                },
            "code_bow": {
                "type": "weapon",
                "value": 200,
                "rarity": "uncommon"
                }
        }
    }
    return inventory


def print_inventory(inventory: dict, player: str) -> None:
    """
    Displays a player's inventory with useful data
    """
    print(f"=== {player}'s Inventory ===")

    player_inventory = inventory["players"].get(player)
    if player_inventory is None:
        print(f"Error: {player} not found.")
        return

    catalog = inventory["catalog"]
    category = dict()
    for item, amount in player_inventory["items"].items():
        value = catalog[item]["value"]
        tp = catalog[item]["type"]
        category[tp] = category.get(tp, 0) + amount
        print(f"{item} ({catalog[item]['rarity']}, {tp}): "
              f"{amount}x @ {value} each = {amount * value} gold")

    print()
    print(f"Inventory value: {player_inventory['total_value']}")
    print(f"Item count: {player_inventory['item_count']}")

    category_print = "Category: "
    for elem in category:
        category_print += f"{elem}({category[elem]}), "
    print(category_print[:-2])


def transaction(inventory: dict, player1: str,
                player2: str, item: str, amount: int) -> None:
    """
    Takes amount elements of item from player1's inventory and gives
    them to player2.
    Updates the gold value and item_count of both players
    """
    print(f"=== Transaction: {player1} gives {player2} {amount} {item} ===")

    if (player1 == player2):
        print("Error: Player 1 and Player 2 must be different players.")
        print("Transaction unsuccessful!")

    if amount <= 0:
        print(f"Error: {player1} cannot give a non-positive "
              f"amount ({amount}) of {item}")
        print("Transaction unsuccessful!")
        return

    p1_inventory = inventory["players"].get(player1)
    p2_inventory = inventory["players"].get(player2)
    catalog = inventory["catalog"]

    if p1_inventory is None:
        print(f"Error: {player1} not found")
        print("Transaction unsuccessful!")
        return
    if p2_inventory is None:
        print(f"Error: {player2} not found")
        print("Transaction unsuccessful!")
        return

    p1_amount = p1_inventory["items"].get(item, 0)
    if p1_amount < amount:
        print(f"Error: {player1} does not have enough {item}.")
        print("Transaction unsuccessful!")
        return

    item_value = catalog[item]["value"]
    p1_inventory["items"][item] -= amount
    p1_inventory["item_count"] -= amount
    p1_inventory["total_value"] -= amount * item_value
    p2_inventory["items"][item] = p2_inventory["items"].get(item, 0) + amount
    p2_inventory["item_count"] += amount
    p2_inventory["total_value"] += amount * item_value
    inventory["players"].update({player1: p1_inventory, player2: p2_inventory})
    print("Transaction successful!\n")

    category = catalog[item]["type"]
    p1_cat_amount = 0
    p2_cat_amount = 0
    print("=== Updated Inventories ===")
    for item, amount in p1_inventory["items"].items():
        if catalog[item]["type"] == category:
            p1_cat_amount += amount
    for item, amount in p2_inventory["items"].items():
        if catalog[item]["type"] == category:
            p2_cat_amount += amount
    print(f"{player1} {category}: {p1_cat_amount}")
    print(f"{player2} {category}: {p2_cat_amount}")


def inventory_analitics(inventory: dict) -> None:
    """
    Calculates inventory analitics:
        - Most valuable player
        - Player with the most items
        - Rarest items
    """
    players = inventory["players"]
    catalog = inventory["catalog"]

    mvp_gold = -1
    mvp = ""
    mip_items = -1
    mip = ""
    rarest_items = "Rarest items: "
    rank = {
        "common": 0,
        "uncommon": 1,
        "rare": 2,
        "legendary": 3
    }
    current_rarity = -1

    for player, invent in players.items():
        if invent["total_value"] > mvp_gold:
            mvp = player
            mvp_gold = invent["total_value"]
        if invent["item_count"] > mip_items:
            mip = player
            mip_items = invent["item_count"]

        for item, count in invent["items"].items():
            if count == 0:
                continue
            if rank.get(catalog[item]["rarity"], -1) == current_rarity:
                rarest_items += f"{item}, "
            elif rank.get(catalog[item]["rarity"], -1) > current_rarity:
                rarest_items = f"Rarest items: {item}, "

    print("=== Player Inventory System ===")
    print(f"Most valuable player: {mvp} ({mvp_gold} gold)")
    print(f"Most items: {mip} ({mip_items} items)")
    print(rarest_items[:-2])


def main() -> None:
    """
    Tests the above functions, using the inventory generates by
    inventory_generator
    """
    print("=== Player Inventory System ===")
    print()
    inventory = inventory_generator()
    print_inventory(inventory, "alice")
    print()
    transaction(inventory, "alice", "bob", "quantum_ring", 2)
    print()
    inventory_analitics(inventory)


if __name__ == "__main__":
    main()
