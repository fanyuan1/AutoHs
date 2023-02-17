from FSM_action import system_exit, AutoHS_automata
import keyboard
from log_state import check_name
from print_info import print_info_init
from FSM_action import init
import sys


if __name__ == "__main__":

    if sys.argv[1] == 'evenDK':
        # EVEN DK
        # AAEBAfHhBATN9AKvjgT47ATipAUN9Q37zgOL1QPJ4gTw4wSN5ASR5ASS5ASP5gTV8QSF9gTdggXixQUA
        REPLACE_COST_BAR = 2
        HERO_POWER_COST = 1
        EVEN_DECK = True

    elif sys.argv[1] == 'classicZoo':
        # # Classic ZOO
        # # AAEDAf0GArahBJajBA77lQSzlgTVlgTtlgSuoQSyoQS9oQTuoQSdogSjogS7ogTDowS5oQS0oQQA
        REPLACE_COST_BAR = 1
        HERO_POWER_COST = 2
        EVEN_DECK = False
    else:
        REPLACE_COST_BAR = 2
        HERO_POWER_COST = 2
        EVEN_DECK = False

    print(sys.argv[1])
    print(EVEN_DECK)

    check_name()
    print_info_init()
    init()
    keyboard.add_hotkey("ctrl+q", system_exit)
    AutoHS_automata()
