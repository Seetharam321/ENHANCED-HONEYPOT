import streamlit as st
import pandas as pd
import hashlib
import matplotlib.pyplot as plt
import seaborn as sns
import time
import random

# Sample blockchain data (replace this with your actual blockchain data)
blockchain_data = pd.DataFrame({
    'index': [1, 2, 3, 4, 5],
    'timestamp': ['2024-01-01 08:00:00', '2024-01-02 12:00:00', '2024-01-03 16:00:00', '2024-01-04 10:00:00',
                  '2024-01-05 14:00:00'],
    'event_type': ['Malicious Activity', 'Suspicious Activity', 'Malicious Activity', 'Suspicious Activity',
                   'Malicious Activity'],
    'source_ip': ['192.168.1.10', '192.168.1.15', '192.168.1.20', '192.168.1.25', '192.168.1.30'],
    'destination_ip': ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5'],
    'hash': ['0000abcdef...', '0000abc123...', '0000def456...', '0000ghi789...', '0000jkl012...']
})


# Function to calculate hash for data
def calculate_hash(data):
    data_str = ''.join(str(value) for value in data)
    return hashlib.sha256(data_str.encode()).hexdigest()


# Function to check if event is malicious based on blockchain records
def check_malicious_event(event_type, source_ip, destination_ip):
    for index, row in blockchain_data.iterrows():
        block_data = [row['index'], row['timestamp'], row['event_type'], row['source_ip'], row['destination_ip']]
        if event_type == row['event_type'] and source_ip == row['source_ip'] and destination_ip == row[
            'destination_ip']:
            if calculate_hash(block_data) == row['hash']:
                return True
    return False


# Function to plot event type distribution
def plot_event_type_distribution():
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=blockchain_data, x='event_type', palette='Set2', ax=ax)
    ax.set_title('Event Type Distribution')
    ax.set_xlabel('Event Type')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    return fig


# Function to plot top 5 source IPs
def plot_top_source_ips():
    top_source_ips = blockchain_data['source_ip'].value_counts().head(5)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=top_source_ips.index, y=top_source_ips.values, palette='Set3', ax=ax)
    ax.set_title('Top 5 Source IPs')
    ax.set_xlabel('Source IP')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    return fig


# Function to plot top 5 destination IPs
def plot_top_destination_ips():
    top_destination_ips = blockchain_data['destination_ip'].value_counts().head(5)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=top_destination_ips.index, y=top_destination_ips.values, palette='Set3', ax=ax)
    ax.set_title('Top 5 Destination IPs')
    ax.set_xlabel('Destination IP')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    return fig


# Streamlit UI
st.set_page_config(layout="wide")
st.title('Enhanced Honeypot Security with Blockchain')
st.header('Intrusion Detection and Prevention System')

# Sidebar for filters and visualization
st.sidebar.subheader('Filters')
event_type_filter = st.sidebar.selectbox('Event Type', ['All'] + list(blockchain_data['event_type'].unique()))

# Apply filters
filtered_data = blockchain_data.copy()
if event_type_filter != 'All':
    filtered_data = filtered_data[filtered_data['event_type'] == event_type_filter]

# Display filtered data
st.subheader('Blockchain Records')
st.write(filtered_data)

# Display event type distribution plot
event_type_distribution_fig = plot_event_type_distribution()
st.pyplot(event_type_distribution_fig)

# Display top 5 source IPs
top_source_ips_fig = plot_top_source_ips()
st.pyplot(top_source_ips_fig)

# Display top 5 destination IPs
top_destination_ips_fig = plot_top_destination_ips()
st.pyplot(top_destination_ips_fig)

# Input form
st.subheader('Check Event')
event_type = st.selectbox('Event Type', ['Malicious Activity', 'Suspicious Activity'])
source_ip = st.text_input('Source IP', '')
destination_ip = st.text_input('Destination IP', '')

# Button to check if event is malicious
if st.button('Check Event'):
    if check_malicious_event(event_type, source_ip, destination_ip):
        st.error('Alert: Malicious Event Detected!')
    else:
        st.success('No Malicious Activity Detected')

# Real-time data updates
if st.sidebar.checkbox('Enable Real-time Updates'):
    st.sidebar.write('**Real-time Updates Enabled**')

    while True:
        # Generate new log data
        new_log = {
            'index': blockchain_data['index'].max() + 1,
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'event_type': random.choice(['Malicious Activity', 'Suspicious Activity']),
            'source_ip': f'192.168.1.{random.randint(1, 255)}',
            'destination_ip': f'10.0.0.{random.randint(1, 255)}',
            'hash': 'dummyhash'  # Replace this with actual hash calculation
        }

        # Concatenate existing DataFrame with new log data
        blockchain_data = pd.concat([blockchain_data, pd.DataFrame([new_log])], ignore_index=True)

        # Rerun the Streamlit app to update the UI
        st.experimental_rerun()

        # Pause for a while before generating the next log
        time.sleep(5)  # Adjust the interval as needed
