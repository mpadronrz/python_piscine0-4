#! /usr/bin/env python3

def main() -> None:
    """
    main function to test open and reading a file
    handels FileNotFoundError, PermissionError apropiately
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        fd = open(filename, "r")
        print("Connection established...")
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error: cannot access Storage Vault: {error}")
        return
    print("RECOVERED DATA:")
    content = fd.read()
    print(content)
    print("\nData recovery complete. Storage unit disconnected.")
    fd.close()


if __name__ == "__main__":
    main()
