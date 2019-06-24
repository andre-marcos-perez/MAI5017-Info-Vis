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

    def __eq__(self, other):
        return self.forename == other.forename and self.surname == other.surname and self.company == other.company and self.position == other.position

    def correlation(self, other, weight):
        corr = 0
        if self != other:
            corr = corr + weight[0] if (self.company == other.company) else corr
            corr = corr + weight[1] if (self.position.lower() == other.position.lower()) else corr
            corr = corr + weight[2] if (self.industry == other.industry) else corr
            corr = corr + weight[3] if (self.city == other.city) else corr
            corr = corr + weight[4] if (self.country == other.country) else corr
        return corr / sum(weight)
