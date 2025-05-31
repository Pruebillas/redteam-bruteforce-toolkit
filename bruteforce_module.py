import time
import random
import logging

logging.basicConfig(filename='brute_force_attack.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def simulate_brute_force(target, max_attempts=10):
    print(f"[+] Iniciando ataque de fuerza bruta contra {target}")
    passwords = ["password", "admin", "123456", "qwerty", "letmein"]
    
    for attempt in range(1, max_attempts + 1):
        password = random.choice(passwords)
        print(f"[*] Intento {attempt}: Probando contraseña '{password}'")
        time.sleep(0.5)

        if random.random() < 0.2:
            print(f"[!] ¡Contraseña encontrada!: {password}")
            logging.info(f"Éxito: Contraseña '{password}' encontrada en intento {attempt}")
            return True
    
    print("[-] No se pudo encontrar la contraseña.")
    logging.warning("Fallo: No se encontró ninguna contraseña después de múltiples intentos.")
    return False

if __name__ == "__main__":
    simulate_brute_force("login.example.com")