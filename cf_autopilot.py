from retriever import Retriever

def main():
    with open("cf_userlist.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for userid in lines:
            retriever = Retriever()
            retriever.start(cf_autopilot=True, userid=userid)

if __name__ == '__main__':
    main()
