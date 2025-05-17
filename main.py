import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the IoT data from the CSV file
def load_data():
    return pd.read_csv('iot_parcel_data.csv')

# Display vehicle data
def display_vehicle_data(vehicle_number):
    data_df = load_data()
    filtered_data = data_df[data_df['vehicle_number'] == vehicle_number]
    st.write(filtered_data)

# Plot temperature vs. time for a specific vehicle
def plot_vehicle_temperature(vehicle_number):
    data_df = load_data()
    filtered_data = data_df[data_df['vehicle_number'] == vehicle_number]
    plt.figure(figsize=(10, 6))
    plt.plot(pd.to_datetime(filtered_data['timestamp']), filtered_data['temperature'], label='Temperature (°C)', color='blue')
    plt.xlabel('Timestamp')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Real-time Temperature for Vehicle {vehicle_number}')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    st.pyplot()

# Real-time data tracking in Streamlit
st.title("IoT Vehicle Data Tracker")

vehicle_number = st.text_input("Enter Vehicle Number (e.g., KA01AB1234):")
if vehicle_number:
    display_vehicle_data(vehicle_number)
    plot_vehicle_temperature(vehicle_number)

    # Additional Filters
    st.sidebar.header("Filter by")
    temp_range = st.sidebar.slider("Temperature Range", min_value=15, max_value=35, value=(15, 35))
    filtered_df = load_data()
    filtered_df = filtered_df[(filtered_df['temperature'] >= temp_range[0]) & (filtered_df['temperature'] <= temp_range[1])]
    st.write("Filtered Data Based on Temperature Range:")
    st.write(filtered_df)

    # Export Button
    if st.button("Export Data to CSV"):
        filtered_df.to_csv("filtered_vehicle_data.csv", index=False)
        st.success("Data exported successfully!")
