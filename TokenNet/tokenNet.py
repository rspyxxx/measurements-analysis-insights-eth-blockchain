#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```token_net_address_hash.csv: (address, hashID)                                         #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```token_net.csv: (hashed_from_address, hashed_to_address)                               #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.token_transfers`                 #
#*****************************************************************************************#

import csv
import sys
csv.field_size_limit(sys.maxsize)
g = 'tokens_trf_final.csv' #merged the exported csv files into one file 

nodes = {}
n = 0
count= 0

with open(g, "r") as gFile:
    with open("token_net_address_hash.csv", "w", newline ='') as hfile:
        with open("token_net.csv", "w",  newline ='') as tfile:
            reader = csv.reader(gFile)
            hasher = csv.writer(hfile)
            writer = csv.writer(tfile)

            for rows in reader:
                if rows[1] != 'from_address':
                    if nodes.get(rows[1]) is None:
                        nodes.update({rows[1] : n})
                        n+=1
                    if nodes.get(rows[2]) is None:
                        nodes.update({rows[2]: n})
                        n+=1
                        
                    writer.writerow([nodes[rows[1]], nodes[rows[2]]])
                    count +=1

            for k,v in nodes.items():
                hasher.writerow([k,v])
            print(n)
            print(count)
            print(len(list(nodes.keys())))
            
                
