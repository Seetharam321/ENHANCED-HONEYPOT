import streamlit as st
import pandas as pd
import hashlib
import matplotlib.pyplot as plt
import seaborn as sns
import time
import random

# Function to calculate hash for data
def calculate_hash(data):
    data_str = ''.join(str(value) for value in data)
    return hashlib.sha256(data_str.encode()).hexdigest()
def generate_log_hash(log_data):
    return calculate_hash(log_data.values())
# Function to check if event is malicious based on blockchain records
def check_malicious_event(event_type, source_ip, destination_ip, blockchain_data):
    for index, row in blockchain_data.iterrows():
        block_data = [row['index'], row['timestamp'], row['event_type'], row['source_ip'], row['destination_ip']]
        if event_type == row['event_type'] and source_ip == row['source_ip'] and destination_ip == row[
            'destination_ip']:
            if calculate_hash(block_data) == row['hash']:
                return True
    return False

# Function to plot event type distribution
def plot_event_type_distribution(blockchain_data):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(data=blockchain_data, x='event_type', palette='Set2', ax=ax)
    ax.set_title('Event Type Distribution')
    ax.set_xlabel('Event Type')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    return fig

# Function to plot top 5 source IPs
def plot_top_source_ips(blockchain_data):
    top_source_ips = blockchain_data['source_ip'].value_counts().head(5)
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=top_source_ips.index, y=top_source_ips.values, palette='Set3', ax=ax)
    ax.set_title('Top 5 Source IPs')
    ax.set_xlabel('Source IP')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    return fig

# Function to plot top 5 destination IPs
def plot_top_destination_ips(blockchain_data):
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
event_type_filter = st.sidebar.selectbox('Event Type', ['All', 'Malicious Activity', 'Suspicious Activity'])

# Enable real-time updates
realtime_updates_enabled = st.sidebar.checkbox('Enable Real-time Updates')

# Initial empty DataFrame for blockchain data
blockchain_data = pd.DataFrame(columns=['index', 'timestamp', 'event_type', 'source_ip', 'destination_ip', 'hash'])

# Display initial filtered data
filtered_data = blockchain_data.copy()
if event_type_filter != 'All':
    filtered_data = filtered_data[filtered_data['event_type'] == event_type_filter]

# Display initial blockchain records
st.subheader('Blockchain Records')
records_table = st.table(filtered_data)

# Display initial event type distribution plot
event_type_distribution_fig = plot_event_type_distribution(filtered_data)
event_type_distribution_plot = st.pyplot(event_type_distribution_fig)

# Display initial top 5 source IPs
top_source_ips_fig = plot_top_source_ips(filtered_data)
top_source_ips_plot = st.pyplot(top_source_ips_fig)

# Display initial top 5 destination IPs
top_destination_ips_fig = plot_top_destination_ips(filtered_data)
top_destination_ips_plot = st.pyplot(top_destination_ips_fig)
import os
def generate_random_hash():
    # Generate a random input (e.g., random bytes)
    random_input = os.urandom(32)  # 32 bytes for SHA-256

    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()

    # Update the hash object with the random input
    hash_object.update(random_input)

    # Get the hexadecimal representation of the hash value
    hash_value = hash_object.hexdigest()

    return hash_value
# Main loop for real-time updates
while realtime_updates_enabled:
    # Generate new log data
    new_log = {
        'index': len(blockchain_data) + 1,
        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
        'event_type': random.choice(['Malicious Activity', 'Suspicious Activity']),
        'source_ip': f'192.168.1.{random.randint(1, 255)}',
        'destination_ip': f'10.0.0.{random.randint(1, 255)}',
          # Replace this with actual hash calculation
    }

    new_log['hash'] = generate_random_hash()
    # Append new log to the blockchain data
    blockchain_data = pd.concat([blockchain_data, pd.DataFrame([new_log])])

    # Update filtered data based on event type filter
    filtered_data = blockchain_data.copy()
    if event_type_filter != 'All':
        filtered_data = filtered_data[filtered_data['event_type'] == event_type_filter]

    # Update blockchain records table
    records_table.table(filtered_data)

    # Update event type distribution plot
    event_type_distribution_fig = plot_event_type_distribution(filtered_data)
    event_type_distribution_plot.pyplot(event_type_distribution_fig)

    # Update top 5 source IPs plot
    top_source_ips_fig = plot_top_source_ips(filtered_data)
    top_source_ips_plot.pyplot(top_source_ips_fig)

    # Update top 5 destination IPs plot
    top_destination_ips_fig = plot_top_destination_ips(filtered_data)
    top_destination_ips_plot.pyplot(top_destination_ips_fig)

    # Pause for a while before generating the next log
    time.sleep(5)  # Adjust the interval as needed

#sudo iptables -A INPUT -s <IP_ADDRESS_TO_BLOCK> -j DROP

