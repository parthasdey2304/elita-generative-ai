# elita-generative-ai
This is a Generative AI script that runs natively on a terminal and it uses Rapid API's api to run in the background!

# Installation
### You would need git to be installed in your system first
+ Installing in `apt` :
``` sh
sudo apt install git -y
```

+ Installing in `pacman` :
``` sh
sudo pacman -Sy --noconfirm git
```

### Then you need to install Python on your system
+ Installing python in `apt` :
```sh
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python-is-python3 -y
```

+ Installing python in `pacman` :
```sh
sudo pacman -Sy --noconfirm python
```



Clone the repository `elita-generative-ai` :
``` sh
git clone https://github.com/parthasdey2304/elita-generative-ai.git
```

Enter the repository :
``` sh
cd elita-generative-ai
```

+ Headover to the website [RapidAPI](https://rapidapi.com/truongvuhung102/api/chatgpt-best-price/details) to get the API keys : 
+ Subscribe to the Test API with whatever plan you are comfortable, and make the payment.
+ Scroll down to header parameters in the EndPoint tab.
+ Grab your RapidAPI key.
+ Paste it in the python code for `elita.py` in the `headers` dictionary in `X-RapidAPI-Key` using vim.
+ Use the command `vim elita.py` and the paste the API key and press `ESC + :x` and exit the vim:
```python
    26  headers = {
    27      "content-type": "application/json",
    28      "X-RapidAPI-Key": "PASTE_THE_API_KEY_HERE",
    29      "X-RapidAPI-Host": "chatgpt-best-price.p.rapidapi.com"
    30  }
```

Run the `setup.sh` file : 
``` sh
./setup.sh
```

# Usage
Open the terminal
```
Ctrl + Alt + T
```

Now type `elita 'WHAT YOU WANT TO ASK INSIDE QUOTES'`
```sh
elita 'give me the code for palindrome number in java!'
```

Output
```bash
┌──(partha㉿xiaomi)-[~]
└─$ elita 'give me the code for palindrome number in java!'
Yes Sir! Generating...
Here's the code for checking if a number is a palindrome in Java:

|java
public class PalindromeNumber {
    public static void main(String[] args) {
        int number = 12321; // Change this number to test different values

        if (isPalindrome(number)) {
            System.out.println(number + " is a palindrome.");
        } else {
            System.out.println(number + " is not a palindrome.");
        }
    }

    public static boolean isPalindrome(int number) {
        int palindrome = number; // Copy the number to a temporary variable
        int reverse = 0;

        while (palindrome != 0) {
            int remainder = palindrome % 10;
            reverse = reverse * 10 + remainder;
            palindrome = palindrome / 10;
        }

        return number == reverse;
    }
}

+------------------------------------------------------------------------------+

In this code, you can change the value of the `number` variable to test different numbers. The `isPalindrome` method checks if a number is a palindrome by reversing it and comparing it to the original number. If they match, it returns `true`, indicating that the number is a palindrome. If they don't match, it returns `false`.
```

# Directory Structure
```sh
┌──(partha㉿xiaomi)-[~/elita-generative-ai]
└─$ tree
.
├── elita
├── elita.py
├── LICENSE
├── README.md
├── remove.sh
└── setup.sh

1 directory, 6 files
```

# Contributing
We welcome contributions from the community! We welcome your contributions to improve the project. If you'd like to contribute to elita-generative-ai, please read the following guidelines on how to contribute:
+ Fork the repository and create a new branch for your changes.
+ Make your changes to the code.
+ Test your changes thoroughly.
+ Commit your changes with a clear and descriptive message.
+ Push your changes to your fork.
+ Create a pull request and wait for me to verify and then merge it to the main branch.

# THANK YOU COMMUNITY!!!!
 
