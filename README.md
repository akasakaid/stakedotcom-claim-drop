# STAKEDOTCOM CLAIM DROP

## a program to help the process of claiming prizes at the end of the week
---
### HOW TO USE?
the program is very easy to use. Make sure you have python3 installed on your device

1. Clone this repository

    ```
    git clone https://github.com/akasakaid/stakedotcom-claim-drop
    ```

2. Go to the repository folder

    ```
    cd stakedotcom-claim-drop
    ```

3. Install all necessary modules

    ```
    python3 -m pip install -r requirements.txt
    ```

4. Run the program

    ```
    python3 claim.py
    ```

5. The program will not run directly because there are several files that you have to fill in. After running the program for the first time will be 3 files: coin.txt, token.txt, key.txt.

- fill in the coin.txt with the coin you want to claim
- fill in the token.txt with your account token
- fill in the key.txt with the key of the anti-captcha, because this claim program requires the help of an anti-captcha to bypass the captcha.

6. After the coin.txt, token.txt, key.txt is filled, run the program again

	```
	python3 claim.py
	```

### NOTE
if you have multiple accounts, you can put tokens on every line. Example:

token 1<br>
token 2<br>
Token 3<br>

---

