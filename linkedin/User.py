class User:

    def __init__(self, forename, surname, company, position):
        self.forename = forename
        self.surname = surname
        self.company = company
        self.position = position
        self.industry = ""
        self.city = ""
        self.country = ""

    def __str__(self):
        return self.forename + "," + self.surname + "," + self.company + \
            "," + self.position + "," + self.industry + "," + self.city + \
            "," + self.country
