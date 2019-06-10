from linkedin.User import User
from linkedin.webscraper import scraper

def main():

    INP_FILENAME = "data/Connections.csv"
    OUT_FILENAME = "data/output.csv"
    ACC_FILENAME = "data/account.csv"

    users = list()
    try:
        with open(INP_FILENAME, mode="r", encoding="utf-8") as file:
                line = file.readline()
                line = file.readline()
                while line:
                    line = line.split(",")
                    if line[0] and line[1] and line[3] and line[4]:
                        user = User(line[0], line[1], line[3], line[4])
                        users.append(user)
                    line = file.readline()
        with open(ACC_FILENAME, mode="r", encoding="utf-8") as file:
            line = file.readline()
            line = line.split(",")
        scraper(users, line[0], line[1])
        # with open(OUT_FILENAME, mode="w", encoding="utf-8") as file:
        #         file.write("Forename,Surname,Company,Position,Industry,Location\n")
        #         for user in users:
        #             file.write("%s\n" % user)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
