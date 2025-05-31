# Red Team Bruteforce Toolkit

Herramienta de ejemplo para realizar simulaciones de ataques de fuerza bruta y análisis automatizado de logs.

## 📦 Requisitos

- Python 3.11+
- Docker
- Dependencias en `requirements.txt`

## 🛠️ Instalación

```bash
# Clonar repo
git clone https://github.com/Pruebillas/redteam-bruteforce-toolkit.git 
cd redteam-bruteforce-toolkit

# Construir imagen Docker
docker build -t redteam/bruteforce .

# Ejecutar ataque simulado
docker run --rm redteam/bruteforce