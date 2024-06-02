import requests
import argparse
import urllib3  # Add this line
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

def get_banner():
    banner = """
         ___                     _        ___             __           
        / _ \ ___   __ _  ___ _ (_)___   / _ ) __ __ ___ / /_ ___  ____
       / // // _ \ /  ' \/ _ `// // _ \ / _  |/ // /(_-</ __// -_)/ __/
      /____/ \___//_/_/_/\_,_//_//_//_//____/ \_,_//___/\__/ \__//_/                                                                              
    """
    print(blue + banner)

def get_arguments():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u","--url",dest="url",help="sepcify the target url to find subdomains")
    parse.add_argument("-s","--sub-domain",dest="subdomain",help="sepcify the wordlist for finding subdomains")
    parse.add_argument("-d","--directory",dest="directory",help="specify the worlist directory to find hidden directory ")
  
    return parse.parse_args()


def get_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
      pass
    except requests.exceptions.InvalidURL:
        pass
    except requests.exceptions.ReadTimeout:
        pass
 
def subdomain_bruteforce(url,wordlists):

    with open(wordlists,"r") as wf:
        for line  in wf:
            subdomains = line.strip()
            full_url = f"https://{subdomains}.{url}"
            try:
                resp = get_request(full_url)
                if resp and resp.status_code == 200:
                    print(green + f"[+] Subdomain exists ----> {full_url} (200)")
                elif resp and resp.status_code == 301:
                    print(blue + f"[+] subdomains redirects ----> {full_url} (301)")
            except urllib3.exceptions.LocationParseError :
                continue



def directory_bruteforce(url,wordlists):

    with open(wordlists,"r") as wf:
        for line  in wf:
            lines = line.strip()
           
            full_url = f"https://{url}/{lines}"
            resp = get_request(full_url)

            if resp and resp.status_code == 200:
                print(green + f"[+] Hidden directories are now visible to the eyes  ----> {full_url} (200)")
            elif resp and resp.status_code == 301:
                print(blue + f"[+] redirect  ---->  {full_url} (301)")
get_banner()
def main():
    args = get_arguments()
    url = args.url
    subdomain = args.subdomain
    directory = args.directory
    
    try:
        if not url:
            print(yellow + "[!] please specify the url using -u or --url")
            return

        if subdomain and not directory:
            print(yellow + "[*] subdomains bruteforcing....")
            subdomain_bruteforce(url,subdomain)
        
        elif directory:
            print(yellow + "[*] directory bruteforcing....\n")
            directory_bruteforce(url,directory)
            return
        else:
            print(yellow + "[!] please specify the wordlist use  -s or -d option eg: -s or -d /path/to/worldist.txt")

       
        
    except KeyboardInterrupt:
        print(red + "Ctrl + C , Exiting....")
if __name__ =="__main__":
    main()