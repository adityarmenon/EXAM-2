import hashlib
message = input("Enter the tetx: ")
md5 = hashlib.md5()
md5.update(message.encode())
digest = md5.digest()
hex_digest = digest.hex()
print("Hash: ", hex_digest)
