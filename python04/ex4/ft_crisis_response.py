#! /usr/bin/env python3

def read_from_file(filename: str) -> str | None:
    """
    Opens and reads the content of a file pased as parameter.
    Handels FileNotFoundError and PermissionError apropiately
    Returns the content of th e file on succes and None on failiure
    """
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
        return None
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        return None
    return content


def main() -> None:
    """
    main function to test read_from_file()
    Tests for valid file, non existing file and file without reading rights
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    read_from_file("lost_archive.txt")
    print()
    read_from_file("classified_vault.txt")
    print()
    read_from_file("standard_archive.txt")


if __name__ == "__main__":
    main()
