import requests

erick_account = '0UKOBDPC00A02'
erick_key = '0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582'
erick_program = '00143acfa10b486c9690c91ef8112f0472774d1c6b05'

mel_account = '0UKOEPK7G0A04'
mel_key = '9485475a74ce493a6299b44b7488997e9278f32d6aee00b15fa2a07ee4ce2688'
mel_program = '001403fa045e4417f378243c2779f11b8204d5cd82a9'

#data = open('create-account-receiver.json')
#response = requests.post('http://localhost:9888/list-pubkeys', data=data)

#print(response.text)

#data = open('compilation-payload.json')
#response = requests.post('http://localhost:9888/compile', data=data)

#print(response.text)

test1 = {"status":"success","data":{"root_xpub":"a8d18922ae6600629d72473dd01815a74bdfbec210605a9b0d2a96d93faa5eecda17e8d51c863c158f7bcf5df80c3d4d6c2726b9a07bc2c7e4ea16e499b1af73","pubkey_infos":[{"pubkey":"0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582","derivation_path":["2c000000","99000000","01000000","01000000","01000000"]},{"pubkey":"5a7b8bde11e45e7348b8a8e2c7f4a9394ae615215ba19d7d36878e6c92291ac0","derivation_path":["2c000000","99000000","01000000","01000000","02000000"]},{"pubkey":"f87595fd4ba417f93eb55c2b5b5f8e4a0959a2d34f61aac30003ef7137c04a41","derivation_path":["2c000000","99000000","01000000","01000000","03000000"]},{"pubkey":"022676689b547f08131e6ef3dc61c8d27c494ae0181afd7afa7d1aa189e11b31","derivation_path":["2c000000","99000000","01000000","01000000","04000000"]},{"pubkey":"1cbc32207a9313311041a69f27578b43f5975566ab2a7a2955a0698a74947e6e","derivation_path":["2c000000","99000000","01000000","01000000","05000000"]},{"pubkey":"86e548c997b2d6dbc081273e69a4395bcbe5cb4ccc303720bceb661b53c952dd","derivation_path":["2c000000","99000000","01000000","01000000","06000000"]},{"pubkey":"7aa6a55193fac84703ede0b4c9590c6eec05fe498c3949035863a50d3a065595","derivation_path":["2c000000","99000000","01000000","01000000","07000000"]},{"pubkey":"20363ce25398fba505c6b5f01a910ae39b18463fc359471a320c54ddc21f5718","derivation_path":["2c000000","99000000","01000000","01000000","08000000"]},{"pubkey":"2b0682613512f4e6faac5c601ca6467180fa8d326338745b606f5615e28fe819","derivation_path":["2c000000","99000000","01000000","01000000","09000000"]},{"pubkey":"dc644cb234d4e29a006a35622e6a6193fc1f9072b985396518d284e2c0616ef7","derivation_path":["2c000000","99000000","01000000","01000000","0a000000"]},{"pubkey":"e6b14df299a3cb1d5e6452eeeac8935f30a3f8c8470faacd9330b0f3bce6535a","derivation_path":["2c000000","99000000","01000000","01000000","0b000000"]},{"pubkey":"a482a0c25563fefe09eff4f55239c4f901ba429bb7c9c72b53a795658510cc56","derivation_path":["2c000000","99000000","01000000","01000000","0c000000"]},{"pubkey":"32a487a83ff8dec60adf16a2669058ef578d8cc337c390620c9e2408f1c865b9","derivation_path":["2c000000","99000000","01000000","01000000","0d000000"]},{"pubkey":"859c7cbe4e8e962ad1a69f6fb8c79b8ae7a708e8172861ec961cee24665285b9","derivation_path":["2c000000","99000000","01000000","01000000","0e000000"]},{"pubkey":"772a9d570410dad294ae9fd6e3575673066c898606041994bae4100d6a04dd5a","derivation_path":["2c000000","99000000","01000000","01000000","0f000000"]},{"pubkey":"3c29d5faa6cd75538ea603d3e4b99538740a58bb2f1b5db0a4c4f61608589cb4","derivation_path":["2c000000","99000000","01000000","01000000","10000000"]},{"pubkey":"12aaba59d6b4a9ab428afb80d33011a5543cccf172f36576fe5b0dda66bcc17d","derivation_path":["2c000000","99000000","01000000","01000000","11000000"]},{"pubkey":"b837104cda2b42d9dff826f9b0bd2eef732e7bbbc5232f048f683c9fd84dd021","derivation_path":["2c000000","99000000","01000000","01000000","12000000"]},{"pubkey":"f25b5f0a04296a6750d535e5102fafa0093238c65cbc9476dea74725d1d69a3e","derivation_path":["2c000000","99000000","01000000","01000000","13000000"]},{"pubkey":"a2d167c880cbb2b84b8f17c85233d48ddd13a82f8a0df4586f4f349be55541ec","derivation_path":["2c000000","99000000","01000000","01000000","14000000"]},{"pubkey":"8b32405635ff1ed7c1774413a92f7ab8aaf9b62a262b949c75d42757be61574a","derivation_path":["2c000000","99000000","01000000","01000000","15000000"]},{"pubkey":"1eb1b45fed8f4b98600873809cde9563807002aaf5a9012f26a4be0cd599a537","derivation_path":["2c000000","99000000","01000000","01000000","16000000"]},{"pubkey":"74b80a98149e29b04bffa869fd7a95267699e5d31e20e59c3ebbfcaf6fc246ab","derivation_path":["2c000000","99000000","01000000","01000000","17000000"]},{"pubkey":"d539e16729fc84f5f7609c584682fe8bb2a30d62d016b5d171abf7e884612fff","derivation_path":["2c000000","99000000","01000000","01000000","18000000"]},{"pubkey":"58acce3ed69d2ed94acaaad102d1c608dda01ccfbafd1dbb0a74c42ffa4ad4d8","derivation_path":["2c000000","99000000","01000000","01000000","19000000"]},{"pubkey":"4573bc515d2b69df25521e640a0cc9b386be12dafdf68b4021f5d55cdeebe089","derivation_path":["2c000000","99000000","01000000","01000000","1a000000"]},{"pubkey":"1128d6a9d28ab77a38b9af36cda3c1e6c1841b9e7ed4ff37c6f23313586491c2","derivation_path":["2c000000","99000000","01000000","01000000","1b000000"]},{"pubkey":"19197878bd252d86f033eaa39ec8c1a2be2b57bb41cbc8c78751f9a18bc97bf9","derivation_path":["2c000000","99000000","01000000","01000000","1c000000"]},{"pubkey":"64466b92e6ad86154f50d0fabd4ce943bf600c2f7e4cd26cf32d42b73a832dc5","derivation_path":["2c000000","99000000","01000000","01000000","1d000000"]},{"pubkey":"5b47bd3d310adc5717173b51ad1868b55542324bad2f0e4971c080b637044f7e","derivation_path":["2c000000","99000000","01000000","01000000","1e000000"]},{"pubkey":"ec17004cce0511732e7f5b71e672cef3a155588d38d2f692608098ac4a74704b","derivation_path":["2c000000","99000000","01000000","01000000","1f000000"]},{"pubkey":"bbb550582f50337a2db754526774716413878d02fe41f32eeaa10ef81f140ad9","derivation_path":["2c000000","99000000","01000000","01000000","20000000"]},{"pubkey":"b475b85d0ac6820d7fc32c2db365421853fe376074f16c87a8b539b0b18d1232","derivation_path":["2c000000","99000000","01000000","01000000","21000000"]},{"pubkey":"3ac055867f6b55c67fe5f8db474e7c5698edb990bf9d1537dde7eb4524edfecb","derivation_path":["2c000000","99000000","01000000","01000000","22000000"]},{"pubkey":"d68b326299bb271e4615b0b011cfc84ed506ed82e5db66c738fd3dafd4273ebb","derivation_path":["2c000000","99000000","01000000","01000000","23000000"]},{"pubkey":"0236d251380453808f01fc9aff1315a8f6e263efbaecc47cd10238438893c545","derivation_path":["2c000000","99000000","01000000","01000000","24000000"]},{"pubkey":"087f2e00c370878fc8e2615620c9ae0e908569a3521418ae85a915d7b80f4f7d","derivation_path":["2c000000","99000000","01000000","01000000","25000000"]},{"pubkey":"406ca6cb43cf7c86ac5c56efca94565e55b5379a7ab22868abc52589327ea2bb","derivation_path":["2c000000","99000000","01000000","01000000","26000000"]},{"pubkey":"743aaa14862288f3c3a2732cd42f132de83f35e3de3c2f3a5fcd905f7ced7f7f","derivation_path":["2c000000","99000000","01000000","01000000","27000000"]},{"pubkey":"7438a9ee3d6e36fe8d81e5fb6d0ad2aa7d05021bc95a50a187774d506e25845f","derivation_path":["2c000000","99000000","01000000","01000000","28000000"]},{"pubkey":"a66f1fdc07c69b639f8966e7fdb9efcd76951261bc930cda466a9d3730eac62b","derivation_path":["2c000000","99000000","01000000","01000000","29000000"]},{"pubkey":"f0ddf3259a310ad66605c8278844c60fd60e72a69a7fd5cd707f6bef431c3cc7","derivation_path":["2c000000","99000000","01000000","01000000","2a000000"]},{"pubkey":"18c56788371c8faaf28859efb555bd602a583491f39be723d7d4ea4962227e74","derivation_path":["2c000000","99000000","01000000","01000000","2b000000"]},{"pubkey":"cc64d6800f72bf8e541df1e3e13475f38c21e15b2f44c6bda49c537c16f2f5b4","derivation_path":["2c000000","99000000","01000000","01000000","2c000000"]},{"pubkey":"6018c1d7b346da4cc2d6f107c0e2879af4635ba93bb8d97a0f38920693d12c6e","derivation_path":["2c000000","99000000","01000000","01000000","2d000000"]},{"pubkey":"56b84fa7e33bc095662d1ddacb2cfa3981d693a4881a961fe02af4c52adf6bfa","derivation_path":["2c000000","99000000","01000000","01000000","2e000000"]},{"pubkey":"a89bb46c1a42ce6349c1ac969e87b48bfc803c8a9ae28d50da6af3e8718e6098","derivation_path":["2c000000","99000000","01000000","01000000","2f000000"]},{"pubkey":"9eed9354d0a219beddb6c39e923b5a9138f5c782b47fa1a663d913a163675955","derivation_path":["2c000000","99000000","01000000","01000000","30000000"]},{"pubkey":"dfec922246c5d0ee22714bfdc15b0cf03bd8b96bc7ff291f6f63fb5b75bfb4fe","derivation_path":["2c000000","99000000","01000000","01000000","31000000"]},{"pubkey":"e6ffb2fdc1ace99159d7f5df3fedaeb20f819a0a453b8eba79145cd7ed367039","derivation_path":["2c000000","99000000","01000000","01000000","32000000"]},{"pubkey":"f3b17f4cb449b5124701d7a3893483d68a3fc662ff345cabd89813a69c198466","derivation_path":["2c000000","99000000","01000000","01000000","33000000"]},{"pubkey":"1c8eb9eab78170c09df1e3daacad382fcbf28f037b40f4face2864ff2505931d","derivation_path":["2c000000","99000000","01000000","01000000","34000000"]},{"pubkey":"f42d758d11d1e5924b3fd35245b9380a85a9ef19aeaf794e66578a0949ae4200","derivation_path":["2c000000","99000000","01000000","01000000","35000000"]},{"pubkey":"a1cefd08c7ff62d19c1f3e8ef3ea3859a44de4d9f20ca57b78ec7c240833afdb","derivation_path":["2c000000","99000000","01000000","01000000","36000000"]},{"pubkey":"73b0099fb4f19ddadb23feae1019fa448406f35812d2c9078812532cfa3e6187","derivation_path":["2c000000","99000000","01000000","01000000","37000000"]},{"pubkey":"bcc221831eeee0aa10fbc23edb99aacaa2fdc4c5852d6042b58fe7194fc4d013","derivation_path":["2c000000","99000000","01000000","01000000","38000000"]},{"pubkey":"879ce109b9588951150e56b119257bd2f3c62f48652da1f05ba7b9808145155e","derivation_path":["2c000000","99000000","01000000","01000000","39000000"]},{"pubkey":"8d153bca94584394ca5c6d328ac0e01cc44d47d3b7b729f1069694af46139363","derivation_path":["2c000000","99000000","01000000","01000000","3a000000"]},{"pubkey":"e5a8c297b4c8f8cabdbd8696e05d0f63a517c797d49c85d005fd78e322ed58b1","derivation_path":["2c000000","99000000","01000000","01000000","3b000000"]},{"pubkey":"6027df8d074482df9798bc159ea54e956cc99745a350b71e52518569ceca7fab","derivation_path":["2c000000","99000000","01000000","01000000","3c000000"]},{"pubkey":"31fbe728a2831447e771ff7bc05e66ade293c81f2924704dbe62ef27293e3839","derivation_path":["2c000000","99000000","01000000","01000000","3d000000"]},{"pubkey":"619aa48cb03d6591888d822a59b5ba9c2f136b32e8d30905ce75ea60b57d48bb","derivation_path":["2c000000","99000000","01000000","00000000","01000000"]},{"pubkey":"0ea307d3c2d4dc6187c89f5fbd9e3f3774360181de0521a8c9defbc13f56e9e4","derivation_path":["2c000000","99000000","01000000","00000000","02000000"]}]}}
test2 = {"status":"success","data":{"name":"LockPosition","source":"contract LockPosition(expireBlockHeight: Integer, saver: Program, saver_key: PublicKey) locks lockAmount of lockAsset { clause expire(sig: Signature) { verify above(expireBlockHeight)  verify checkTxSig(saver_key, sig) lock lockAmount of lockAsset with saver } }","program":"200ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af81308735821600143acfa10b486c9690c91ef8112f0472774d1c6b0501647410cd9f697b7bae7cac6900c3c251547ac100c0","params":[{"name":"expireBlockHeight","type":"Integer"},{"name":"saver","type":"Program"},{"name":"saver_key","type":"PublicKey"}],"value":"lockAmount of lockAsset","clause_info":[{"name":"expire","params":[{"name":"sig","type":"Signature"}],"blockheight":["expireBlockHeight"],"values":[{"name":"","program":"saver","asset":"lockAsset","amount":"lockAmount"}]}],"opcodes":"0x0ff578cc3228fe697a47d178081a1d642e677c637f1c9ecb7434af8130873582 0x00143acfa10b486c9690c91ef8112f0472774d1c6b05 0x64 DEPTH 0xcd9f697b7bae7cac6900c3c251547ac1 FALSE CHECKPREDICATE","error":""}}

print(test2.get('data').get('program'))