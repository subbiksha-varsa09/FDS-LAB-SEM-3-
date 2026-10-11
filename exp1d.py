

from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher_suite = Fernet(key)

plain_text = b"Rajalakshmi Engineering College."

cipher_text = cipher_suite.encrypt(plain_text)

decrypted_text = cipher_suite.decrypt(cipher_text)


print("Original Data:", plain_text)
print("Encrypted Data:", cipher_text)
print("Decrypted Data:", decrypted_text)