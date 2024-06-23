from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
import csv
#pip install all this stuff

filename = 'ligandsheet - Sheet1.csv' #downloaded, put in the same folder

#rows = []
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        search = (str(row)[2:-2])
        driver.get("https://pubchem.ncbi.nlm.nih.gov/#query="+search)
        time.sleep(15)
        smiles = driver.find_element(By.XPATH, '//*[@id="featured-results"]/div/div[2]/div/div[1]/div[2]/div[5]/div/span/span[2]/span').text
        #takes isomeric smiles, NOT canonical                                                                  
        #rows.append([search, smiles])
        #if it crashes midway (bc of a erroneous ligand) then copy paste from the terminal onto sheets
        print(smiles)

# field names
#fields = ['Ligand', 'SMILES']

# name of outputted csv file
#filename = "ligandlist.csv"

# writing to csv file
#with open(filename, 'w') as csvfile:
    # creating a csv writer object
    #csvwriter = csv.writer(csvfile)

    # writing the fields
    #csvwriter.writerow(fields)

    # writing the data rows
    #csvwriter.writerows(rows)


