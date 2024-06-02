 DomainBuster

DomainBuster is a Python tool for subdomain enumeration and directory brute-forcing. It combines both methods to discover subdomains and hidden directories on a target domain.

 Features
- Subdomain enumeration using wordlists
- Directory brute-forcing to find hidden directories
- Flexible command-line interface for specifying target URL, subdomain wordlist, and directory wordlist
- Lightweight and easy-to-use

 Installation
1. Clone the repository:
    ```
    git clone https://github.com/your_username/DomainBuster.git
    ```
2. Navigate to the directory:
    ```
    cd DomainBuster
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

 Usage

	python domainbuster.py -u <target_url> -s <subdomain_wordlist> -d <directory_wordlist>

javascript


Replace `<target_url>` with the URL of the target domain, `<subdomain_wordlist>` with the path to the wordlist for subdomain enumeration, and `<directory_wordlist>` with the path to the wordlist for directory brute-forcing.

 Examples
1. Enumerate subdomains:
    ```
    python domainbuster.py -u example.com -s subdomains.txt
    ```
2. Brute-force directories:
    ```
    python domainbuster.py -u example.com -d directories.txt
    ```

 Credits
DomainBuster was created by [Your Name].

 License
This project is licensed under the [MIT License](LICENSE).
