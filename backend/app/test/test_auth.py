from app.utils.auth import (
    hash_password,
    verify_password,
    create_user_token,
    decode_access_token
)

password = "Aayesha123"

# Hash password
hashed = hash_password(password)
print("Hashed Password:")
print(hashed)

# Verify password
result = verify_password(password, hashed)
print("\nPassword Match:")
print(result)

# Generate JWT Token
token = create_user_token(
    user_id=1,
    email="test@gmail.com"
)

print("\nGenerated Token:")
print(token)

# Decode Token
payload = decode_access_token(token)

print("\nDecoded Payload:")
print(payload)