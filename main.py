from linkedin.User import User

def main():

    INPUT_FILENAME = "data\Connections.csv"

    users = list()
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as file:
            line = file.readline()
            line = file.readline()
            while line:
                line = line.split(",")
                if line[0] and line[1] and line[3] and line[4]:
                    user = User(line[0], line[1], line[3], line[4])
                    users.append(user)
                    print(user)
                line = file.readline()

if __name__ == "__main__":
    main()
