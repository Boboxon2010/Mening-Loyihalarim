import os
import subprocess
import sys

# Terminal ranglari uchun
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def run_command(command):
    print(f"{YELLOW}➡️  {command}{RESET}")
    subprocess.check_call(command, shell=True)

def main():
    print(f"{GREEN}🚀 Python Data Science muhitini o‘rnatish boshlandi...{RESET}\n")

    # pip yangilash
    run_command(f"{sys.executable} -m pip install --upgrade pip")

    # Kutubxonalarni o‘rnatish
    packages = ["numpy", "pandas", "matplotlib", "jupyter", "scipy"]
    run_command(f"{sys.executable} -m pip install " + " ".join(packages))

    print(f"\n{GREEN}✅ Muhit tayyor! Endi siz quyidagilarni ishlatishingiz mumkin:{RESET}")
    print("""
📦 Kutubxonalar:
    - numpy
    - pandas
    - matplotlib
    - scipy
📘 Jupyter Notebook:
    jupyter notebook
    """)

if __name__ == "__main__":
    main()
