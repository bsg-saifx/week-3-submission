import requests

def main():
    r = requests.get("https://httpbin.org/get")
    print(r.json())

if __name__ == "__main__":
    main()

