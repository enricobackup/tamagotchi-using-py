import os
import time
from datetime import datetime, timedelta
from random import randint
import json


#insira a data atual!
initial_date = datetime(2024, 9, 25)



tamagotchi = {
  "hunger": 3,
  "happiness": 3,
  "health": 3,
  "energy": 3,
  "age": 0, 
  "weight": 0, 
  "sickness": 0, 
  "alive": True,
}

def atualizar_status():
  tempo_de_fome = 10
  tempo_de_sono = 28800
  tempo_de_happiness = 25000
  tempo_sickness = 86400
 


def update_age(initial_date, age):
    current_date = datetime.now()
    days_passed = (current_date - initial_date).days
    new_age = tamagotchi['age'] + days_passed
    return new_age
    


heart_stages = [
"♡︎♡︎♡︎♡︎"
,
"❤♡︎♡︎♡︎"
,
"❤❤♡︎♡︎"
,
"❤❤❤♡︎"
,
"❤❤❤❤"
      ]

tamagotchi_stages = [
  """
"""
]
            
def limpar_tela():
  os.system('cls') 
limpar_tela()

def feed():
  feed_delay = 1.5
  global heart_stages
  limpar_tela()
  
  while True:
    print('escolha uma das opções: ')
    print('1- banana**')
    print('2- maçã**')
    print('3- Sair')
    escolha_de_comida = input('#')
    
    if escolha_de_comida == '1':
      try:
        tamagotchi['hunger'] += 1
        tamagotchi['weight'] += 0.5
        health_value = tamagotchi['hunger']
        print(heart_stages[health_value])
        time.sleep(feed_delay)
        limpar_tela()
        continue
      
      except:
        print('tamagotchi está cheio!')
        time.sleep(feed_delay)
        limpar_tela()
      continue
    
    elif escolha_de_comida == "2":
      try:
        tamagotchi["happiness"] += 1
        tamagotchi['weight'] += 0.5
        health_value = tamagotchi['happiness']
        print(heart_stages[health_value]) 
        time.sleep(feed_delay)    
        limpar_tela()
        continue
      except:
        print('tamagotchi está cheio e feliz!')
        time.sleep(feed_delay)
        limpar_tela()
      continue
    elif escolha_de_comida == '3':
      break
    else:
      limpar_tela()
      print('opção invalida')
      time.sleep(feed_delay)
      limpar_tela()
      continue
    

def lights():
  sleep_delay = 10
  while True:
    limpar_tela()
    print('gostaria de apagar as luzes?')
    print('1- Sim!')
    print('2- Não!')
    lights_choice = input('#')
    limpar_tela()
    
    if lights_choice == '1':
      if tamagotchi['energy'] >= 4:
        print('tamagotchi não está com muito sono...')
        time.sleep(3)
        limpar_tela()
        continue
      
      elif tamagotchi['energy'] in range(0,4):
        tamagotchi['energy'] += 1
        print('luzes apagadas')
        print('tamagotchi está dormindo...')
        time.sleep(sleep_delay)
        limpar_tela()
        continue
    if lights_choice == '2':
      break
    else:
      print('escolha uma opção valida!')
      continue
  
  
def game():
  while True:
    numero_tama_aleatorio = randint(0,10)
    numero_escolhido = randint(3,7)
    if numero_tama_aleatorio == numero_escolhido:
      continue
    else:
      pass
    limpar_tela()
    print('Jogo da advinhação')
    time.sleep(2)
    limpar_tela()
    print(f'o numero escolhido foi {numero_escolhido}.')
    print(f'O tamagotchi pensou em um numero, você acha que é maior ou menor que {numero_escolhido}?')
    print('1- Maior')
    print('2- Menor')
    print('3- sair')
    escolha_game = input('#')
    limpar_tela()
    
    if escolha_game == '1':
      
      if numero_tama_aleatorio > numero_escolhido:
        print(f'Você acertou! O numero do tamagotchi era {numero_tama_aleatorio}')
        time.sleep(2)
        if tamagotchi['happiness'] < 4:
          tamagotchi['happiness'] += 1
        else:
          pass
      else:
        print(f'Você errou! O numero do tamagotchi era {numero_tama_aleatorio}')
        time.sleep(2)
        continue
        
    elif escolha_game == '2':
      if numero_tama_aleatorio < numero_escolhido:
        print(f'Você acertou! O numero do tamagotchi era {numero_tama_aleatorio}')
        time.sleep(2)
        if tamagotchi['happiness'] < 4:
          tamagotchi['happiness'] += 1
        else:
          pass
      else:
        print(f'Você errou! O numero do tamagotchi era {numero_tama_aleatorio}')
        time.sleep(2)
        continue
      
    elif escolha_game == '3':
      break
    else:
      print('escolha uma opção valida!')
      time.sleep(2)
      continue



def medicine():
  limpar_tela()
  global heart_stages
  print('Você deu medicamento para o tamagotchi')
  try:
    tamagotchi['sickness'] -= 1
  except:
    pass
  if tamagotchi['health'] < 4:
    tamagotchi['health'] += 1
  else:
    pass
  time.sleep(1)
  health_heart = tamagotchi['health']
  print(heart_stages[health_heart])
  time.sleep(2)
  
def save_game():
  files = tamagotchi
  with open("tamagotchi.json", "w") as archive:
    json.dump(files, archive, indent=2)
    
def read_save():
  global tamagotchi
  try:
    with open("tamagotchi.json", "r") as archive:
      new_files = json.load(archive)
      tamagotchi = new_files
  except:
    pass
  

def status():
  global tamagotchi
  while True:
    tamagotchi_status_secondary = {
    "hunger": tamagotchi['hunger'],
    "happiness": tamagotchi['happiness'],
    "health": tamagotchi['health'],
    "energy": tamagotchi['energy'],
  }
    break
  
  limpar_tela()
  current_age = update_age(initial_date, tamagotchi['age'])
  phase = current_age
  if phase <= 0:
    idade = "egg"
  elif phase in range(1,5):
    idade = "baby"
  elif phase in range(5,10):
    idade = "child"
  else:
    idade = "Adult"

############################
    
  while True:
    def func_four_below_one():
      return "morrendo!"

    def func_three_below_one():
      return "se sentindo um pouco mal"

    def func_two_below_one():
      return "se sentindo normal"

    def func_one_below_one():
      return "bem"

    def func_no_below_one():
      return "ótimo!"

    count_below_one = sum(1 for value in tamagotchi_status_secondary.values() if value <= 1)


    if count_below_one == 4:
      result = func_four_below_one()
    elif count_below_one == 3:
      result = func_three_below_one()
    elif count_below_one == 2:
      result = func_two_below_one()
    elif count_below_one == 1:
      result = func_one_below_one()
    else:
        result = func_no_below_one()

    print('Bem vindo aos status do seu tamagotchi')
    time.sleep(2)
    print(f'seu tamagotchi está {result}. Atualmente ele é um {idade}.')
    print(f'ele pesa {tamagotchi["weight"]} kg e está com {current_age} anos.')
    input('#')
    break


last_event_date = datetime(2024, 8, 15)
def check_and_perform_action(last_event_date):
  current_date = datetime.now()
  days_passed = (current_date - last_event_date).days
    
  if days_passed >= 2:

    tamagotchi['sickness'] += 1

    last_event_date = current_date
  else:
    pass
    
  return last_event_date
 
def age_ascii(idade):
  if idade == "egg":
    print("""
                                                                          
              ████████                                  
            ██        ██                                
          ██▒▒▒▒        ██                              
        ██▒▒▒▒▒▒      ▒▒▒▒██                            
        ██▒▒▒▒▒▒      ▒▒▒▒██                            
      ██  ▒▒▒▒        ▒▒▒▒▒▒██                          
      ██                ▒▒▒▒██                          
    ██▒▒      ▒▒▒▒▒▒          ██                        
    ██      ▒▒▒▒▒▒▒▒▒▒        ██                        
    ██      ▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒██                        
    ██▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒██                        
      ██▒▒▒▒  ▒▒▒▒▒▒    ▒▒▒▒██                          
      ██▒▒▒▒            ▒▒▒▒██                          
        ██▒▒              ██                            
          ████        ████                              
              ████████                                  
""")
  elif idade == "baby":
    print("""
        ██████████        
    ████▒▒▒▒░░░░░░████    
  ██▒▒▒▒░░░░░░      ░░██  
  ██▒▒▒▒░░░░░░░░    ░░██  
██▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒██
██▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒██
██▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒██
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
    ██████████████████    
          """)
    
  elif idade == "child":
    print("""
          ██████████          
      ████░░░░░░░░░░████      
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
  ██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██  
██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██
██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██
██▓▓▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▓▓██
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  
    ██████████████████████    
""")
  else:
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣤⠤⠤⠴⠤⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠲⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢀⣄⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⣾⣠⠎⠀⣸⠁⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠃⣾⣿⡏⠀⢰⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⠷⠻⠟⠀⠀⠸⣿⠏⠀⠀⢠⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀
⢠⡴⢦⣤⣄⠀⡇⠀⠀⠀⢰⣶⣶⡄⠀⠀⠀⠈⠛⠛⠯⠿⠃⠀⠀⠀⠀⠀⠀⢸⡘⠀⠀
⢸⣹⢿⣾⣹⢿⣿⠀⠀⠀⠀⠹⠏⠀⠀⠀⠀⠀⠀⠀⣀⣶⣆⣀⠀⠀⠀⠀⠀⠀⣿⡀⠀
⠘⣭⢷⣫⡽⣯⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⣻⠽⣶⣫⣟⣷⡄⠀⠀⠀⠀⠘⢖⡀
⠀⠘⣯⢷⣻⣽⣻⣿⡄⠀⠀⠀⠀⠀⠀⢀⣼⣳⣻⢞⣟⣳⡽⣞⣳⢿⡀⠀⠀⠀⠀⠘⣡
⠀⠀⠈⢯⢷⣞⣷⣻⣿⣄⠀⠀⠀⠀⢠⣿⣳⡽⣳⣟⣾⡳⣿⠽⣯⣟⣧⠀⠀⠀⠀⠀⠸
⠀⠀⠀⠀⠙⢞⣾⣳⢿⣿⣷⢤⠀⠈⢿⣳⣳⢟⣳⡽⣶⣻⣽⡻⣗⣯⠷⡄⠀⠀⠀⠀⡬
⠀⠀⠀⠀⠀⠀⠱⢏⣿⡿⠁⠀⠉⠶⣸⣷⢏⡿⣷⢿⢷⡿⣶⢿⣹⡎⠁⠈⠳⠶⠶⠊⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠫⣿⣝⡷⣯⠿⣝⣯⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀           
""")

while True:
  current_age = update_age(initial_date, tamagotchi['age'])
  phase = current_age
  if phase <= 0:
    idade = "egg"
  elif phase in range(1,5):
    idade = "baby"
  elif phase in range(5,10):
    idade = "child"
  else:
    idade = "Adult"
  limpar_tela()
  print('Bem vindo ao tamagotchi!')
  print('')
  age_ascii(idade)
  print("")
  
  escolhas = ["1- alimentar", "2- brincar", "3- dormir", "4- dar remedio", "5- ver status"]
  print('escolha uma das seguintes opções')
  for x in escolhas:
    print(x)
    
  print("\n" "obs: inacabado")
  escolha = input('#')
  if escolha == '1':
    feed()
  elif escolha == '2':
    game()
  elif escolha == '3':
    lights()
    last_event_date = check_and_perform_action(last_event_date)
  elif escolha == '4':
    medicine()
  elif escolha == '5':
    status()
  else:
    print('escolha uma opção valida')   
    continue 
  
    

