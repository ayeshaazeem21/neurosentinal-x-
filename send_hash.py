from web3 import Web3
import json

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

with open("abi.json") as f:
    abi = json.load(f)

contract_address = "0xD6da43978002900E3382416c5B53d0cb2797E3dA"
contract = web3.eth.contract(address=contract_address, abi=abi)

fraud_hash = "abc1234deadbeef"
tx = contract.functions.storeHash(fraud_hash).transact()
receipt = web3.eth.wait_for_transaction_receipt(tx)
print("Stored hash on blockchain.")
