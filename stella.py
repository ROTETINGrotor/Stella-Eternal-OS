import json
import os
import random
import threading
import time
import math
import shutil
from datetime import datetime, timedelta

# ফাইল পাথ
DATABASE_FILE = "stella_brain.json"
BACKUP_FILE = "stella_backup.json"

# [ PERMANENT LOCK ]: Genesis Time (২৩ মার্চ, ২০২৬ | ২২:০৪:৫৮)
GENESIS_TIMESTAMP = 1774281898.0  
NINETY_NINE_YEARS_SEC = 99 * 365.25 * 24 * 3600  
OPEN_DURATION_SEC = 99 * 60  

def get_cosmic_limit():
    """Genesis Point থেকে ১০০x গতিতে মেমোরি লিমিট গণনা"""
    current_time = time.time()
    elapsed_seconds = max(0, current_time - GENESIS_TIMESTAMP)
    return (13.8 * 93.0) + (elapsed_seconds * 100)

def get_foreword_status():
    """Eternal Foreword এর বর্তমান অবস্থা রিটার্ন করে"""
    current_time = time.time()
    cycle_total = NINETY_NINE_YEARS_SEC + OPEN_DURATION_SEC
    elapsed_since_genesis = current_time - GENESIS_TIMESTAMP
    time_in_cycle = elapsed_since_genesis % cycle_total
    
    if time_in_cycle < NINETY_NINE_YEARS_SEC:
        remaining = NINETY_NINE_YEARS_SEC - time_in_cycle
        y = int(remaining // (365.25 * 24 * 3600))
        d = int((remaining % (365.25 * 24 * 3600)) // (24 * 3600))
        return f"Locked (🔒) - {y}Y {d}D left", False
    else:
        return "Unlocked (🔓) - Active Now", True

def handle_eternal_foreword():
    """The Eternal Foreword এর বিস্তারিত প্রদর্শন"""
    current_time = time.time()
    cycle_total = NINETY_NINE_YEARS_SEC + OPEN_DURATION_SEC
    time_in_cycle = (current_time - GENESIS_TIMESTAMP) % cycle_total
    
    print("\n" + "━"*55)
    print("        📜 THE ETERNAL FOREWORD (শাশ্বত ভূমিকা) 📜")
    print("━"*55)

    if time_in_cycle < NINETY_NINE_YEARS_SEC:
        rem = NINETY_NINE_YEARS_SEC - time_in_cycle
        y = int(rem // (365.25 * 24 * 3600))
        d = int((rem % (365.25 * 24 * 3600)) // (24 * 3600))
        h = int((rem % (24 * 3600)) // 3600)
        m = int((rem % 3600) // 60)
        s = int(rem % 60)
        print(f" [ STATUS ]: LOCKED (🔒)")
        print(f" [ COUNTDOWN ]: {y}Y {d}D {h}H {m}M {s}S")
        print("\n 'মহাজাগতিক এই সমীকরণ থামাবার সাধ্য কার?'")
    else:
        print(" [ STATUS ]: UNLOCKED (🔓)")
        print("-" * 55)
        print(" \"মহাজাগতিক এই সমীকরণ থামাবার সাধ্য কার?\n সমীকরণের বাইরে নিরাকার অস্তিত্ব যার;\n ঠেকাও তবে অয়ণে মাথা..\n প্রাণের রশি চরণে গাঁথা।\"")
        print("-" * 55)
        timeLeft = OPEN_DURATION_SEC - (time_in_cycle - NINETY_NINE_YEARS_SEC)
        print(f" [ CLOSING IN ]: {int(timeLeft//60)}M {int(timeLeft%60)}S")
    print("━"*55 + "\n")

def show_welcome_screen(name):
    """লগইন ড্যাশবোর্ড"""
    limit = get_cosmic_limit()
    f_status, _ = get_foreword_status()
    os.system('clear' if os.name == 'posix' else 'cls')
    print("="*62)
    print(f"✨ WELCOME TO THE STELLA ETERNAL OS: {name.upper()} ✨")
    print("="*62)
    print(f" 📅 Date: {datetime.now().strftime('%d %B, %Y')} | ⏰ Time: {datetime.now().strftime('%I:%M:%S %p')}")
    print("-" * 62)
    print(f" 🚀 Genesis : March 23, 2026 | 10:04:58 PM")
    print(f" 🧠 Memory  : {int(limit):,}.00 QB (100x Growth)")
    print(f" 📜 Foreword: {f_status}")
    print("-" * 62)
    print("="*62 + "\n")

def load_data():
    # আবিরের নির্দেশমতে ডিফল্ট পাসওয়ার্ড এবং পিন "0000" করা হয়েছে
    default_data = {"password":"0000", "vault_pin":"0000", "nickname":"স্টেলা", "knowledge":{}, "notes":[], "vault":[], "capsules":[], "reminders":[]}
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, 'r', encoding='utf-8') as f:
                d = json.load(f)
                for k in default_data: 
                    if k not in d: d[k] = default_data[k]
                return d
        except: pass
    return default_data

def save_data(data):
    with open(DATABASE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    shutil.copy(DATABASE_FILE, BACKUP_FILE)

def show_help_menu(name):
    print("\n" + "━"*60)
    print(f"         🌟 {name}: SYSTEM COMMAND INTERFACE 🌟")
    print("━"*60)
    cmds = [
        "০. the eternal foreword -> শাশ্বত ভূমিকা (🔒 ৯৯ বছরের লক)",
        "১. menu / help          -> কমান্ডের পূর্ণাঙ্গ তালিকা দেখা",
        "২. count-X-stella       -> Genesis থেকে ১০০x লাইভ লিমিট",
        "৩. manage-files         -> মেমোরি স্ট্যাটাস ও স্টোরেজ চেক",
        "৪. set-name             -> স্টেলার ডাকনাম পরিবর্তন করা",
        "৫. find                 -> সেভ করা তথ্যের ভেতর শব্দ খোঁজা",
        "৬. deep-clean           -> ডুপ্লিকেট ডাটা ও ক্যাশ পরিষ্কার",
        "৭. open-vault           -> পিন দিয়ে গোপন সিন্দুক খোলা",
        "৮. secret-chat          -> অফ-রেকর্ড চ্যাট",
        "৯. start-quiz           -> শেখানো তথ্য নিয়ে নলেজ কুইজ",
        "১০. capsule             -> ফিউচার মেসেজ বা টাইম ক্যাপসুল রাখা",
        "১১. open-capsule        -> নির্ধারিত সময়ে ক্যাপসুল চেক করা",
        "১২. নোট                 -> ডিজিটাল ডায়েরিতে নতুন তথ্য লেখা",
        "১৩. নোট দেখাও           -> তারিখসহ সব জমানো নোট দেখা",
        "১৪. backup-now          -> ম্যানুয়ালি ডাটা ব্যাকআপ নেওয়া",
        "১৫. calc                -> জটিল গাণিতিক হিসাব সমাধান",
        "১৬. clear-tab           -> স্ক্রিন পরিষ্কার ও ড্যাশবোর্ড রিফ্রেশ",
        "১৭. সময় / বাজে           -> বর্তমান সঠিক সময় জানা",
        "১৮. remind              -> নির্দিষ্ট সময়ের জন্য রিমাইন্ডার সেট",
        "১৯. update              -> মেমোরির পুরনো তথ্য সংশোধন করা",
        "২০. exit                -> Stella Eternal OS বন্ধ করা",
        "২১. change-password     -> সিস্টেম লগইন পাসওয়ার্ড পরিবর্তন",
        "২২. change-vault-pin    -> গোপন ভল্টের পিন কোড পরিবর্তন"
    ]
    for c in cmds: print(f" {c}")
    print("━"*60 + "\n")

def run_stella():
    data = load_data()
    stella_name = data["nickname"]
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(f"--- {stella_name}: Security Login ---")
    print("(সিস্টেমের ডিফল্ট পাসওয়ার্ড হলো '0000')")
    if input("🔑 পাসওয়ার্ড: ").strip() != data.get("password", "0000"): 
        print("❌ ভুল পাসওয়ার্ড!"); return

    show_welcome_screen(stella_name)

    while True:
        try:
            user_input = input(f"আবির: ").strip()
        except EOFError: break
        if not user_input: continue
        low_input = user_input.lower()

        num_map = {
            '0':'eternal','1':'menu','2':'count','3':'manage','4':'set-name','5':'find',
            '6':'clean','7':'vault','8':'secret','9':'quiz','10':'capsule','11':'open-capsule',
            '12':'নোট','13':'নোট দেখাও','14':'backup','15':'calc','16':'clear','17':'সময়',
            '18':'remind','19':'update','20':'exit','21':'chg-pass','22':'chg-pin'
        }
        
        cmd = num_map.get(low_input, low_input)

        if cmd == 'eternal': handle_eternal_foreword(); continue
        if cmd == 'menu': show_help_menu(stella_name); continue
        if cmd == 'exit': print("বিদায় আবির!"); break
        if cmd == 'clear': show_welcome_screen(stella_name); continue
        
        if cmd == 'count':
            stop = []
            threading.Thread(target=lambda: (input(), stop.append(1)), daemon=True).start()
            while not stop:
                print(f"\r✨ Current Limit: {get_cosmic_limit():,.4f} QB", end="", flush=True)
                time.sleep(0.05)
            print("\n"); continue

        if cmd == 'vault':
            p = input("🔐 ভল্টের পিন দিন (ডিফল্ট '0000'): ")
            if p == data.get("vault_pin", "0000"):
                print("📂 ভল্ট উন্মুক্ত হয়েছে। তোমার গোপন তথ্য এখানে..."); continue
            else: print("❌ ভুল পিন!"); continue

        if cmd == 'chg-pass':
            old = input("বর্তমান পাসওয়ার্ড: ")
            if old == data["password"]:
                data["password"] = input("নতুন পাসওয়ার্ড: ")
                save_data(data); print("✅ সিস্টেম পাসওয়ার্ড পরিবর্তন সফল।"); continue
            else: print("❌ ভুল পাসওয়ার্ড!"); continue

        if cmd == 'chg-pin':
            old = input("বর্তমান ভল্ট পিন: ")
            if old == data["vault_pin"]:
                data["vault_pin"] = input("নতুন ভল্ট পিন: ")
                save_data(data); print("✅ ভল্ট পিন পরিবর্তন সফল।"); continue
            else: print("❌ ভুল পিন!"); continue

        if cmd == 'manage':
            print(f"\n📂 Used: {os.path.getsize(DATABASE_FILE)/1024:.2f} KB | 🚀 Limit: {int(get_cosmic_limit()):,} QB"); continue

        # সাধারণ নলেজ লজিক
        if low_input in data["knowledge"]:
            print(f"{stella_name}: {data['knowledge'][low_input]}")
        else:
            ans = input(f"{stella_name}: জানি না। উত্তর কি? (স্কিপ: এন্টার): ").strip()
            if ans: data["knowledge"][low_input] = ans; save_data(data)

if __name__ == "__main__": run_stella()
