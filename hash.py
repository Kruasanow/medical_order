import hashlib

def hashed_data(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    # print(f"hashed_data is {hashed_data}")
    return hashed_data
# print(hashed_data('passw'))