# pip install cryptography
# pip install pywin32

import win32com.client as client, time
from cryptography.fernet import Fernet

usuario_criptografado = b'gAAAAABf14wQWmqhkF_Z-JbYdydbl2gQ6rOzOWAUEaKyFpTdGvDBRGolCNXZ-0yjZNigphivzsNwqO92zJb6FNkx_uR5ziD9ew=='
senha_criptografada = b'gAAAAABf05t0I1umWi9_tE45aAvptf7fcCbv8SCtLD-KjICA3hygmku-NGrBvJ2tbkHuHAxNXb8uYm59IITzB5V-1NCSYw1Hsw=='
path_criptografado= b'gAAAAABf16dQ2pdRTTjvl6HSKMm5h7sLSd4R75rsfyBbkaXG4Y8JK3BaYFxv6pykBPj4QWQSAftMhNLx4CLvvHQR-cx8q5qtTSSWUgxtwHChgsrvdhw3j88bcFIxuA92EarqaWHhE8w2'


def crypt(ciphered_text):
    key = b'djNnswBmpi98AV-j6BeuzDyiGF1Y_5JQir4NQWoQ_N4='
    cipher_suite = Fernet(key)
    unciphered_text = (cipher_suite.decrypt(ciphered_text))
    return bytes(unciphered_text).decode("utf-8")


def run_as(required_command, required_password, required_user):
    shell = client.Dispatch("WScript.shell")
    shell.Run(f'runas /user:{required_user} "{required_command}"')

    time.sleep(0.5)
    shell.SendKeys(f"{required_password}\r\n", 0)
    time.sleep(0.5)

run_as(crypt(path_criptografado), crypt(senha_criptografada), crypt(usuario_criptografado))
## python -OO -m py_compile



