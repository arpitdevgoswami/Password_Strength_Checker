import getpass
from colorama import init, Fore, Style
from checker import analyze_password
from scorer import evaluate
from feedback import generate_feedback

# Initialize colorama
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + """
    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗
    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║
    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║
    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
    """)
    print(Fore.YELLOW + "         🔐 Password Strength Checker  v1.0\n")


def print_result(password, results, score, label, tips):

    print(Fore.WHITE + "\n" + "═" * 50)

    # Strength label with color
    if score >= 8:
        color = Fore.CYAN
    elif score >= 6:
        color = Fore.GREEN
    elif score >= 4:
        color = Fore.YELLOW
    elif score >= 2:
        color = Fore.MAGENTA
    else:
        color = Fore.RED

    print(color + f"\n  Strength  :  {label}")
    print(Fore.WHITE + f"  Score     :  {score} / 9")

    print(Fore.WHITE + "\n" + "─" * 50)
    print(Fore.WHITE + "  📋 Feedback:\n")
    for tip in tips:
        print(Fore.WHITE + f"    {tip}")

    print(Fore.WHITE + "\n" + "═" * 50 + "\n")


def main():
    print_banner()

    while True:
        print(Fore.WHITE + "  Options:")
        print(Fore.WHITE + "    [1] Check password (hidden input)")
        print(Fore.WHITE + "    [2] Check password (visible input)")
        print(Fore.WHITE + "    [3] Exit\n")

        choice = input(Fore.YELLOW + "  Enter choice: ").strip()

        if choice == '1':
            password = getpass.getpass(Fore.YELLOW + "\n  Enter password: ")
        elif choice == '2':
            password = input(Fore.YELLOW + "\n  Enter password: ")
        elif choice == '3':
            print(Fore.CYAN + "\n  Goodbye! Stay secure 🔐\n")
            break
        else:
            print(Fore.RED + "\n  ❌ Invalid choice. Try again.\n")
            continue

        if not password:
            print(Fore.RED + "\n  ❌ Password cannot be empty!\n")
            continue

        results = analyze_password(password)
        score, label = evaluate(results)
        tips = generate_feedback(results, score, password)

        print_result(password, results, score, label, tips)


if __name__ == "__main__":
    main()