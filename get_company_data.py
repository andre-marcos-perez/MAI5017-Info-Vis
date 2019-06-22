import pandas as pd
from os import listdir
from bs4 import BeautifulSoup
from linkedin.Company import Company

def main():

    INP_FILENAME = "data/user.csv"
    OUT_FILENAME = "data/company.csv"
    DAT_DIR = "data/companies/"

    try:
        companies = list()
        data = pd.read_csv(INP_FILENAME)
        data = list(data["Company"].unique())
        for company_name in data:
            company = Company(company_name.strip())
            companies.append(company)
        for filename in listdir(DAT_DIR):
            if filename.endswith(".html"):
                name = filename.split(".")[0]
                for company in companies:
                    if company.name == name:
                        with open(DAT_DIR + filename, mode="r", encoding="utf-8") as file:
                            soup = BeautifulSoup(file, 'html.parser')
                            elements = soup.find_all(attrs={"class": "search-typeahead-v2__hit-info"})
                            for element in elements:
                                try:
                                    company_name = element.find_all(attrs={"class": "search-typeahead-v2__hit-text"})[0].getText().strip()
                                    company_industry = element.find_all(attrs={"class": "search-typeahead-v2__hit-subtext"})[0].getText().strip()
                                    if company_name.lower() in company.name.lower():
                                        if "School" in company_industry:
                                            company.industry = "School"
                                            break
                                        elif "Company •" in company_industry:
                                            company.industry = company_industry.split("•")[1].strip()
                                            break
                                except Exception as e:
                                    continue
                        print(company)
        with open(OUT_FILENAME, mode="w", encoding="utf-8") as file:
            file.write("Company;Industry\n")
            for company in companies:
                file.write("%s\n" % company)
    except Exception as e:
        raise

if __name__ == "__main__":
    main()
