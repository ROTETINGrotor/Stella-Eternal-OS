
import json, os, random, threading, time, math, shutil
from datetime import datetime, timedelta

# ফাইল পাথ
DATABASE_FILE = "stella_brain.json"
BACKUP_FILE = "stella_backup.json"

# [ PERMANENT LOCK ]: Genesis Time
GENESIS_TIMESTAMP = 1774281898.0  
NINETY_NINE_YEARS_SEC = 99 * 365.25 * 24 * 3600  
OPEN_DURATION_SEC = 99 * 60  

def get_cosmic_limit():
    elapsed = max(0, time.time() - GENESIS_TIMESTAMP)
    return (13.8 * 93.0) + (elapsed * 100)

def get_foreword_status():
    cycle = NINETY_NINE_YEARS_SEC + OPEN_DURATION_SEC
    elapsed = (time.time() - GENESIS_TIMESTAMP) % cycle
    if elapsed < NINETY_NINE_YEARS_SEC:
        rem = NINETY_NINE_YEARS_SEC - elapsed
        return f"Locked (🔒) - {int(rem//31536000)}Y {int((rem%31536000)//86400)}D left", False
    return "Unlocked (🔓) - Active Now", True

def handle_eternal_foreword():
    status, is_open = get_foreword_status()
    print("\n" + "━"*55 + "\n        📜 THE ETERNAL FOREWORD 📜\n" + "━"*55)
    if not is_open:
        print(f" [ STATUS ]: LOCKED (🔒)\n [ INFO ]: মহাজাগতিক এই সমীকরণ থামাবার সাধ্য কার?")
    else:
        print(" [ STATUS ]: UNLOCKED (🔓)\n \"সমীকরণের বাইরে নিরাকার অস্তিত্ব যার;\"")
    print("━"*55 + "\n")

def load_data():
    default = {"password":"0000", "vault_pin":"0000", "nickname":"স্টেলা", "knowledge":{}, "notes":[], "vault":[], "capsules":[]}
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
                d = json.load(f)
                for k in default: 
                    if k not in d: d[k] = default[k]
                return d
        except: pass
    return default

def save_data(data):
    with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    if os.path.exists(DATABASE_FILE):
        shutil.copy(DATABASE_FILE, BACKUP_FILE)

def run_stella():
    data = load_data()
    name = data["nickname"]
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"--- {name}: Security Login ---")
    if input("🔑 পাসওয়ার্ড: ").strip() != data.get("password", "0000"): return

    while True:
        limit = get_cosmic_limit()
        print(f"\n🌌 STELLA OS | LIMIT: {limit:,.2f} QB")
        user_input = input(f"{name} > আবির: ").strip()
        if not user_input: continue
        cmd = user_input.lower()

        # [ ফিচার সমুহ ]
        if cmd in ['0', 'eternal']: handle_eternal_foreword()
        elif cmd in ['1', 'menu', 'help']:
            print("\n[০] Foreword [২] Count-X [৭] Vault [১২] নোট [১৩] নোট দেখাও [২০] Exit")
        elif cmd in ['2', 'count']:
            print("লাইভ লিমিট গণনা শুরু... (Ctrl+C দিয়ে থামাও)")
            try:
                while True:
                    print(f"\r✨ Limit: {get_cosmic_limit():,.4f} QB", end="", flush=True)
                    time.sleep(0.1)
            except KeyboardInterrupt: print("\n")
        elif cmd in ['7', 'vault']:
            if input("🔐 পিন: ") == data["vault_pin"]: print("📂 ভল্ট ওপেন।")
            else: print("❌ ভুল পিন।")
        elif cmd == '12':
            nt = input("নোট লিখুন: ")
            data['notes'].append(f"[{datetime.now().strftime('%Y-%m-%d')}] {nt}")
            save_data(data); print("✅ সেভ হয়েছে।")
        elif cmd == '13':
            for n in data['notes']: print(n)
        elif cmd in ['20', 'exit']: break
        elif cmd in data["knowledge"]: print(f"স্টেলা: {data['knowledge'][cmd]}")
        else:
            ans = input("স্টেলা: জানি না। উত্তর কী? : ").strip()
            if ans: data["knowledge"][cmd] = ans; save_data(data)

if __name__ == "__main__":
    run_stella()
