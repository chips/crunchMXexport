#Import needed packages
import csv
import dns.resolver

#Parameters for search.
#What do you want to match anywhere in the mx lookup
servermatch = "google"

#What do you want to call the service in the printout
servername = "Google"

#The name of the text output
txtFileOutName = "MyOutput.txt"

#Name of csv export
csvFileOutName = "MyOutput.csv"

#Name of your input file, the one from crunchbase
inputFile = "companies-large.csv"

file1 = open(txtFileOutName,"w+") 
file2 = open(csvFileOutName, "w+")

count = 0

with open(inputFile, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domain = (row[-1].split("@")[-1])
        size = (row[-2])
        company = row[0]
        industries = row[2]
        mail = row[-1]
        location = row[3]
        try:
            ismatch = 0
            for rdata1 in dns.resolver.query(domain, 'MX') :
                if ismatch == 0:
                    if servermatch in str(rdata1).lower():
                        ismatch = 1
                        count += 1
                        file2.write(row[0] + ";" +row[3] + ";" + domain + "\n")
                        print("%s located in %s has %s employees in the %s industries and uses %s servers. They can be reached at %s " % (company,location, size, industries, servername, mail ))
                        print()
                        file1.write("%s located in %s has %s employees in the %s industries and uses % servers. They can be reached at %s \n\n" % (company,location, size, industries,servername, mail ))
                        
        except:
            z=2
file1.close()
file2.close()
print(count)