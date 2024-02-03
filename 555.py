import keyboard

def on_key_event(event):
    if event.name == '1':
        keyboard.send('a')
        keyboard.send('s')
    elif event.name == '2':
        keyboard.send('a')
        keyboard.send('w')
    elif event.name == '3':
        keyboard.send('d')
        keyboard.send('s')
    elif event.name == '4':
        keyboard.send('d')
        keyboard.send('w')
    elif event.name == '5':
        keyboard.send('w')
        keyboard.send('d')
    elif event.name == '6':
        keyboard.send('w')
        keyboard.send('a')

# Ajout du gestionnaire d'événements pour les touches
keyboard.on_press(on_key_event)

# Boucle infinie pour maintenir le programme actif
keyboard.wait('esc')  # Attend que la touche "Escape" soit pressée pour quitter le programme
