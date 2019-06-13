class Company:

    def __init__(self, name):
        self.name = name
        self.industry = ""

    def __str__(self):
        return self.name + "," + self.industry
