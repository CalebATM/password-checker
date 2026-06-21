# Password Checker

This password checker is a command-line tool that checks if your password has been compromised in known data breaches without ever exposing your actual password.

## The Problem It Solves
The main problem with using websites like https://haveibeenpwned.com to check your passwords is that information entered into search forms may be stored for an undisclosed amount of time and could potentially be shared with third-party servers like Google. (See https://haveibeenpwned.com/privacy#Logging.) Trusting others with your password leaves your information vulnerable to exposure or interception. However, this password checker tool ensures that neither your password nor its full cryptographic hash leaves your computer.

## How It Works
* **Secure Input Handling:** The application uses the `pwinput` library to securely capture user input. This ensures that the password is never saved in the command-line history on your machine and is masked by "*" characters to prevent shoulder-surfing (when attackers secretly look over your shoulder to observe your screen).
* **K-Anonymity:** The script hashes the password using the SHA-1 algorithm, so the actual password never gets sent over the internet. 
* **Secure API Communication:** It takes only the *first 5 characters* of the hash and sends them to the pwnedpasswords API, meaning that the hash of your password (and thereby your password) is never communicated to the API. 
* **Local Verification:** The API returns a list of all leaked hashes that match the first five characters. The script then compares your hash with the results to see if there is a match, ensuring your full password and its hash never leave your computer.

## Installation & Setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python checkmypassword.py`