from colorama import init, Fore, Back, Style
init(autoreset=True)

messages = [
  'bla bla bla bla',
  (Fore.LIGHTYELLOW_EX + Style.BRIGHT
  + Back.GREEN + 'Alert'),
  'bla bla bla'
]

for m in messages:
  print(m)