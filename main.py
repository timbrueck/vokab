import json
from random import randint

file = open("data.json")
data = json.loads(file.read())
file.close()
voc = data["voc"]

def run():
    command = input("Test (0)\nAppend (1)")
    if command == "0":
        rng = randint(0, len(voc) - 1)
        used_voc = []
        while(True):
            random_voc = voc[rng]
            print("Whats \"" + random_voc["plain"] + "\" in " + data["meta"]["translatedLanguage"])
            random_voc_answer = input("")
            if random_voc_answer == random_voc["translated"]:
                print("You're right.")
                rng = randint(0, len(voc) - 1)
            else:
                print("Try again.")

    else:
        to_append_plain = input("Plain:")
        to_append_trans = input("Translated:")
        voc.append({"plain": to_append_plain, "translated": to_append_trans})
        json.dump(data, open("data.json", "w"))

if __name__ == "__main__":
    print("""
____    ____  ______    __  ___      ___      .______   
\   \  /   / /  __  \  |  |/  /     /   \     |   _  \ 
 \   \/   / |  |  |  | |  '  /     /  ^  \    |  |_)  |
  \      /  |  |  |  | |    <     /  /_\  \   |   _  < 
   \    /   |  `--'  | |  .  \   /  _____  \  |  |_)  |
    \__/     \______/  |__|\__\ /__/     \__\ |______/
""")
    print("Version 0.0.1")
    run()
