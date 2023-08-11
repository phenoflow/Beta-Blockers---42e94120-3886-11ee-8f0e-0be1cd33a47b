# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"297","system":"gprdproduct"},{"code":"31214","system":"gprdproduct"},{"code":"34804","system":"gprdproduct"},{"code":"34867","system":"gprdproduct"},{"code":"36576","system":"gprdproduct"},{"code":"39233","system":"gprdproduct"},{"code":"43525","system":"gprdproduct"},{"code":"45494","system":"gprdproduct"},{"code":"940","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('beta-blockers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["beta-blockers-propranolol---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["beta-blockers-propranolol---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["beta-blockers-propranolol---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
