import json

def getChars(ctext):
    pass

def loadCipherText():
    file_path = "cipher-texts/2021.json"
    my_file = open(file_path)
    my_obj = json.load(my_file)
    my_file.close()

    ctext = my_obj["challenges"][0]["ctext"]

    return ctext

def main():
    ctext = loadCipherText()
    print(getChars(ctext))

if __name__ == "__main__":
    main()