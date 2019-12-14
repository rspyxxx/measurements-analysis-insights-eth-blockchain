#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```trace_net_address_hash.csv: (address, hashID)                                         #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```trace_net.csv: (hashed_from_address, hashed_to_address)                               #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.traces`                          #   
#*****************************************************************************************#

import csv
import sys
import datetime

print("start: ", datetime.datetime.now())
csv.field_size_limit(sys.maxsize)

filenum1 = '00000000000'	#remove 1 zero
filenum2 = '0000000000'		#remove 2 zeroes
filenum3 = '000000000'		#remove 3 zeroes
filenum4 = '00000000'		#remove 4 zeroes

a = 0
nodes = {}
n = 0
count= 0

while a < 5000 :
    if a < 10:
        f = 'traces'+filenum1+str(a)+'.csv'
    elif a <100:
        f = 'traces'+filenum2+str(a)+'.csv'
    elif a < 1000:
        f = 'traces'+filenum3+str(a)+'.csv'
    else:
        f = 'traces'+filenum4+str(a)+'.csv'
        
    #['transaction_hash', 'transaction_index', 'from_address', 'to_address', 'value', 'input', 'output', 'trace_type', 'call_type', 'reward_type', 'gas', 'gas_used', 'subtraces', 'trace_address', 'error', 'status', 'block_timestamp', 'block_number', 'block_hash']

    with open(f, "r") as gFile:
        reader = csv.reader(gFile)
        with open("trace_net.csv", "a+", newline ='') as tfile:
            writer = csv.writer(tfile)
            for rows in reader:
                if rows[2] != 'from_address':
                    if int(rows[15]) == 1:
                        if ((rows[2] != '') and (rows[3] != '')):
                            #<e, from, to, value, gas, gas used, txnhash, trace addr, trace type, block num>
                            if nodes.get(rows[2]) is None:
                                nodes.update({rows[2] : n})
                                n+=1
                            if nodes.get(rows[3]) is None:
                                nodes.update({rows[3]: n})
                                n+=1

                            writer.writerow([nodes[rows[2]], nodes[rows[3]]])
                            count +=1                
    print(f, " done")
    a+=1

with open("trace_net_address_hash.csv", "w", newline ='') as hfile:
    hasher = csv.writer(hfile)
    for k,v in nodes.items():
        hasher.writerow([k,v])

print(n)
print(count)
print(len(list(nodes.keys())))
            
       
                        
