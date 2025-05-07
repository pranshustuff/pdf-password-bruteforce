import PyPDF2
import itertools
import string
import multiprocessing

PDF_PATH = "input.pdf"
CHARSET = string.ascii_letters + string.digits
N = 5  # Replace with any password length

def try_passwords(start_chars):
    with open(PDF_PATH, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for combo in itertools.product(CHARSET, repeat=N - len(start_chars)):
            brute = start_chars + ''.join(combo)
            print(brute)
            if reader.decrypt(brute):
                print(f"Success! Password is: {brute}")
                return brute
    return None

def main():
    cpu_count = multiprocessing.cpu_count()
    print(f"Using {cpu_count} CPU cores...")

    pool = multiprocessing.Pool(cpu_count)

    # Split based on first character to divide the space
    start_prefixes = [c for c in CHARSET]

    try:
        results = pool.map(try_passwords, start_prefixes)
    finally:
        pool.close()
        pool.join()

    for result in results:
        if result:
            print(f"Found password: {result}")
            break
    else:
        print("Password not found.")

if __name__ == "__main__":
    main()
