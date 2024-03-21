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
def create_genesis_block():
    index = 0
    previous_hash = "0"
    timestamp = int(time.time())
    data = "Genesis Block"
    nonce = 0

    while True:
        hash = calculate_hash(index, previous_hash, timestamp, data, nonce)
        if hash.startswith("0000"):  # Adjust the difficulty level as needed
            break
        nonce += 1

    return Block(index, previous_hash, timestamp, data, hash)

# Adjust calculate_hash to include nonce
def calculate_hash(index, previous_hash, timestamp, data, nonce):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data) + str(nonce)
    return hashlib.sha256(value.encode()).hexdigest()
