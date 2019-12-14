# Measurements, Analyses and Insights on the Entire Ethereum Blockchain
## Data (Four Interaction Network)
This repository consist of the four interaction networks in their respective folders. Files here are converted and extracted form the original data which can be found from Google Cloud Platform's BigQuery -'ethereum_blockchain'. Original data set extracted will not be found here. Script for hashing the files and extracting the four network from the original data set can also be found in the respective folders.

(1) TraceNet
(2) ContractNet
(3) TransactionNet
(4) TokenNet

As the files are relatively huge, they are split into multiple text files, separated by commas. After extraction, the files are split using linux command line:  i.e. split -d -l 1500000 trace_net.csv trace_net_  <br> 

Format for hash files: address, hash <br>
Format for net files: from_address_hash, to_address_hash

Credits:
https://www.kaggle.com/bigquery/ethereum-blockchain (original dataset)

### Data Extraction from BigQuery
1. Login to Google Cloud Platform. 
2. Create a bucket to store your files.
2. Go to BigQuery and find the data set 'ethereum_blockchain'
3. Select the table you want and 'Export to GCS'.
4. Then select the GCS location (the bucket created in step 2). 
5. If csv is preferred: <bucket>/<folder>/file*.csv (e.g. tmpbucket/blocks/blocks*.csv). <bR>
   The * will help to number the files as exporting the tables will split the data into multiple files. <br>
   Replace .csv with .txt or .json as per your preference.
6. Pip install gsutil, open command line and download the files. (Tried with Python 2.7 in Ubuntu)<br>
   For downloaded entire folder: gsutil -m cp -r gs://bucketname/folder-name local-location <br>
   For downloaded multiple files: gsutil -m cp -r gs://bucketname/folder-name/filename* local-location<br>

If gstuil does not work, manual download is possible from the bucket (not recommended).<br>
After downloaded the necessary data you might want to delete the bucket to prevent charges.<br>
Alternative method: https://github.com/blockchain-etl/ethereum-etl <br>


   
