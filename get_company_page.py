import pandas as pd
from linkedin.Company import Company
from linkedin.company_scraper import company_scraper

def main():

    INP_FILENAME = "data/user.csv"
    ACC_FILENAME = "data/account.csv"

    try:
        companies = list()
        data = pd.read_csv(INP_FILENAME)
        data = list(data["Company"].unique())
        for company_name in data:
            company = Company(company_name)
            companies.append(company)
        with open(ACC_FILENAME, mode="r", encoding="utf-8") as file:
            line = file.readline()
            line = line.split(",")
        company_scraper(companies, line[0], line[1])
    except Exception as e:
        raise

if __name__ == "__main__":
    main()
