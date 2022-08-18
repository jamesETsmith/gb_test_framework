import xmltodict
import json

def main():
    with open("output.xml", "r") as f:
        data = xmltodict.parse(f.read())

    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()
