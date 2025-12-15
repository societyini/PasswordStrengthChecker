import os
import time
import configparser
import string

# =========================
# COLORES
# =========================
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# =========================
# BANNER
# =========================
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Colors.CYAN}{Colors.BOLD}
 ██████╗  █████╗ ███████╗███████╗
 ██╔══██╗██╔══██╗██╔════╝██╔════╝
 ██████╔╝███████║███████╗███████╗
 ██╔═══╝ ██╔══██║╚════██║╚════██║
 ██║     ██║  ██║███████║███████║
 ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

            SOCIETY.INI
       Password Strength Checker
        discord.gg/7ZHueg8gWZ
{Colors.RESET}""")

# =========================
# CONFIG
# =========================
def load_config():
    config = configparser.ConfigParser()

    defaults = {
        "save_to_file": False,
        "output_file": "results.txt"
    }

    if os.path.exists("society.ini"):
        config.read("society.ini")
        s = config["SETTINGS"]
        return {
            "save_to_file": s.getboolean("save_to_file", defaults["save_to_file"]),
            "output_file": s.get("output_file", defaults["output_file"])
        }
    return defaults

# =========================
# CHECKER
# =========================
def check_password(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 1:
        return "WEAK", Colors.RED
    elif score <= 3:
        return "MEDIUM", Colors.YELLOW
    else:
        return "STRONG", Colors.GREEN

# =========================
# MAIN
# =========================
def main():
    config = load_config()

    while True:
        banner()

        password = input(
            f"{Colors.YELLOW}Introduce una contraseña: {Colors.RESET}"
        )

        if password.strip() == "":
            print(f"{Colors.RED}La contraseña no puede estar vacía.{Colors.RESET}")
            time.sleep(1.5)
            continue

        strength, color = check_password(password)

        print(f"\n{color}{Colors.BOLD}Nivel de seguridad: {strength}{Colors.RESET}")

        if config["save_to_file"]:
            with open(config["output_file"], "a", encoding="utf-8") as f:
                f.write(f"{password} -> {strength}\n")

        choice = input(
            f"\n{Colors.CYAN}¿Quieres comprobar otra contraseña? (s/n): {Colors.RESET}"
        ).lower()

        if choice != "s":
            print(f"\n{Colors.BOLD}Proceso finalizado.{Colors.RESET}")
            break

# =========================
# START
# =========================
if __name__ == "__main__":
    main()
