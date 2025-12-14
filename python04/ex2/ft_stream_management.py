#! /usr/bin/env python3

import sys


def main() -> None:
    """
    main function to test:
        - reading from stdin: input()
        - writing to stdout: sys.stdout
        - writing to stderr: sys.stderr
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    user_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    print(
        f"[STANDARD]: Archive status from {user_id}: {status}",
        file=sys.stdout
    )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
    )
    print(
        "[STANDARD] Data transmission complete",
        file=sys.stdout
    )
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
