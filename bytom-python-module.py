import requests
import json

erick_account = '0UKOBDPC00A02'
erick_address = '0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582'
erick_program = '00143acfa10b486c9690c91ef8112f0472774d1c6b05'

mel_account = '0UKOEPK7G0A04'
mel_address = '9485475a74ce493a6299b44b7488997e9278f32d6aee00b15fa2a07ee4ce2688'
mel_program = '001403fa045e4417f378243c2779f11b8204d5cd82a9'

gold_id = '82ec80b9f81217b8c912322fb3f505b1e542b4e58cebb7c128081fbe0d8584c2'

def getProgram(data):
    result = data.get('program')
    return result

def getRawTransaction(data):
    result = data.get('transaction').get('raw_transaction')
    return result

def compileContract(program, address):
    payload = {
        "contract": "contract LockPosition(expireBlockHeight: Integer, saver: Program, saver_key: PublicKey) locks lockAmount of lockAsset { clause expire(sig: Signature) { verify above(expireBlockHeight)  verify checkTxSig(saver_key, sig) lock lockAmount of lockAsset with saver } }",
        "args": [
            {"integer": 100 },
            {"string": program},
            {"string": address}
        ]
    }

    result = curl('compile',payload).get('data')
    return result

def buildTransaction(account_id, asset_id, amount, control_program):
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
          "amount": amount,
          "asset_id": asset_id,
          "type": "spend_account"
        },
        {
          "amount": amount,
          "asset_id": asset_id,
          "control_program": control_program,
          "type": "control_program"
        }
      ],
      "ttl": 0,
      "time_range": 1521625823
    }

    result = curl('build-transaction',payload).get('data')
    return result

def signTransaction(transaction):
    payload = {
      "password": "12345",
      "transaction": transaction
    }

    result = curl('sign-transaction',payload).get('data')
    return result

def submitTransaction(raw_transaction):
    payload = {
        "raw_transaction": raw_transaction
    }

    result = curl('submit-transaction',payload).get('data')
    return result

def curl(command, payload):
    url = 'http://localhost:9888/' + command
    data = json.dumps(payload)
    response = requests.post(url, data=data)
    result = json.loads(response.text)
    return result

def main():
    print("calling compileContract")
    compiled_contract = compileContract(erick_program, erick_address)
    print(compiled_contract)
    print("finished compileContract")
    print("\n")
    
    print("calling getProgram")
    control_program = getProgram(compiled_contract)
    print(control_program)
    print("finished getProgram")
    print("\n")

    print("calling buildTransaction")
    build_output = buildTransaction(erick_account, gold_id, 100000000, control_program)
    print(build_output)
    print("finished buildTransaction")
    print("\n")

    print("calling signTransaction")
    sign_output = signTransaction(build_output)
    print(sign_output)
    print("finished signTransaction")
    print("\n")

    print("calling getRawTransactionData")
    raw_transaction = getRawTransaction(sign_output)
    print(raw_transaction)
    print("finished getRawTransactionData")
    print("\n")

    print("calling submitTransaction")
    submit_output = submitTransaction(raw_transaction)
    print(submit_output)
    print("finished submitTransaction")

main()
