

import pydicom
import os

def load_dicom_series(folder_path):
    dicom_files = [pydicom.dcmread(os.path.join(folder_path, f)) for f in os.listdir(folder_path) if f.endswith(".dcm")]
    dicom_files.sort(key=lambda x: int(x.InstanceNumber))  # Sort by slice order
    return dicom_files