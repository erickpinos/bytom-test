import requests
import json

erick_account = '0UKOBDPC00A02'
erick_key = '0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582'
erick_program = '00143acfa10b486c9690c91ef8112f0472774d1c6b05'

mel_account = '0UKOEPK7G0A04'
mel_key = '9485475a74ce493a6299b44b7488997e9278f32d6aee00b15fa2a07ee4ce2688'
mel_program = '001403fa045e4417f378243c2779f11b8204d5cd82a9'

#data = open('create-account-receiver.json')
#response = requests.post('http://localhost:9888/list-pubkeys', data=data)

#print(response.text)

#print(response.text)

#response = requests.post('http://localhost:9888/build-transaction', data=data)

#compilation-payload = open('compilation-payload.json')
#build-contractLoad-txt-payload = open('build-contractLoad-tx-payload.json')
#sign-contractLoad-txt-payload = open('sign-contractLoad-tx-payload.json')
#submit-contractLoad-txt-payload = open('submit-contractLoad-tx-payload.json')

compilation_payload_data = {
    "contract": "contract LockPosition(expireBlockHeight: Integer, saver: Program, saver_key: PublicKey) locks lockAmount of lockAsset { clause expire(sig: Signature) { verify above(expireBlockHeight)  verify checkTxSig(saver_key, sig) lock lockAmount of lockAsset with saver } }",
    "args": [
        {"integer": 100 },
	{"string": "00143acfa10b486c9690c91ef8112f0472774d1c6b05"},
	{"string": "0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582"}
    ]
}

with open("compilation-payload.json", "w") as write_file:
    json.dump(compilation_payload_data, write_file)

compilation = open('compilation-payload.json')

#compilation_result = {"status":"success","data":{"name":"LockPosition","source":"contract LockPosition(expireBlockHeight: Integer, saver: Program, saver_key: PublicKey) locks lockAmount of lockAsset { clause expire(sig: Signature) { verify above(expireBlockHeight)  verify checkTxSig(saver_key, sig) lock lockAmount of lockAsset with saver } }","program":"200ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af81308735821600143acfa10b486c9690c91ef8112f0472774d1c6b0501647410cd9f697b7bae7cac6900c3c251547ac100c0","params":[{"name":"expireBlockHeight","type":"Integer"},{"name":"saver","type":"Program"},{"name":"saver_key","type":"PublicKey"}],"value":"lockAmount of lockAsset","clause_info":[{"name":"expire","params":[{"name":"sig","type":"Signature"}],"blockheight":["expireBlockHeight"],"values":[{"name":"","program":"saver","asset":"lockAsset","amount":"lockAmount"}]}],"opcodes":"0x0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582 0x00143acfa10b486c9690c91ef8112f0472774d1c6b05 0x64 DEPTH 0xcd9f697b7bae7cac6900c3c251547ac1 FALSE CHECKPREDICATE","error":""}}

compilation_result = requests.post('http://localhost:9888/compile', data=compilation)
print(compilation_result.text)
with open("compilation-payload.json", "w") as write_file:
    json.dump(compilation_payload_data, write_file)

decoded_hand = json.loads(compilation_result.text)

program = decoded_hand.get('data').get('program')
print(program)
build_contractLoad_tx_payload_data = {
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
      "control_program": program,
      "type": "control_program"
    }
  ],
  "ttl": 0,
  "time_range": 1521625823
}

with open("build-contractLoad-tx-payload.json", "w") as write_file:
    json.dump(build_contractLoad_tx_payload_data, write_file)

#Compile
#response = requests.post('http://localhost:9888/compile', data=compilation-payload)
