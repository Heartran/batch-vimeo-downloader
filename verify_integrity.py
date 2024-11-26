import os
import hashlib
from dotenv import load_dotenv

# Carica le variabili dall'ambiente
load_dotenv()

def get_file_checksum(file_path, hash_algorithm='sha256'):
    hash_function = hashlib.new(hash_algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_function.update(chunk)
    except FileNotFoundError:
        return None
    return hash_function.hexdigest()

def verify_directory_integrity(directory_path):
    file_checksums = {}
    if not os.path.isdir(directory_path):
        print(f"Errore: Il percorso {directory_path} non esiste o non è una directory.")
        return None

    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = get_file_checksum(file_path)
            if checksum:
                file_checksums[file_path] = checksum
            else:
                print(f"Errore nella lettura del file: {file_path}")

    return file_checksums

def main():
    directory_path = os.getenv("FOLDER_PATH")
    if not directory_path:
        print("Errore: FOLDER_PATH non definito nelle variabili di ambiente.")
        return

    checksums = verify_directory_integrity(directory_path)
    if checksums:
        for file_path, checksum in checksums.items():
            print(f"File: {file_path} - Checksum: {checksum}")

if __name__ == "__main__":
    main()
