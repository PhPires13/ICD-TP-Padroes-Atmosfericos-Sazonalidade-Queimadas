import os

# ---------- Data Directory
data_dir = os.path.join('data')

# ----- Raw Directory
raw_dir = os.path.join(data_dir, 'raw')

raw_inmet_dir = os.path.join(raw_dir, 'inmet')

raw_inpe_dir = os.path.join(raw_dir, 'inpe')
raw_inpe_all_dir = os.path.join(raw_inpe_dir, 'todos-sats')

# ----- Raw Fixed Directory
raw_fixed_dir = os.path.join(data_dir, 'raw_fixed')
os.makedirs(raw_fixed_dir, exist_ok=True)

raw_fixed_inmet_dir = os.path.join(raw_fixed_dir, 'inmet')
os.makedirs(raw_fixed_inmet_dir, exist_ok=True)

raw_fixed_inpe_dir = os.path.join(raw_fixed_dir, 'inpe')
os.makedirs(raw_fixed_inpe_dir, exist_ok=True)
raw_fixed_inpe_all_dir = os.path.join(raw_fixed_inpe_dir, 'todos-sats')
os.makedirs(raw_fixed_inpe_all_dir, exist_ok=True)

# ----- Concat Directory
concat_dir = os.path.join(data_dir, 'concat')
os.makedirs(concat_dir, exist_ok=True)

inmet_concat_file = os.path.join(concat_dir, 'inmet_concat.csv')
inmet_stations_file = os.path.join(concat_dir, 'inmet_stations.csv')
inpe_all_concat_file = os.path.join(concat_dir, 'inpe_all_concat.csv')

# ----- Linked Directory
linked_dir = os.path.join(data_dir, 'linked')
os.makedirs(linked_dir, exist_ok=True)

inpe_stations_linked_file = os.path.join(linked_dir, 'inpe_stations_linked.csv')

inmet_inpe_linked_file = os.path.join(linked_dir, 'inmet_inpe_linked.csv')

# ---------- Model Directory
model_dir = os.path.join('models')
os.makedirs(model_dir, exist_ok=True)

# ----- Training Directory
training_dir = os.path.join(model_dir, 'training')
os.makedirs(training_dir, exist_ok=True)

classification_info_dir = os.path.join(training_dir, 'catboost_info_fire_occurrence_classification')
regression_info_dir = os.path.join(training_dir, 'catboost_info_fire_intensity_regression')

# ----- CBM Directory
cbm_dir = os.path.join(model_dir, 'cbm')
os.makedirs(cbm_dir, exist_ok=True)

classification_cbm_file = os.path.join(cbm_dir, 'fire_occurrence_classification_model.cbm')
regression_cbm_file = os.path.join(cbm_dir, 'fire_intensity_regression_model.cbm')