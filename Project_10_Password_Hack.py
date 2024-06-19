import itertools
import string
import time

def brute_force_password_cracker(target_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    start_time = time.time()

    for password_length in range(1, 9):
        for guess in itertools.product(characters, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                end_time = time.time()
                time_taken = end_time - start_time
                return guess, attempts, time_taken

    return None, attempts, None

if __name__ == "__main__":
    target_password = input("Enter the password to hack: ")
    print(f"Trying to hack the password: {target_password}")
    hacked_password, attempts, time_taken = brute_force_password_cracker(target_password)

    if hacked_password:
        print(f"Password '{hacked_password}' was hacked in {attempts} attempts and {time_taken:.2f} seconds.")
    else:
        print("Failed to hack the password.")