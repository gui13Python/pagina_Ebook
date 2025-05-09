import pyautogui
import time
import datetime

def agendar_clique(x, y, hora_alvo):
    """
    Agenda um clique na coordenada (x, y) quando a hora atual for igual a hora_alvo.

    Args:
        x (int): Coordenada x da tela.
        y (int): Coordenada y da tela.
        hora_alvo (str): Hora no formato HH:MM (ex: "08:00").
    """
    while True:
        agora = datetime.datetime.now()
        hora_atual = agora.strftime("%H:%M")

        # Verifica se já passou da hora alvo hoje
        hora_alvo_dt = datetime.datetime.strptime(hora_alvo, "%H:%M").time()
        if agora.hour > hora_alvo_dt.hour or (agora.hour == hora_alvo_dt.hour and agora.minute >= hora_alvo_dt.minute):
            amanha = agora + datetime.timedelta(days=1)
            hora_do_clique = amanha.replace(hour=hora_alvo_dt.hour, minute=hora_alvo_dt.minute, second=0, microsecond=0)
            print(f"Hoje já passou das {hora_alvo}. O clique será agendado para amanhã, {hora_do_clique.strftime('%Y-%m-%d %H:%M')}.")
            break
        elif hora_atual == hora_alvo:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            print(f"Clique realizado em ({x}, {y}) às {hora_alvo}")
            break  # Encerra o loop após o clique
        time.sleep(1)  # Verifica a hora a cada segundo

if __name__ == "__main__":
    # *** Coordenadas do clique ***
    x_clique = 2030
    y_clique = 54

    # *** Defina a hora para o clique (formato HH:MM) ***
    hora_do_clique = "18:11"

    # *** Agende o clique ***
    print(f"O clique será agendado para as {hora_do_clique}...")
    agendar_clique(x_clique, y_clique, hora_do_clique)
    
    
    
    
pyautogui.click(2030,54)
time.sleep(10)