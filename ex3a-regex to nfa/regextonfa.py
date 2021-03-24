if __name__ == '__main__':
    states = {
    "1": "0 a 1",
    "2": "0 e 1 a 2 e 5 0 e 3 b 4 e 5",
    "3": "0 a 1 b",
    "4": "0 e 1 a 2 e 3 0 e 3 2 e 1"
    }
    choices = ["1. a", "2. a/b", "3. ab", "4. a*"]
    while(True):
        print("enter your choice")
        for i in choices:
            print(i)

        choice = input()
        if(choice == "1"):
            print(states["1"])
        elif(choice == "2"):
            print(states["2"])
        elif(choice == "3"):
            print(states["3"])
        elif(choice == "4"):
            print(states["4"])

        print("enter Q to exit")
        if input() == "Q":
            break