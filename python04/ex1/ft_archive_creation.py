#! /usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - RESERVATION SYSTEM ===\n")
    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    try:
        fd = open(filename, "w")
        print("Connection established...")
    except PermissionError as error:
        print(f"Error: cannot access Storage Vault: {error}")
        return
    print("\nInscribing preservation data...")
    content = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee"
    )
    fd.write(content)
    print(content)
    fd.close()
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
