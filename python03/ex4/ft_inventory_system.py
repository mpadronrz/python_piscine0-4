#! /usr/bin/env python3

def inventory_value(inventory: dict) -> int:
    total = 0
    for element in inventory.values():
        total += element["amount"] * element["value"]
    return total


def item_count(inventory: dict) -> int:
    total = 0
    for element in inventory.values():
        total += element["amount"]
    return total


def print_categories(inventory: dict) -> None:
    aux = {}
    for elem in inventory.values():
        aux[elem["category"]] = aux.get(elem["category"], 0) + elem["amount"]
    string = "Categories: "
    for elem in aux.keys():
        string += f"{elem}({aux[elem]}), "
    print(string[:-2])


def print_inventory(inventory: dict) -> None:
    for element, data in inventory.items():
        print(f"{element} ({data["category"]}, {data["rarity"]}): {data["amount"]}x @ {data["value"]} gold each = {data["amount"] * data["value"]}")
    print(f"\nInventory value: {inventory_value(inventory)} gold")
    print(f"Item count: {item_count(inventory)} items")
    print_categories(inventory)


def transaction(player1: dict, player2: dict, item: str, amount: int) -> None:
    if amount <= 0:
        return None
    if player1.get(item) is None or player1[item].get("amount", 0) < amount:
        print(f"Cannot complete transaction: player1 doesn't have enough {item}")
        return None
    player1[item]["amount"] -= amount
    if player2.get(item) is None:
        player2[item] = {
            "category": player1[item]["category"],
            "rarity": player1[item]["rarity"],
            "amount": amount,
             "value": player1[item]["value"]
        }
    else:
        player2[item]["amount"] += amount


def main() -> None:
    print("=== Player Inventory System ===")
    alice = {
        "sword": {
            "category": "weapon",
            "rarity": "rare",
            "amount": 1,
             "value": 500
        },
        "potion": {
            "category": "consumable",
            "rarity": "common",
            "amount": 5,
             "value": 50
        },
        "shield": {
            "category": "armor",
            "rarity": "uncommon",
            "amount": 1,
             "value": 200
        }
    }
    bob = {
        "magic_ring": {
            "category": "weapon",
            "rarity": "rare",
            "amount": 1,
             "value": 500
        }
    }
    print("\n=== Alice's Inventory ===")
    print_inventory(alice)
    print("\n=== Bob's Inventory ===")
    print_inventory(bob)
    transaction(alice, bob, "potion", 2)
    print("\n=== Alice's Inventory ===")
    print_inventory(alice)
    print("\n=== Bob's Inventory ===")
    print_inventory(bob)

if __name__ == "__main__":
    main()
