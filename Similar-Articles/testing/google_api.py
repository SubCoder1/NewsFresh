from googlesearch import search

query = "Mueller team wants to withhold 3.2 million ‘sensitive’ docs from indicted Russian company"

for j in search(query, tld = "com", num = 10, start = 1, stop = 10):
    print (j)
