#%% good example of changing txt file to csv:
#https://stackoverflow.com/a/55606626/4510954
import csv
with open ('/path.txt') as from_fp, open('/new_path.tsv', 'w') as to_fp:
    csv_reader = csv.DictReader(from_fp, delimiter='\t')
    csv_writer = csv.writer(to_fp, delimiter='\t')
    csv_writer.writerow(['AgentName', 'MRP'])
    for row in csv_reader:
        csv_writer.writerow([row.get('Agent Name'), row.get('MRP')])
