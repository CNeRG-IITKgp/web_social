import csv
import sys

with open('CNeRG Web and Social Details.csv') as fp:
        rdr = csv.reader(fp)
        head = next(rdr)
        data = list(rdr)

# redirect to file
stdout = sys.stdout
with open('index.md', 'w') as sys.stdout:
        
        print('# Web and Social Media Research, [CNeRG](https://cnerg-iitkgp.github.io/)')
        print('[Department of Computer Science and Engineering](http://cse.iitkgp.ac.in/) <br>')
        print('[Indian Institute of Technology Kharagpur](http://www.iitkgp.ac.in/) <br>\n\n')
        
        print('# Students ')
        for row in data:
                print('- ### ', row[2],'\n')
                # print('```s h\n')
                print('\t- Supervisor:', row[4],'\n')
                print('\t- Projects:\n')
                for proj in row[5].strip().split('\n'):
                        if proj.strip(): print('\t\t- ',proj,'\n\n')
                print('	- Publications:\n')
                for pub in row[6].strip().split('\n'):
                        if pub.strip(): print('\t\t- ',pub,'\n\n')

sys.stdout = stdout