import PyPDF2
import itertools
import string

file_obj = open("input.pdf", 'rb')
pdf_obj = PyPDF2.PdfReader(file_obj)

# Include uppercase, lowercase, and digits
charset = string.ascii_letters + string.digits  # A-Z, a-z, 0-9

N = 5 # If password is 5 letters long

# Brute-force all N-character combinations from the charset
for combo in itertools.product(charset, repeat=N):
    brute = ''.join(combo)
    password = brute # Can also add string to this, if you know part of the password
    print(password)
    
    if pdf_obj.decrypt(password):
        print(f"Success! Password is: {password}")
        break
