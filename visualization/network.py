from linkedin.User import User

def create_nodes():

    INP_FILENAME = "data/user_final.csv"
    OUT_FILENAME = "data/nodes.csv"

    try:
        id = 1;
        with open(INP_FILENAME, mode="r", encoding="utf-8") as input, open(OUT_FILENAME, mode="w", encoding="utf-8") as output:
            output.write("Id,Label,Forename,Surname,Company,Position,Industry,City,Country\n")
            input.readline()
            line = input.readline()
            while line:
                label = line.split(",")
                if "" not in label:
                    output.write(str(id) + "," + label[0] + " " + label[1] + "," + line)
                    id += 1
                line = input.readline()
    except Exception as e:
        raise

def create_edges(weight, label):

    INP_FILENAME = "data/user_final.csv"
    OUT_FILENAME = "data/edges_" + label + ".csv"

    try:
        users = list()
        with open(INP_FILENAME, mode="r", encoding="utf-8") as file:
                line = file.readline()
                line = file.readline()
                while line:
                    line = line.split(",")
                    if "" not in line:
                        user = User(line[0], line[1], line[2], line[3])
                        user.industry = line[4]
                        user.city = line[5]
                        user.country = line[6].rstrip("\n")
                        users.append(user)
                    line = file.readline()
        with open(OUT_FILENAME, mode="w", encoding="utf-8") as file:
            id = 1;
            header = ""
            for user in users:
                header = header + ";" + str(id)
                id = id + 1
            file.write("%s\n" % header)
            id = 1
            for userA in users:
                corr = str(id)
                for userB in users:
                    corr = corr + ";" + str(userA.correlation(userB, weight))
                id = id + 1
                file.write("%s\n" % corr)
    except Exception as e:
        raise
