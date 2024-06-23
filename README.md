# smiles-scraping

This script takes in a CSV file that has a list of the ligands you want. Make sure they're spelled correctly. 
Download the CSV file from sheets and put it in the same folder as this. 
In line 9,
filename = 'ligandsheet - Sheet1.csv' 

Change the filename to the name of your csv file that's inside your folder.

Now, in your bash terminal write 
python3 run.py


It's gonna run, just wait for it to print onto the terminal. Let the chrome tabs open on its own. it's ok
For instance if in your CSV it says 

Mercaptopurine
Cytarabine
Floxuridine
Pemetrexed
Carmustine
irinotecan
topotecan
doxorubicin
etoposide
novobiocin
quinolones 
teniposide
Mitoxantrone
Moxifloxacin
Grepafloxacin
Dexrazoxane
Epirubicin
Enoxacin
Pefloxacin
Ciprofloxacin
Trovafloxacin
Daunorubicin
Nalidixic Acid
Cinoxacin
Lomefloxacin
Doxorubicin
Gatifloxacin
Norfloxacin
Levofloxacin

it will print

C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=CC=CC=C5C4=O)O)(C(=O)C)O)N)O
CCCCC(=O)OCC(=O)[C@]1(C[C@@H](C2=C(C1)C(=C3C(=C2O)C(=O)C4=C(C3=O)C=CC=C4OC)O)O[C@H]5C[C@@H]([C@@H]([C@@H](O5)C)O)NC(=O)C(F)(F)F)O
CC[C@]1(C[C@@H](C2=C(C3=C(C=C2[C@H]1C(=O)OC)C(=O)C4=C(C3=O)C(=CC=C4)O)O)O[C@H]5C[C@@H]([C@@H]([C@@H](O5)C)O[C@H]6C[C@@H]([C@@H]([C@@H](O6)C)O[C@H]7CCC(=O)[C@@H](O7)C)O)N(C)C)O
C1=CC(=C2C(=C1NCCN)C(=O)C3=C(C2=O)C=NC=C3)NCCN
CC(=O)[C@]1(C[C@@H](C2=C(C1)C(=C3C(=C2O)C(=O)C4=CC=CC=C4C3=O)O)O[C@H]5C[C@@H]([C@@H](CO5)O)O)N
C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(/C(=N/NC(=O)C6=CC=CC=C6)/C)O)N)O
C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)O)O)(C(=O)C)O)N)O
C[C@@H]1[C@H]([C@@H](C[C@@H](O1)O[C@@H]2C[C@@H](O[C@@H]([C@H]2O)C)OC3=CC4=CC5=C(C(=O)[C@H]([C@@H](C5)[C@@H](C(=O)[C@H]([C@@H](C)O)O)OC)O[C@H]6C[C@H]([C@@H]([C@H](O6)C)O)O[C@H]7C[C@H]([C@H]([C@H](O7)C)O)O[C@H]8C[C@]([C@@H]([C@H](O8)C)O)(C)O)C(=C4C(=C3C)O)O)O)O
C[C@@]1(C[C@H](C2=C(C3=C(C=C2C1)C(=O)C4=C5C(=CC(=C4C3=O)O)[C@@]6([C@@H]([C@H]([C@@H]([C@H](O5)O6)O)N(C)C)O)C)O)OC)O
CC1=C2C=CN=CC2=C(C3=C1NC4=CC=CC=C43)C
CC1=C(N=C(N=C1N)[C@H](CC(=O)N)NC[C@@H](C(=O)N)N)C(=O)N[C@@H]([C@H](C2=CN=CN2)OC3C(C(C(C(O3)CO)O)O)OC4C(C(C(C(O4)CO)O)OC(=O)N)O)C(=O)N[C@H](C)[C@H]([C@H](C)C(=O)N[C@@H]([C@@H](C)O)C(=O)NCCC5=NC(=CS5)C6=NC(=CS6)C(=O)NCCC[S+](C)C)O
C[C@@H]1[C@@H](C(=O)N[C@@H](C(=O)N2CCC[C@H]2C(=O)N(CC(=O)N([C@H](C(=O)O1)C(C)C)C)C)C(C)C)NC(=O)C3=C4C(=C(C=C3)C)OC5=C(C(=O)C(=C(C5=N4)C(=O)N[C@H]6[C@H](OC(=O)[C@@H](N(C(=O)CN(C(=O)[C@@H]7CCCN7C(=O)[C@H](NC6=O)C(C)C)C)C)C(C)C)C)N)C
CC1=C(C(=C(N=C1C(=O)O)C2=NC3=C(C=C2)C(=O)C(=C(C3=O)N)OC)N)C4=C(C(=C(C=C4)OC)OC)O
CN(C)C1=NC=NC2=C1N=CN2[C@H]3[C@@H]([C@@H]([C@H](O3)CO)NC(=O)[C@H](CC4=CC=C(C=C4)OC)N)O
C1=NC2=C(N=C(N=C2N1[C@H]3[C@H]([C@@H]([C@H](O3)CO)O)O)F)N
CN(CC1=CN=C2C(=N1)C(=NC(=N2)N)N)C3=CC=C(C=C3)C(=O)N[C@@H](CCC(=O)O)C(=O)O
C1=C(C(=O)NC(=O)N1)F
C1=CN(C(=O)N=C1N)[C@H]2C([C@@H]([C@H](O2)CO)O)(F)F
C1[C@@H]([C@H](O[C@H]1N2C=NC(=NC2=O)N)CO)O
C1=NC2=C(N1)C(=S)N=CN2
C1=CN(C(=O)N=C1N)[C@H]2[C@H]([C@@H]([C@H](O2)CO)O)O
C1[C@@H]([C@H](O[C@H]1N2C=C(C(=O)NC2=O)F)CO)O
C1=CC(=CC=C1CCC2=CNC3=C2C(=O)NC(=N3)N)C(=O)N[C@@H](CCC(=O)O)C(=O)O
C(CCl)NC(=O)N(CCCl)N=O
CCC1=C2CN3C(=CC4=C(C3=O)COC(=O)[C@@]4(CC)O)C2=NC5=C1C=C(C=C5)OC(=O)N6CCC(CC6)N7CCCCC7
CC[C@@]1(C2=C(COC1=O)C(=O)N3CC4=CC5=C(C=CC(=C5CN(C)C)O)N=C4C3=C2)O
C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(C(=O)CO)O)N)O
C[C@@H]1OC[C@@H]2[C@@H](O1)[C@@H]([C@H]([C@@H](O2)O[C@H]3[C@H]4COC(=O)[C@@H]4[C@@H](C5=CC6=C(C=C35)OCO6)C7=CC(=C(C(=C7)OC)O)OC)O)O
CC1=C(C=CC2=C1OC(=O)C(=C2O)NC(=O)C3=CC(=C(C=C3)O)CC=C(C)C)O[C@H]4[C@@H]([C@@H]([C@H](C(O4)(C)C)OC)OC(=O)N)O
C1=CC=C2C(=C1)C=CC(=O)N2
COC1=CC(=CC(=C1O)OC)[C@H]2[C@@H]3[C@H](COC3=O)[C@@H](C4=CC5=C(C=C24)OCO5)O[C@H]6[C@@H]([C@H]([C@H]7[C@H](O6)CO[C@H](O7)C8=CC=CS8)O)O
C1=CC(=C2C(=C1NCCNCCO)C(=O)C3=C(C=CC(=C3C2=O)O)O)NCCNCCO
COC1=C2C(=CC(=C1N3C[C@@H]4CCCN[C@@H]4C3)F)C(=O)C(=CN2C5CC5)C(=O)O
CC1CN(CCN1)C2=C(C(=C3C(=C2)N(C=C(C3=O)C(=O)O)C4CC4)C)F
C[C@@H](CN1CC(=O)NC(=O)C1)N2CC(=O)NC(=O)C2
C[C@H]1[C@@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(C(=O)CO)O)N)O
CCN1C=C(C(=O)C2=CC(=C(N=C21)N3CCNCC3)F)C(=O)O
CCN1C=C(C(=O)C2=CC(=C(C=C21)N3CCN(CC3)C)F)C(=O)O
C1CC1N2C=C(C(=O)C3=CC(=C(C=C32)N4CCNCC4)F)C(=O)O
C1[C@@H]2[C@@H](C2N)CN1C3=C(C=C4C(=O)C(=CN(C4=N3)C5=C(C=C(C=C5)F)F)C(=O)O)F
C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(C(=O)C)O)N)O
CCN1C=C(C(=O)C2=C1N=C(C=C2)C)C(=O)O
CCN1C2=CC3=C(C=C2C(=O)C(=N1)C(=O)O)OCO3
CCN1C=C(C(=O)C2=CC(=C(C(=C21)F)N3CCNC(C3)C)F)C(=O)O
C[C@H]1[C@H]([C@H](C[C@@H](O1)O[C@H]2C[C@@](CC3=C2C(=C4C(=C3O)C(=O)C5=C(C4=O)C(=CC=C5)OC)O)(C(=O)CO)O)N)O
CC1CN(CCN1)C2=C(C=C3C(=C2OC)N(C=C(C3=O)C(=O)O)C4CC4)F
CCN1C=C(C(=O)C2=CC(=C(C=C21)N3CCNCC3)F)C(=O)O
C[C@H]1COC2=C3N1C=C(C(=O)C3=CC(=C2N4CCN(CC4)C)F)C(=O)O

in your terminal. copy paste it on a sheets, now you have a 2 column sheets with ligands and smiles.
