#! /usr/bin/env python3

import sys


def main() -> None:
    """
    main function to test how sys.argv works
    """
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return None
    scores = []
    i = 1
    while (i < argc):
        try:
            new_score = int(sys.argv[i])
        except ValueError:
            print(f"{sys.argv[i]} is not a valid score")
            return None
        scores += [new_score]
        i += 1
    print(f"Scores proccesed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
