import pyperclip
import time
import re

# Percorso del file in cui verranno salvati i link
file_path = r"C:\Users\f.viola\OneDrive\Strumenti\vimeo-downloader\vimeo-downloader-main\vimeo_links.txt"

# Espressione regolare per rilevare un link di Vimeo
vimeo_regex = re.compile(r'(https?://vimeo\.com/\S+)')

def save_link_to_file(link):
    """Salva il link al file specificato."""
    try:
        with open(file_path, 'a') as file:
            file.write(link + '\n')
        print(f"[DEBUG] Link salvato correttamente nel file: {link}")
    except Exception as e:
        print(f"[ERROR] Impossibile salvare il link nel file: {e}")

def main():
    last_copied = ""
    while True:
        # Ottieni il contenuto attuale degli appunti
        try:
            copied_text = pyperclip.paste()
            print(f"[DEBUG] Contenuto degli appunti attuale: {copied_text}")
        except Exception as e:
            print(f"[ERROR] Impossibile ottenere il contenuto degli appunti: {e}")
            continue
        
        # Se il contenuto è cambiato ed è un link di Vimeo, salvalo nel file
        if copied_text != last_copied:
            print(f"[DEBUG] Rilevato nuovo contenuto negli appunti.")
            if vimeo_regex.search(copied_text):
                last_copied = copied_text
                print(f"[DEBUG] Link di Vimeo rilevato: {copied_text}")
                save_link_to_file(copied_text)
            else:
                print(f"[DEBUG] Il contenuto non è un link di Vimeo.")
        
        # Attendi un po' prima di controllare di nuovo
        time.sleep(1)

if __name__ == "__main__":
    print("[DEBUG] Avvio del programma di monitoraggio degli appunti per link di Vimeo.")
    main()
