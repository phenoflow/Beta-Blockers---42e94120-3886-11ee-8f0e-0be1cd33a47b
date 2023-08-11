# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"1295","system":"gprdproduct"},{"code":"27700","system":"gprdproduct"},{"code":"3087","system":"gprdproduct"},{"code":"31776","system":"gprdproduct"},{"code":"34371","system":"gprdproduct"},{"code":"34600","system":"gprdproduct"},{"code":"34868","system":"gprdproduct"},{"code":"38498","system":"gprdproduct"},{"code":"40240","system":"gprdproduct"},{"code":"41555","system":"gprdproduct"},{"code":"43549","system":"gprdproduct"},{"code":"45297","system":"gprdproduct"},{"code":"707","system":"gprdproduct"},{"code":"786","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('beta-blockers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["beta-blockers-400mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["beta-blockers-400mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["beta-blockers-400mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
