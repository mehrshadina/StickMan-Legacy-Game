import time

coins = 500
last_coins_update = 0
last_dragon_damages = 0
army = []
miners_employment_times = []
dragons_health = 100
mines = [0, 0, 0, 0]  # Number of miners on each mine
deleted_idx = set()

def add_soldier(role, timestamp):
    global coins, army

    if dragons_health <= 0:
        return "game over"
    elif coins < get_cost(role):
        return "not enough money"
    elif len(army) >= 50:
        return "too many army"
    else:
        coins -= get_cost(role)
        army.append({"role": role, "health": get_health(role), "timestamp": timestamp})
        return len(army)

def add_miners(role, timestamp):
    global coins, miners_employment_times, mines

    if dragons_health <= 0:
        return "game over"
    elif coins < get_cost(role):
        return "not enough money"
    elif len(miners_employment_times) > 8:
        return "too many miners"
    else:
        miners_employment_times.append(int(timestamp.replace(":", "")))
        coins -= get_cost(role)
        army.append({"role": role, "health": get_health(role), "timestamp": timestamp})
        return len(army)

def damage_soldier(idx, d, timestamp):
    global army, dragons_health, mines

    idx = idx-1

    if dragons_health <= 0:
        return "game over"
    if idx not in deleted_idx and idx >= len(army) or army[idx]["health"] <= 0:
        return "no matter"
    else:
        #print(army[idx])
        army[idx]["health"] -= d
        if army[idx]["health"] <= 0:
            deleted_idx.add(idx)
            mines[mines.index(min(mines))] += 1
            return "dead"
        else:
            return army[idx]["health"]

def get_enemy_status(timestamp):
    global dragons_health

    if dragons_health <= 0:
        return "Game over"
    else:
        return dragons_health

def get_army_status():
    global army

    #for a in army:
        #print(a)
    if dragons_health <= 0:
        return "game over"
    else:
        soldiers = [0, 0, 0, 0, 0, 0]  # Number of soldiers per role
        for soldier in army:
            if (soldier['health'] <= 0) != True:
                soldiers[get_role_index(soldier["role"])] += 1
        return " ".join(str(x) for x in soldiers)
    

def get_money_status(timestamp):
    global coins

    if dragons_health <= 0:
        return "game over"
    else:
        return coins

def get_cost(role):
    if role == "miner":
        return 150
    elif role == "swordwrath":
        return 125
    elif role == "archidon":
        return 300
    elif role == "spearton":
        return 500
    elif role == "magikill":
        return 1200
    elif role == "giant":
        return 1500

def get_power(role):
    if role == "miner":
        return 0
    elif role == "swordwrath":
        return 20
    elif role == "archidon":
        return 10
    elif role == "spearton":
        return 35
    elif role == "magikill":
        return 200
    elif role == "giant":
        return 150
    
def get_power_delay(role):
    if role == "swordwrath":
        return 1
    elif role == "archidon":
        return 1
    elif role == "spearton":
        return 3
    elif role == "magikill":
        return 5
    elif role == "giant":
        return 4

def get_health(role):
    if role == "miner":
        return 100
    elif role == "swordwrath":
        return 120
    elif role == "archidon":
        return 80
    elif role == "spearton":
        return 250
    elif role == "magikill":
        return 80
    elif role == "giant":
        return 1000

def get_role_index(role):
    if role == "miner":
        return 0
    elif role == "swordwrath":
        return 1
    elif role == "archidon":
        return 2
    elif role == "spearton":
        return 3
    elif role == "magikill":
        return 4
    elif role == "giant":
        return 5

def income_coins(role, timestamp):
    global last_coins_update, miners_employment_times, coins

    current_time = int(timestamp.replace(":", ""))
    if current_time - last_coins_update >= 20_000:  # هر 20 ثانیه
        coins += 180  # افزایش سکه‌ها
        last_coins_update += 20_000

    for i in range(len(miners_employment_times)):
        if current_time - miners_employment_times[i] >= 10_000:  # هر 10 ثانیه
            coins += 100  # افزایش سکه با درآمد معدنکار
            miners_employment_times[i] += 10_000

def dragon_damages(timestamp):
    global last_dragon_damages, army, dragons_health
    current_time = int(timestamp.replace(":", ""))

    delta_time = int((current_time - last_dragon_damages)/1000)
    if delta_time >= 1:
        for soldier in army:
            if soldier['role'] != 'miner' and soldier['health'] > 0:
                #print(soldier['role'])
                #print(get_power(soldier['role']) * (delta_time//get_power_delay(soldier['role'])))
                #print(dragons_health)
                dragons_health -= (get_power(soldier['role']) * (delta_time//get_power_delay(soldier['role'])))
                #print(dragons_health)
                #print('-----')
    last_dragon_damages = current_time

def process_request(request):
    parts = request.split()
    request_type = parts[0]

    income_coins(role=parts[1], timestamp=parts[-1])
    dragon_damages(timestamp=parts[-1])

    if request_type == "add":
        role = parts[1]
        timestamp = parts[2]
        if role == 'miner':
            return add_miners(role, timestamp)
        else:
            return add_soldier(role, timestamp)
    elif request_type == "damage":
        idx = int(parts[1])
        d = int(parts[2])
        timestamp = parts[3]
        return damage_soldier(idx, d, timestamp)
    elif request_type == "enemy-status":
        timestamp = parts[1]
        return get_enemy_status(timestamp)
    elif request_type == "army-status":
        return get_army_status()
    elif request_type == "money-status":
        timestamp = parts[1]
        return get_money_status(timestamp)

def process_requests(input_file, output_file):
    global dragons_health
    
    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        q, h = map(int, f_in.readline().split())
        f_out.write(str(coins) + "\n")

        dragons_health = h
        for _ in range(q):
            request = f_in.readline().strip()
            output = str(process_request(request))
            f_out.write(output + "\n")
            print(output)
    """
    q, h = map(int, input().split())
    dragons_health = h

    for _ in range(q):
            request = input().strip()
            output = process_request(request)
            print(output)
    """

input_file = "input.txt"
output_file = "output.txt"
process_requests(input_file, output_file)
