

# main.py
import streamlit as st
from app.dicom_loader import load_dicom_series
from app.viewer import show_slice
from app.classifier import predict

st.title("Brain MRI DICOM Viewer")

folder = st.text_input("Enter DICOM folder path", "data/sample_dicom")

if folder:
    dicoms = load_dicom_series(folder)
    slice_num = st.slider("Slice Number", 0, len(dicoms)-1, 0)
    show_slice(dicoms, slice_num)

    if st.button("Predict Tumor"):
        img = dicoms[slice_num].pixel_array
        result = predict(img)
        st.success(f"Prediction: {result}")