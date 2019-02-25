import json
import csv
import sys

if len(sys.argv) != 3 or '.json' not in sys.argv[1]:
    print(sys.argv)
    print("argument: predictions.json, output_file")
    exit(1)

print("Load {}....".format(sys.argv[1]))
with open(sys.argv[1], 'r') as f:
    json_data = json.load(f)
with open(sys.argv[2], 'w') as csv_fh:
    csv_writer = csv.writer(csv_fh, delimiter=',')
    csv_writer.writerow(['Id', 'Predicted'])
    for uuid in sorted(json_data):
        csv_writer.writerow([uuid, json_data[uuid]])
