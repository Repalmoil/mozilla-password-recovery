import mozilla_pass_rec
from colorama import init, Fore, Style
import sys



init(autoreset=True)


def main():
    print(Fore.CYAN + "Mozilla Password Recovery Tool")
    command = input(Fore.YELLOW + "Enter command (recover/show/exit): ").strip().lower()

    if command == "recover":
        try:
            data = mozilla_pass_rec.recover_passwords()
            print(Fore.YELLOW + "Recovered Passwords:")
            for entry in data:
                print(f"{Fore.YELLOW}Profile: {Fore.GREEN}{entry['profile']}")
                print(f"{Fore.YELLOW}Website: {Fore.GREEN}{entry['hostname']}")
                print(f"{Fore.YELLOW}Username: {Fore.GREEN}{entry['username']}")
                print(f"{Fore.YELLOW}Password: {Fore.GREEN}{entry['password']}")
                print("-" * 40)
        except Exception as e:
            print(Fore.RED + f"Error during recovery: {str(e)}")
            
    elif command == "show":
        try:
            mozilla_pass_rec.display_all()
        except Exception as e:
            print(Fore.RED + f"Error displaying data: {str(e)}")
        
    elif command == "exit":
        print(Fore.CYAN + "Exiting...")
        sys.exit()
    
    else:
        print(Fore.RED + "Invalid command. Try again.")

if __name__ == "__main__":
    while True:
        main()