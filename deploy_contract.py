from web3 import Web3
import json
from solcx import compile_source
from solcx import set_solc_version
set_solc_version("0.8.0")


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

with open("contract.sol", "r") as file:
    contract_source = file.read()

compiled = compile_source(contract_source)
contract_id, contract_interface = compiled.popitem()

FraudChain = web3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
tx_hash = FraudChain.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

with open("abi.json", "w") as f:
    json.dump(contract_interface["abi"], f)

print("Contract deployed at:", tx_receipt.contractAddress)
