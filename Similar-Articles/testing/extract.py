from newspaper import Article
import re

urls = ['https://www.youtube.com/watch?v=IZo5gHfn-Xs', 'https://www.youtube.com/watch?v=xANPlkt3VLc', 'https://www.vox.com/policy-and-politics/2019/1/17/18167430/nra-2018-midterms-trump-spending-trouble']

domains = []

for i in urls:
    s = (r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}', i)
    domains.append(s)

print(domains)
