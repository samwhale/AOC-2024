# Parse a list of data. Each entry is a line in the file.
def parseData(path: str):
    with open(path, 'r') as file:
        data = file.readlines()
        
        formattedData = [row.strip().split("   ") for row in data]
        
        result = []
        for row in formattedData:
            result.append([int(x) for x in row])
        
        return result
