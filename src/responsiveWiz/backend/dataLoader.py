import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from responsiveWiz.utils import print

import json


def getJsonData(path: str) -> dict:
    jsonPath = os.path.join(path)
    print(f"Loading JSON from: {jsonPath}", "blue")
    
    with open(jsonPath, 'r') as file:
        data = json.load(file)
    
    return data

def main() -> None:
    getJsonData('src/responsiveWiz/data/responsiveOptions.json')

if __name__ == '__main__':
    main()