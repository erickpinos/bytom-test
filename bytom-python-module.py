import requests
import json

erick_account = '0UKOBDPC00A02'
erick_address = '0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582'
erick_program = '00143acfa10b486c9690c91ef8112f0472774d1c6b05'

mel_account = '0UKOEPK7G0A04'
mel_address = '9485475a74ce493a6299b44b7488997e9278f32d6aee00b15fa2a07ee4ce2688'
mel_program = '001403fa045e4417f378243c2779f11b8204d5cd82a9'

gold_id = '82ec80b9f81217b8c912322fb3f505b1e542b4e58cebb7c128081fbe0d8584c2'

compile_input_python = {
    "contract": "contract LockPosition(expireBlockHeight: Integer, saver: Program, saver_key: PublicKey) locks lockAmount of lockAsset { clause expire(sig: Signature) { verify above(expireBlockHeight)  verify checkTxSig(saver_key, sig) lock lockAmount of lockAsset with saver } }",
    "args": [
        {"integer": 100 },
        {"string": erick_program},
        {"string": erick_address}
    ]
}

def compileContract(contract):
    data = json.dumps(contract)
    response = requests.post('http://localhost:9888/compile', data=data)
    result = json.loads(response.text).get('data')
    return result

def getProgram(compiled_contract):
    control_program = compiled_contract.get('program')
    return control_program

def buildTransaction(account_id, asset_id, control_program):
    payload = {
      "base_transaction": None,
      "actions": [
        {
          "account_id": account_id,
          "amount": 100000000,
          "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
          "type": "spend_account"
        },
        {
          "account_id": account_id,
          "amount": 1000000000,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "amount": 1000000000,
          "asset_id": asset_id,
          "control_program": control_program,
          "type": "control_program"
        }
      ],
      "ttl": 0,
      "time_range": 1521625823
    }

    data = json.dumps(payload)
    response = requests.post('http://localhost:9888/build-transaction', data=data)
    result = json.loads(response.text).get('data')
    return result

def signTransaction():
    info = {
      "password": "12345",
      "transaction": transaction_data
    }

    data = json.dumps(info)
    response = requests.post('http://localhost:9888/sign-transaction', data=data)
    result = json.loads(response.text)
    return result

def getRawTransactionData(data):
    result = data.get('transaction').get('raw_transaction')
    return result

def submitTransaction():
    info = {
        "raw_transaction": raw_transaction
    }

    data = json.dumps(info)
    response = requests.post('http://localhost:9888/submit-transaction', data=data)
    result = json.loads(response.text)
    return result

def main():
    print("calling compileContract")
    compiled_contract = compileContract(compile_input_python)
    print(compiled_contract)
    print("finished compileContract")
    print("\n")
    print("calling getProgram")
    control_program = getProgram(compiled_contract)
    print(control_program)
    print("finished getProgram")
    print("\n")
    print("calling buildTransaction")
    transaction_data = buildTransaction(control_program)
    print(transaction_data)
    print("finished buildTransaction")
    print("\n")
    print("calling signTransaction")
    signresult = signTransaction()
    print(signresult)
    print("finished signTransaction")
    print("\n")
    print("calling getRawTransactionData")
    raw_transaction = getRawTransactionData()
    print(raw_transaction)
    print("finished getRawTransactionData")
    print("\n")
    print("calling submitTransaction")
    submitted_transaction = submitTransaction()
    print(submitted_transaction)
    print("finished submitTransaction")

main()
