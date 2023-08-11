# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"10191","system":"gprdproduct"},{"code":"10429","system":"gprdproduct"},{"code":"11711","system":"gprdproduct"},{"code":"11793","system":"gprdproduct"},{"code":"1288","system":"gprdproduct"},{"code":"15117","system":"gprdproduct"},{"code":"15176","system":"gprdproduct"},{"code":"1684","system":"gprdproduct"},{"code":"19055","system":"gprdproduct"},{"code":"19182","system":"gprdproduct"},{"code":"21133","system":"gprdproduct"},{"code":"21873","system":"gprdproduct"},{"code":"24191","system":"gprdproduct"},{"code":"2432","system":"gprdproduct"},{"code":"26741","system":"gprdproduct"},{"code":"29762","system":"gprdproduct"},{"code":"30541","system":"gprdproduct"},{"code":"30636","system":"gprdproduct"},{"code":"31470","system":"gprdproduct"},{"code":"31708","system":"gprdproduct"},{"code":"32094","system":"gprdproduct"},{"code":"32135","system":"gprdproduct"},{"code":"32836","system":"gprdproduct"},{"code":"33092","system":"gprdproduct"},{"code":"33650","system":"gprdproduct"},{"code":"33850","system":"gprdproduct"},{"code":"34034","system":"gprdproduct"},{"code":"34094","system":"gprdproduct"},{"code":"34265","system":"gprdproduct"},{"code":"34365","system":"gprdproduct"},{"code":"34407","system":"gprdproduct"},{"code":"34430","system":"gprdproduct"},{"code":"34443","system":"gprdproduct"},{"code":"34449","system":"gprdproduct"},{"code":"34584","system":"gprdproduct"},{"code":"34695","system":"gprdproduct"},{"code":"34825","system":"gprdproduct"},{"code":"34882","system":"gprdproduct"},{"code":"34890","system":"gprdproduct"},{"code":"34925","system":"gprdproduct"},{"code":"36261","system":"gprdproduct"},{"code":"38433","system":"gprdproduct"},{"code":"39819","system":"gprdproduct"},{"code":"42152","system":"gprdproduct"},{"code":"4542","system":"gprdproduct"},{"code":"46614","system":"gprdproduct"},{"code":"4725","system":"gprdproduct"},{"code":"5","system":"gprdproduct"},{"code":"581","system":"gprdproduct"},{"code":"739","system":"gprdproduct"},{"code":"8071","system":"gprdproduct"},{"code":"8642","system":"gprdproduct"},{"code":"9273","system":"gprdproduct"},{"code":"9783","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('beta-blockers-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["beta-blockers-250mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["beta-blockers-250mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["beta-blockers-250mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
