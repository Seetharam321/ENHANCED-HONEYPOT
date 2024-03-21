import socket
import threading
import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

# Create blockchain with a genesis block
blockchain = [create_genesis_block()]

# Function to add a new block to the blockchain
def add_block(data):
    index = len(blockchain)
    previous_block = blockchain[-1]
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    new_block = Block(index, previous_block.hash, timestamp, data, hash)
    blockchain.append(new_block)

# Example: Adding a block to the blockchain
add_block("Honeypot Event Detected")
class SmartContract:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

# Example Smart Contract: Block IP if "Intrusion" is detected
intrusion_smart_contract = SmartContract(condition="Intrusion", action="Block IP")

# Function to check conditions and execute smart contracts
def execute_smart_contracts(data):
    for contract in smart_contracts:
        if contract.condition in data:
            print(f"Executing Smart Contract: {contract.action}")

# Example: Executing smart contracts based on honeypot data
smart_contracts = [intrusion_smart_contract]
execute_smart_contracts("Intrusion Detected")

# Function to share threat intelligence with peers
def share_threat_intelligence(data):
    for peer in peers:
        send_data_to_peer(peer, data)

# Function to send data to a peer
def send_data_to_peer(peer, data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(peer)
        s.sendall(data.encode())
        s.close()
    except Exception as e:
        print(f"Error sending data to {peer}: {str(e)}")

# Example: Sharing threat intelligence with peers
peers = [("peer1_ip", 9000), ("peer2_ip", 9000)]
share_threat_intelligence("New Threat Detected")
# Adding blockchain and smart contract functionalities from Part 1 and Part 2

# Function to add a new block to the blockchain with smart contract execution
def add_block_with_smart_contracts(data):
    add_block(data)
    execute_smart_contracts(data)

# Function to add a new block to the blockchain with threat intelligence sharing
def add_block_with_threat_intelligence(data):
    add_block(data)
    share_threat_intelligence(data)

# Example: Adding a block with smart contract execution and threat intelligence sharing
add_block_with_smart_contracts("Intrusion Detected")
add_block_with_threat_intelligence("New Threat Detected")

# Function to add a new block to the blockchain with smart contract execution and threat intelligence sharing
def add_block_with_smart_contracts_and_threat_intelligence(data):
    add_block(data)
    execute_smart_contracts(data)
    share_threat_intelligence(data)

# Example: Adding a block with smart contract execution and threat intelligence sharing
add_block_with_smart_contracts_and_threat_intelligence("Intrusion Detected")

# Function to add a new block to the blockchain with honeypot data, smart contract execution, and threat intelligence sharing
def add_block_with_honeypot_data_smart_contracts_and_threat_intelligence(data):
    add_block_with_honeypot_data(data)
    execute_smart_contracts(data)
    share_threat_intelligence(data)

# Example: Adding a block with honeypot data, smart contract execution, and threat intelligence sharing
add_block_with_honeypot_data_smart_contracts_and_threat_intelligence("New Threat Detected")
def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

# Create blockchain with a genesis block
blockchain = [create_genesis_block()]

# Function to add a new block to the blockchain with honeypot data
def add_block_with_honeypot_data(data):
    add_block(data)

# Example: Adding a block with honeypot data
add_block_with_honeypot_data("Honeypot Event Detected")