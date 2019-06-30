from visualization.network import create_nodes
from visualization.network import create_edges

def main():

    try:
        create_nodes()
        #create_edges([30,10,50,7,3], "industry")
        #create_edges([50,20,20,7,3], "company")
        #create_edges([20,3,7,50,20], "country")
        create_edges([0,0,80,0,20], "demo")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
