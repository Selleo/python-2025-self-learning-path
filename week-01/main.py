import requests

def main():
    r = requests.get('https://selleo.com')
    print(r.status_code)


if __name__ == "__main__":
    main()
