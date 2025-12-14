#! /usr/bin/env python3

def read_from_file(filename: str) -> str:
    try:
        with open(filename, "r") as fd:
            print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
            content = fd.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    read_from_file("lost_archive.txt")
    print()
    read_from_file("classified_vault.txt")
    print()
    read_from_file("standard_archive.txt")


if __name__ == "__main__":
    main()
