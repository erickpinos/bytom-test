import requests
import json

erick_account = '0UKOBDPC00A02'
erick_address = '0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582'
erick_program = '00143acfa10b486c9690c91ef8112f0472774d1c6b05'

mel_account = '0UKOEPK7G0A04'
mel_address = '9485475a74ce493a6299b44b7488997e9278f32d6aee00b15fa2a07ee4ce2688'
mel_program = '001403fa045e4417f378243c2779f11b8204d5cd82a9'

gold_id = '82ec80b9f81217b8c912322fb3f505b1e542b4e58cebb7c128081fbe0d8584c2'

#response = requests.post('http://localhost:9888/build-transaction', data=data)

#compilation-payload = open('compilation-payload.json')
#build-contractLoad-txt-payload = open('build-contractLoad-tx-payload.json')
#sign-contractLoad-txt-payload = open('sign-contractLoad-tx-payload.json')
#submit-contractLoad-txt-payload = open('submit-contractLoad-tx-payload.json')

# Compile the Contract

# Make Python Version
compile_input_python = {
    "contract": "contract LockPosition(expireBlockHeight: Integer, saver: Program, saver_key: PublicKey) locks lockAmount of lockAsset { clause expire(sig: Signature) { verify above(expireBlockHeight)  verify checkTxSig(saver_key, sig) lock lockAmount of lockAsset with saver } }",
    "args": [
        {"integer": 100 },
	{"string": erick_program},
	{"string": erick_address}
    ]
}
print(compile_input_python)

# Make JSON Version
with open("compile.json", "w") as write_file:
    json.dump(compile_input_python, write_file)
compile_input_json = open('compile.json')
print(compile_input_json)

# Compile
compile_output_json = requests.post('http://localhost:9888/compile', data=compile_input_json)
print(compile_output_json)
print(compile_output_json.text)

# Get the program
compile_output_python = json.loads(compile_output_json.text)

control_program = compile_output_python.get('data').get('program')
print(control_program)


# Built the Transaction
build_input_python = {
  "base_transaction": None,
  "actions": [
    {
      "account_id": "0UKOBDPC00A02",
      "amount": 100000000,
      "asset_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
      "type": "spend_account"
    },
    {
      "account_id": "0UKOBDPC00A02",
      "amount": 10000000000,
      "asset_id": "82ec80b9f81217b8c912322fb3f505b1e542b4e58cebb7c128081fbe0d8584c2",
      "type": "spend_account"
    },
    {
      "amount": 10000000000,
      "asset_id": "82ec80b9f81217b8c912322fb3f505b1e542b4e58cebb7c128081fbe0d8584c2",
      "control_program": control_program,
      "type": "control_program"
    }
  ],
  "ttl": 0,
  "time_range": 1521625823
}


# Make JSON Version
with open("build-input.json", "w") as write_file:
    json.dump(build_input_python, write_file)

build_input_json = open('build-input.json')
print(build_input_json)

# Build the transaction
build_output_json = requests.post('http://localhost:9888/build-transaction', data=build_input_json)
print(build_output_json.text)
