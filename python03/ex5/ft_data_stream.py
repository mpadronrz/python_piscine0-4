#! /usr/bin/env python3

def prime_generator():
    n = 2
    while True:
        sqrt = n ** (1/2)
        i = 2
        while i <= sqrt:
            if n % i == 0:
                n += 1
                break
            i += 1
        else:
            yield n
            n += 1


def fibonacci_generator():
    yield (first := 0)
    yield (second := 1)
    while True:
        first, second = second, first + second
        yield second


def generate_numbers(size: int, method: str):
    if method == "prime":
        generator = prime_generator()
        print(f"Prime numbers (first {size}): ", end="")
    elif method == "fibonacci":
        generator = fibonacci_generator()
        print(f"Fibonacci sequence (first {size}): ", end="")
    else:
        return
    for i in range(size - 1):
        print(f"{next(generator)}, ", end="")
    print(f"{next(generator)}")


def game_events_generator(players, events):
    i = 1
    while True:
        level = ((17 * i + 37) % ((11 * i + 5) % 19 + 2))
        player = players[
            ((47 * i + 7) % (((37 * i + 19)) % (2 * len(events) + 1)
                             + 2 * len(players))) % len(players)
        ]
        event = events[
            ((53 * i + 11) % (((23 * i + 5)) % (3 * len(events) + 1)
                              + 2 * len(players))) % len(events)
        ]
        data = {
            "id": i,
            "level": level,
            "player": player,
            "event": event,
        }
        yield data
        i += 1


def game_events(size, players, events):
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {size} game events...")
    high_level = 0
    tresures = 0
    level_up = 0
    generator = game_events_generator(players, events)
    for i in range(size):
        data = next(generator)
        print(f"Event {data["id"]}: Player {data["player"]} "
              f"(level {data["level"]}) {data["event"]}")
        if data["level"] >= 10:
            high_level += 1
        if data["event"] == "found tresure":
            tresures += 1
        if data["event"] == "leveled up":
            level_up += 1
    print("=== Stream Analytics ===")
    print(f"Total events processed: {size}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {tresures}")
    print(f"Level-up events: {level_up}")


def main():
    players = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
    events = [
        'loged in',
        'loged out',
        'killed monster',
        'died',
        'leveled up',
        'found tresure'
    ]
    game_events(1000, players, events)
    print("\n=== Generator Demonstration ===")
    generate_numbers(23, "fibonacci")
    generate_numbers(13, "prime")


if __name__ == "__main__":
    main()
