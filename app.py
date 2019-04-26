game_action = ""
is_carStarted = False
is_carStopped = False
while True:
    game_action = input("> ").upper()
    if game_action == 'START':
        if is_carStarted == False:
            print('Car has started!')
            is_carStarted = True
            is_carStopped = False
        else:
            print('Car is already started!')
    elif game_action == 'STOP':
        if is_carStopped == False:
            print('Car has stopped.')
            is_carStopped = True
            is_carStarted = False
        else:
            print('Car has already been stopped!')
    elif game_action == 'HELP':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif game_action == 'QUIT':
        break
    else:
        print('Sorry I don\'t know that command')