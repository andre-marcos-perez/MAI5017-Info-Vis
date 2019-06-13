from os import listdir
from bs4 import BeautifulSoup
from linkedin.User import User

def main():

    INP_FILENAME = "data/Connections.csv"
    OUT_FILENAME = "data/user.csv"
    DAT_DIR = "data/users/"

    try:
        users = list()
        with open(INP_FILENAME, mode="r", encoding="utf-8") as file:
                line = file.readline()
                line = file.readline()
                while line:
                    line = line.split(",")
                    if line[0] and line[1] and line[3] and line[4]:
                        user = User(line[0], line[1], line[3], line[4])
                        users.append(user)
                    line = file.readline()
        for filename in listdir(DAT_DIR):
            if filename.endswith(".html"):
                name = filename.split(".")
                name = name[0].split("_")
                for user in users:
                    if user.forename == name[0] and user.surname == name[1]:
                        with open(DAT_DIR + filename, mode="r", encoding="utf-8") as file:
                            soup = BeautifulSoup(file, 'html.parser')
                            location = soup.find_all(attrs={"class": "pv-top-card-section__location"})[0].getText()
                            user.location = location.strip().replace("\n", "").replace(",", ";")
                        print(user)
        with open(OUT_FILENAME, mode="w", encoding="utf-8") as file:
            file.write("Forename,Surname,Company,Position,Industry,Location\n")
            for user in users:
                file.write("%s\n" % user)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
