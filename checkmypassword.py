import requests
import hashlib
import pwinput
import sys


def request_api_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check API and try again"
        )
    return response


def get_password_leaks_count(hashes, input_hash):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == input_hash:
            return count
    return 0


def pwned_api_check(password):
    # Check if password in API response
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5)
    return get_password_leaks_count(response, tail)


def main():
    print("---- Pwned Password Checker ----")
    password = pwinput.pwinput(prompt="Please enter the password to check: ", mask="*")

    if not password:
        print("No password entered. Exiting...")
        return

    count = pwned_api_check(password)
    del password

    if count:
        print(
            f"\n[WARNING] That password has been exposed {count} time(s) in known data breaches. Please change it ASAP!"
        )
    else:
        print(
            "That password was NOT found in any data leaks. Your password is most likely secure."
        )
    return "All done!"


if __name__ == "__main__":
    sys.exit(main())
