#! /usr/bin/env python3


def main() -> None:
    """
    main function to test opening a file with the 'with' statement
    ensures the file is closed even when a an error ocurres
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    read_fn = "classified_data.txt"
    write_fn = "security_protocols.txt"
    try:
        with open(read_fn, "r") as fd:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            content = fd.read()
            print(content)
    except (FileNotFoundError, PermissionError) as error:
        print(f"Error: cannot access vault: {error}")
    try:
        with open(write_fn, "w") as fd:
            print("\nSECURE PRESERVATION:")
            data = "[CLASSIFIED] New security protocols archived"
            fd.write(data)
            print(data)
    except PermissionError as error:
        print(f"Error: cannot access vault: {error}")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
