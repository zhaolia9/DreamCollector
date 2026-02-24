# test_frontend.py
"""
Console-based test for Aurelia API
Performs full CRUD for all entities, using read_all before each operation
to ensure data can be retrieved successfully.
"""

import requests
from pprint import pprint

BASE_URL = "http://127.0.0.1:8000"

print("=== Starting Aurelia API Front-End Test ===\n")

# ---------------------------
# USERS CRUD
# ---------------------------
print(">>> USERS CRUD")

print("\nCurrent users:")
resp = requests.get(f"{BASE_URL}/users")
pprint(resp.json())

print("\nCreating a user...")
user_data = {"name": "Test User", "email": "testuser@example.com"}
requests.post(f"{BASE_URL}/users", json=user_data)
print("After creation:")
resp = requests.get(f"{BASE_URL}/users")
pprint(resp.json())

print("\nUpdating the user...")
users = resp.json()
user_id = users[-1]["id"]
updated_data = {"name": "Updated User", "email": "updated@example.com"}
requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
print("After update:")
resp = requests.get(f"{BASE_URL}/users")
pprint(resp.json())

print("\nDeleting the user...")
requests.delete(f"{BASE_URL}/users/{user_id}")
print("After deletion:")
resp = requests.get(f"{BASE_URL}/users")
pprint(resp.json())

# ---------------------------
# DREAMS CRUD
# ---------------------------
print("\n>>> DREAMS CRUD")

print("\nCurrent dreams:")
resp = requests.get(f"{BASE_URL}/dreams")
pprint(resp.json())

print("\nCreating a dream...")
dream_data = {
    "user_id": 1,  # make sure this user exists
    "title": "Flying",
    "description": "I was flying over mountains",
    "date": "2026-02-23",
    "mood": "Excited",
    "vividness": 8
}
requests.post(f"{BASE_URL}/dreams", json=dream_data)
print("After creation:")
resp = requests.get(f"{BASE_URL}/dreams")
pprint(resp.json())

print("\nUpdating the dream...")
dreams = resp.json()
dream_id = dreams[-1]["id"]
updated_dream = {
    "user_id": 1,
    "title": "Flying Higher",
    "description": "Flying above clouds",
    "date": "2026-02-23",
    "mood": "Thrilled",
    "vividness": 9
}
requests.put(f"{BASE_URL}/dreams/{dream_id}", json=updated_dream)
print("After update:")
resp = requests.get(f"{BASE_URL}/dreams")
pprint(resp.json())

print("\nDeleting the dream...")
requests.delete(f"{BASE_URL}/dreams/{dream_id}")
print("After deletion:")
resp = requests.get(f"{BASE_URL}/dreams")
pprint(resp.json())

# ---------------------------
# SYMBOLS CRUD
# ---------------------------
print("\n>>> SYMBOLS CRUD")

print("\nCurrent symbols:")
resp = requests.get(f"{BASE_URL}/symbols")
pprint(resp.json())

print("\nCreating a symbol...")
symbol_data = {"name": "Sun", "description": "Bright celestial body"}
requests.post(f"{BASE_URL}/symbols", json=symbol_data)
print("After creation:")
resp = requests.get(f"{BASE_URL}/symbols")
pprint(resp.json())

print("\nUpdating the symbol...")
symbols = resp.json()
symbol_id = symbols[-1]["id"]
updated_symbol = {"name": "Sun Updated", "description": "Shining star"}
requests.put(f"{BASE_URL}/symbols/{symbol_id}", json=updated_symbol)
print("After update:")
resp = requests.get(f"{BASE_URL}/symbols")
pprint(resp.json())

print("\nDeleting the symbol...")
requests.delete(f"{BASE_URL}/symbols/{symbol_id}")
print("After deletion:")
resp = requests.get(f"{BASE_URL}/symbols")
pprint(resp.json())

# ---------------------------
# POEMS CRUD
# ---------------------------
print("\n>>> POEMS CRUD")

print("\nCurrent poems:")
resp = requests.get(f"{BASE_URL}/poems")
pprint(resp.json())

print("\nCreating a poem...")
poem_data = {
    "author_id": 1,  # ensure this user exists
    "dream_id": 1,   # ensure this dream exists
    "content": "Flying high above the clouds",
    "created_at": "2026-02-23"
}
requests.post(f"{BASE_URL}/poems", json=poem_data)
print("After creation:")
resp = requests.get(f"{BASE_URL}/poems")
pprint(resp.json())

print("\nUpdating the poem...")
poems = resp.json()
poem_id = poems[-1]["id"]
updated_poem = {
    "author_id": 1,
    "dream_id": 1,
    "content": "Flying higher, touching stars",
    "created_at": "2026-02-23"
}
requests.put(f"{BASE_URL}/poems/{poem_id}", json=updated_poem)
print("After update:")
resp = requests.get(f"{BASE_URL}/poems")
pprint(resp.json())

print("\nDeleting the poem...")
requests.delete(f"{BASE_URL}/poems/{poem_id}")
print("After deletion:")
resp = requests.get(f"{BASE_URL}/poems")
pprint(resp.json())

# ---------------------------
# DREAM SYMBOLS CRUD
# ---------------------------
print("\n>>> DREAM SYMBOLS CRUD")

print("\nCurrent dream-symbol links:")
resp = requests.get(f"{BASE_URL}/dreamsymbols")
pprint(resp.json())

print("\nCreating a dream-symbol link...")
dream_symbol_data = {"dream_id": 1, "symbol_id": 1}  # ensure these exist
requests.post(f"{BASE_URL}/dreamsymbols", json=dream_symbol_data)
print("After creation:")
resp = requests.get(f"{BASE_URL}/dreamsymbols")
pprint(resp.json())

print("\nDeleting the dream-symbol link...")
requests.delete(f"{BASE_URL}/dreamsymbols?dream_id=1&symbol_id=1")
print("After deletion:")
resp = requests.get(f"{BASE_URL}/dreamsymbols")
pprint(resp.json())

print("\n=== Test Finished ===")