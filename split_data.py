#!/usr/bin/env python3

import os
from collections import defaultdict
from collections import Counter
import random

gem_dict = {}

with open('data/covid-selected-data.csv') as gem_f:
    gem_fl = gem_f.readline()
    genes = gem_fl.rstrip().split(',')[1:]
    for line in gem_f:
        line = line.rstrip().split(',')
        cell_id = line[0]
        gem_dict[cell_id] = line[1:]

cell_info = {}
patient_cells = defaultdict(list)
patient_labels = {}
label_counts = defaultdict(int)

with open('data/covid-selected-data-labels.csv') as labels_f:
    labels_fl = labels_f.readline()
    for line in labels_f:
        cell_id,label = line.rstrip().split(',')
        patient_id = cell_id.split('-')[0].split('_')[1]
        cell_info[cell_id] = {
            'patient_id' : patient_id,
            'label' : label,
        }
        label_counts[label] += 1
        patient_labels[patient_id] = label
        patient_cells[patient_id].append(cell_id)

label_pct = { label : label_counts[label]/sum(label_counts.values()) for label in label_counts }

if not os.path.exists('./outputs'):
    os.mkdir('./outputs')

finding_test = True
while finding_test:
    patient_ids = list(patient_labels)
    random.shuffle(patient_ids)
    test_patients = patient_ids[10:]
    test_label_counts = dict(Counter([patient_labels[p] for p in test_patients]))
    remaining_patients = patient_ids[:10]

    test_sum = sum(len(patient_cells[p]) for p in test_patients)
    test_pct = test_sum/len(cell_info)

    if test_label_counts == {'Normal' : 1, 'Mild' : 1, 'Severe' : 1} and test_pct < 0.25 and test_pct > 0.15:
        cell_label_count = defaultdict(int)
        for p in test_patients:
            cell_label_count[patient_labels[p]] += len(patient_cells[p])
        cell_label_pct = { label : cell_label_count[label]/sum(cell_label_count.values()) for label in cell_label_count }
        if cell_label_pct['Severe'] > (label_pct['Severe'] * 0.50) and cell_label_pct['Severe'] < (label_pct['Severe'] * 1.50):
            print('Found test patients')
            print(f"Total test cells: {test_sum}")
            print(f"Test percentage of all {len(cell_info)} cells: {test_pct:.2f}")
            print(f"Test label counts (# patients): {test_label_counts}")
            id_label = { p : patient_labels[p] for p in test_patients }
            print(f"Test patient IDs and labels: {id_label}")
            print(f"Cell label count (test): {dict(cell_label_count)}")
            cell_label_pct = { label : round(cell_label_pct[label],2) for label in cell_label_pct }
            print(f"Cell label percentages (test): {cell_label_pct}\n")

            print('Writing test set to files')
            cell_ids = []
            for p in test_patients:
                cell_ids += patient_cells[p]
            
            with open('./outputs/test-data-labels.csv', 'w') as test_labels_f, open('./outputs/test-data.csv', 'w') as test_data_f:
                test_labels_f.write(labels_fl)
                test_data_f.write(gem_fl)
                for c in cell_ids:
                    test_labels_f.write(f"{c},{cell_info[c]['label']}\n")
                    test_data_f.write(f"{c},{','.join(gem_dict[c])}\n")
            print('Finished writing test set to files\n')

            finding_test = False

print(f"\nRemaining patients (for training): {remaining_patients}\n")

for i,p in enumerate(remaining_patients):
    labels_filename = f"./outputs/train-data-labels_{i+1}.csv"
    data_filename = f"./outputs/train-data_{i+1}.csv"
    print(f"Writing files for patient {p} to {labels_filename} and {data_filename}")

    with open(labels_filename, 'w') as train_labels_f, open(data_filename, 'w') as train_data_f:
        train_labels_f.write(labels_fl)
        train_data_f.write(gem_fl)
        for c in patient_cells[p]:
            train_labels_f.write(f"{c},{cell_info[c]['label']}\n")
            train_data_f.write(f"{c},{','.join(gem_dict[c])}\n")

    print(f"Done writing files for patient {p}\n")
