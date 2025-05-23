# -*- coding: utf-8 -*-
"""app/utils.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Oz546-c4YJeJbKfkQSltovva2L0NUn92
"""

# app/utils.py
def print_metadata(ds):
    print("Patient ID:", ds.PatientID)
    print("Modality:", ds.Modality)
    print("Study Date:", ds.StudyDate)
    print("Dimensions:", ds.Rows, "x", ds.Columns)