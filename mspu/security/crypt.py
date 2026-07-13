import json
import base64
import hashlib
from cryptography.fernet import Fernet


def create_key(keypath: str):
    # Generate a key
    key = Fernet.generate_key()

    # Save the key securely
    with open(keypath, 'wb') as f:
        f.write(key)


def load_key(keypath: str) -> bytes:
    # Load key from file
    with open(keypath, 'rb') as f:
        key = f.read()
    return key


def encrypt_txt(key: bytes, txt: str) -> bytes:
    # Serialize and encrypt the txt
    cipher = Fernet(key)
    encrypted_credentials = cipher.encrypt(txt)
    return encrypted_credentials


def decrypt_txt(key: bytes, txt: bytes) -> bytes:
    # Decrypt the credentials
    cipher = Fernet(key)
    decrypted_credentials = cipher.decrypt(txt)
    return decrypted_credentials


def encrypt_file(key: bytes, filepath: str):
    # Load the credentials
    with open(filepath, 'rb') as f:
        txt = f.read()
    # Serialize and encrypt the txt
    encrypted_credentials = encrypt_txt(key, txt)
    # Save the encrypted file
    file, ext = filepath.rsplit('.', 1)
    filepath = f'{file}_.{ext}'
    with open(filepath, 'wb') as f:
        f.write(encrypted_credentials)


def decrypt_file(key: bytes, filepath: str, to_json: bool = True):
    # Load the credentials
    with open(filepath, 'rb') as f:
        txt = f.read()
    # Decrypt the credentials
    decrypted_credentials = decrypt_txt(key, txt).decode()
    # Load the credentials into a dictionary
    if to_json:
        decrypted_credentials = json.loads(decrypted_credentials)
    return decrypted_credentials


def ha64(txt: str):
    txt = hashlib.sha256(txt.encode()).digest()
    return base64.urlsafe_b64encode(txt)

if __name__ == '__main__':
    fp = 'c:/files'
    # create_key(f'{fp}/my-key.json')

    key = load_key(f'{fp}/my-key.json')

    key = hashlib.sha256('my-key'.encode()).digest()
    key = base64.urlsafe_b64encode(key)
    fl = 'my-key.json'
    # encrypt_file(key, f'{fp}/{fl}')

    key = decrypt_file(key, f'{fp}/my-key_.json', False)
    db_cred = decrypt_file(key, f'{fp}/credentials_.json')

    print(db_cred)
