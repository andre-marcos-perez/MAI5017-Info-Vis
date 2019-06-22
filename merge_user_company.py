import pycountry as pc
from linkedin.User import User
from linkedin.Company import Company

def main():

    USR_FILENAME = "data/user.csv"
    COM_FILENAME = "data/company.csv"
    OUT_FILENAME = "data/user_final.csv"
    DAT_DIR = "data/"

    try:
        users = list()
        companies = list()
        countries = list()
        for country in list(pc.countries):
            countries.append(country.name)
        with open(COM_FILENAME, mode="r", encoding="utf-8") as file:
            line = file.readline()
            line = file.readline()
            while line:
                line = line.split(";")
                company = Company(line[0])
                company.industry = line[1].rstrip("\n").replace(",", "")
                companies.append(company)
                line = file.readline()
        with open(USR_FILENAME, mode="r", encoding="utf-8") as file:
                line = file.readline()
                line = file.readline()
                while line:
                    line = line.split(",")
                    user = User(line[0], line[1], line[2], line[3])
                    for company in companies:
                        if user.company.strip() == company.name.strip():
                            user.industry = company.industry
                            break
                    location = line[5].rstrip("\n").split(";")
                    if len(location) == 3:
                        user.city = location[0].replace("Area", "").strip()
                        user.country = location[2].replace("Area", "").strip()
                    elif len(location) == 2:
                        if "Area" in location[0]:
                            user.city = location[0].replace("Area", "").strip()
                            user.country = location[1].replace("Area", "").strip()
                        else:
                            if location[1].replace("Area", "").strip() in countries:
                                user.city = location[0].replace("Area", "").strip()
                                user.country = location[1].replace("Area", "").strip()
                            else:
                                user.city = location[0].replace("Area", "").strip()
                    elif len(location) == 1 and location[0] != "" and location[0] != "Other":
                        if "Area" not in location[0]:
                            user.country = location[0].replace("Area", "").strip()
                    users.append(user)
                    line = file.readline()
        with open(OUT_FILENAME, mode="w", encoding="utf-8") as file:
            file.write("Forename,Surname,Company,Position,Industry,City,Country\n")
            for user in users:
                file.write("%s\n" % user)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
