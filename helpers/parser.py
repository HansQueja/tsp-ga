import pandas as pd
import math

def parser():

    print("\nParsing city.xlsx...")
    # Try to open the excel file and store it to a dataframe variable df
    try:
        df = pd.read_excel('city.xlsx')
        print("\nReading the excel file and converted to a dataframe.")

        # Lists to store the city matrix and distances per city
        city_nodes = {}
        distance_matrix = []

        # Get each city's coordinates
        for row in range(len(df)):
            curr = df.iloc[row]
            city_nodes[curr[0]] = [curr[1], curr[2]]

        # Compute for the distance matrix
        for i in range(len(city_nodes)):
            curr = []
            for j in range(len(city_nodes)):
                if i == j:
                    curr.append(float('inf'))
                else:
                    curr_city = city_nodes[i + 1]
                    trav_city = city_nodes[j + 1]
                    distance = math.sqrt(math.pow(curr_city[0]-trav_city[0], 2) + math.pow(curr_city[1]-trav_city[1], 2))
                    curr.append(round(distance, 3))
            
            distance_matrix.append(curr)

        print("Map has been parsed and ready for map logic.")

        return distance_matrix
                        
    # Error if the file cannot be found
    except FileNotFoundError:
        raise FileNotFoundError("Warning: No file found")

if __name__ == "__main__":
    parser()