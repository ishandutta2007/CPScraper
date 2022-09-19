from retriever import Retriever


def main():
    with open("cf_userlist.txt") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for i, userid in enumerate(lines):
            retriever = Retriever()
            retriever.start(cf_autopilot=True, userid=userid, cf_serial_no=(i + 1))


if __name__ == "__main__":
    main()
