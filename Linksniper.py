#!/usr/bin/env python3 import requests, time, os from bs4 import BeautifulSoup

RED = "\033[91m" GREEN = "\033[92m" YELLOW = "\033[93m" BLUE = "\033[94m" CYAN = "\033[96m" RESET = "\033[0m"

banner = f""" {RED}██████╗ ██╗███╗   ███╗███████╗███████╗██╗███████╗ ██╔══██╗██║████╗ ████║██╔════╝██╔════╝██║██╔════╝ ██████╔╝██║██╔████╔██║█████╗  █████╗  ██║███████╗ ██╔═══╝ ██║██╔██╔██║██╔══╝  ██╔══╝  ██║╚════██║ ██║     ██║██║╚═╝██║███████╗██║     ██║███████║ ╚═╝     ╚═╝╚═╝   ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝ {YELLOW}     WhatsApp & Telegram Group Finder - by RIMZI{RESET} """

def search_whatsapp(topic): print(f"\n{CYAN}Searching WhatsApp groups for:{RESET} {topic}\n") headers = {'User-Agent': 'Mozilla/5.0'} url = f"https://html.duckduckgo.com/html/?q=site:chat.whatsapp.com+{topic}" res = requests.get(url, headers=headers) soup = BeautifulSoup(res.text, 'html.parser')

count = 0
for a in soup.find_all('a', href=True):
    href = a['href']
    if "chat.whatsapp.com" in href:
        count += 1
        gid = href.split('/')[-1]
        print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮")
        print(f"{GREEN} Group Name : {topic.title()} Group")
        print(f" ID         : {gid}")
        print(f" Link       : {href}")
        print(f" Description: Public {topic.title()} Group")
        print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n")
        time.sleep(0.2)
if count == 0:
    print(f"{RED}❌ No groups found.{RESET}")

def search_telegram(topic): print(f"\n{CYAN}Searching Telegram groups for:{RESET} {topic}\n") url = f"https://t.me/s/{topic}" try: res = requests.get(url, timeout=5) if res.status_code == 200: print(f"{YELLOW}╭──────────────[ ✅ SUCCESS ✅ ]──────────────╮") print(f"{GREEN} Group Name : {topic.title()} Channel/Group") print(f" Link       : https://t.me/{topic}") print(f" Description: Public Telegram Group") print(f"{YELLOW}╰────────────────────────────────────────────╯{RESET}\n") else: print(f"{RED}❌ Group not found on Telegram.{RESET}") except: print(f"{RED}⚠️ Error connecting to Telegram.{RESET}")

MAIN PROGRAM

os.system('clear') print(banner) print("\nChoose platform:") print(" [1] WhatsApp Group Finder") print(" [2] Telegram Group Finder") choice = input("\n>> ").strip()

if choice == '1': topic = input("\n📘 Enter topic to search (e.g. PUBG, Girls, Crypto): ").strip() search_whatsapp(topic) elif choice == '2': topic = input("\n📘 Enter Telegram group name (e.g. CryptoNews, Termux): ").strip() search_telegram(topic) else: print(f"{RED}❌ Invalid option. Exiting...{RESET}")

