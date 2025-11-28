import os


data_path = os.path.join('data')

# ---------- Raw Folder
raw_path = os.path.join(data_path, 'raw')

raw_inmet_folder = os.path.join(raw_path, 'inmet')

raw_inpe_folder = os.path.join(raw_path, 'inpe')
raw_inpe_all_folder = os.path.join(raw_inpe_folder, 'todos-sats')

# ---------- Raw Fixed Folder
raw_fixed_path = os.path.join(data_path, 'raw_fixed')

raw_fixed_inmet_folder = os.path.join(raw_fixed_path, 'inmet')

raw_fixed_inpe_folder = os.path.join(raw_fixed_path, 'inpe')
raw_fixed_inpe_all_folder = os.path.join(raw_fixed_inpe_folder, 'todos-sats')

# ---------- Concat Folder
concat_path = os.path.join(data_path, 'concat')
os.makedirs(concat_path, exist_ok=True)

inmet_concat_file = os.path.join(concat_path, 'inmet_concat.csv')
inmet_stations_file = os.path.join(concat_path, 'inmet_stations.csv')
inpe_all_concat_file = os.path.join(concat_path, 'inpe_all_concat.csv')

# ---------- Linked Folder
linked_path = os.path.join(data_path, 'linked')
os.makedirs(linked_path, exist_ok=True)

inpe_stations_linked_file = os.path.join(linked_path, 'inpe_stations_linked.csv')

inmet_inpe_linked_file = os.path.join(linked_path, 'inmet_inpe_linked.csv')