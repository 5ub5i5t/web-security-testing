"""Analyze Accepted Vulns"""

import os
import sys
import json
from datetime import datetime

if len(sys.argv) == 1:
    print("Please provide a path to a folder.")
    sys.exit()
elif len(sys.argv) == 2:
    folder = sys.argv[1]
    status = 'all'
elif len(sys.argv) == 3:
    folder = sys.argv[1]
    status = sys.argv[2]
    if status!='all' and status!='pending' and status!='fixed':
        print("Please input a valid status (i.e. all, pending, fixed).")
        sys.exit()

if not os.path.exists(folder):
    print("Invalid path.")
    sys.exit()

vulns = {}

for filename in os.listdir(folder):
    if filename=='all.json' or filename=='all_by_target.json' or filename=='fixed.json' or filename=='fixed_by_target.json' or filename=='pending.json' or filename=='pending_by_target.json':
        continue
    f = os.path.join(folder, filename)
    if os.path.isfile(f) and f.endswith('.json'):
        target_id = filename.split("_")[1].replace(".json","")
        target = filename.split("_")[0]
        data = json.load(open(f))
        vulns[target] = []
        for item in data['value']:
            item['id'] = target_id
            item['target'] = target
            for location in item['exploitable_locations']:
                created_timestamp = datetime.utcfromtimestamp(location['created_at']).strftime('%Y-%m-%d %H:%M:%S')
                location['created_timestamp'] = created_timestamp
                location['id'] = target_id
                location['target'] = target
                location['categories'] = item['categories']
                location['category-main'] = item['categories'][0]
                location['category-sub'] = item['categories'][1]
                vulns[target].append(location)

output = {}

if not folder.endswith('/'):
    folder = folder + '/'

if status=='all':
    output = vulns
    with open(folder + 'all_by_target.json', 'w') as f:
        json.dump(output, f)
    output = []
    for target in vulns:
        for vuln in vulns[target]:
            output.append(vuln)
    with open(folder + 'all.json', 'w') as f:
        json.dump(output, f)
else:
    for target in vulns:
        output[target] = []
        for vuln in vulns[target]:
            if vuln['status'] == status:
                output[target].append(vuln)
    with open(folder + status + '_by_target.json', 'w') as f:
        json.dump(output, f)
    output = []
    for target in vulns:
        for vuln in vulns[target]:
            if vuln['status'] == status:
                output.append(vuln)
    with open(folder + status + '.json', 'w') as f:
        json.dump(output, f) 