import secrets
import base64

def generate_base64_key(byte_length=32):
    random_bytes = secrets.token_bytes(byte_length)
    base64_key = base64.b64encode(random_bytes).decode('utf-8')
    return base64_key

key = generate_base64_key()
print(key)
