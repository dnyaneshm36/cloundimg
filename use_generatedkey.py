import json
import requests
import os 
import string
import random
import timeit

start = timeit.default_timer()


result = 0

LOCALHOST = "http://localhost:8080/"
CYTOPTO_HEROKU = "https://criptography-dnyanesh.herokuapp.com/"

ENDPOINT = LOCALHOST
headers = {
     "Content-Type": "application/json"
}


for i in range(1):
    words = ['first','second','third']
    # for j in range(10):
    #     N =random.randint(0,19)
    #     word = ''.join(random.choices(string.ascii_uppercase +
    #                             string.digits, k = N))
    #     words.append(word)
    

    print("words generated: \n",words)
    wordchecking = words[0]
    print("word Searching: \n",wordchecking)
    Requestdata = ""
    r = requests.get(ENDPOINT+"microservice/clpeks/setup",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata['p'])

    p = 'UD8405i0/AnYkf0z90G08/E4BLCaCUfRbQLeHR1fU8ke8mjnjxMotUXCb0ETTk3YdbsGq8dn1TCeGobju6piDXX4Ec5oP4CNdIx9B3z4m3R3yGq0fmZGjHrFXzaqn0jSVz7fAD4+ZiZ4LJZFiCNPtuFO+WvbmRRRIhlH5ozWsF4='
    master_key_lambda = 'JAU8bnne/7hs7O9bwlazKQTDgwg='
    # PKc = Responddata["pkc"]

    senderid = "dnyaneshwardmogal3"
    receiverid = "dnyaneshdmogal36"
    # N =random.randint(0,9)
    # senderid = ''.join(random.choices(string.ascii_uppercase +
    #                          string.digits, k = N))
    # N =random.randint(0,9)
    # receiverid = ''.join(random.choices(string.ascii_uppercase +
    #                          string.digits, k = N))
    r = requests.get(ENDPOINT+"microservice/clpeks/ePPK/"+senderid,data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    Qs = Responddata["qu"]
    Ds = Responddata["du"]

    r = requests.get(ENDPOINT+"microservice/clpeks/ePPK/"+receiverid,data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    Qr = Responddata["qu"]
    Dr = Responddata["du"]
    # # Qr = Qs
    # # Dr = Qs


    r = requests.get(ENDPOINT+"microservice/clpeks/sSV",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    Ss = Responddata["su"]
    r = requests.get(ENDPOINT+"microservice/clpeks/sSV",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    Sr = Responddata["su"]
    Sr = Ss

    Ss = 'S0HQnrzbhr93akaPQF6ldxk+o+k='
    Sr = 'YLdvCJQqmcnAbcPyVp9yVHbBgqM='

    Requestdata={
        "su":Ss,
        "du":Ds
    }   
    r = requests.get(ENDPOINT+"microservice/clpeks/gPriK",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    SKs1 = Responddata["sku1"]
    SKs2 = Responddata["sku2"]

    Requestdata={
        "su":Sr,
        "du":Dr
    }   
    r = requests.get(ENDPOINT+"microservice/clpeks/gPriK",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    SKr1 = Responddata["sku1"]
    SKr2 = Responddata["sku2"]


    Requestdata={
        "su":Ss
    }

    r = requests.get(ENDPOINT+"microservice/clpeks/gPubK",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    # PKs1 = Responddata["pku1"]
    # PKs2 = Responddata["pku2"]


    Requestdata={
        "su":Sr
    }

    r = requests.get(ENDPOINT+"microservice/clpeks/gPubK",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    PKr1 = Responddata["pku1"]
    PKr2 = Responddata["pku2"]
    # PKr1 = 'X+iRwPV1Um3jtGNXOHo48ua3UneQ2ki2W2auQ0TTjDj2r9bbfZ5wb/bKXY7RvHCByt24KKBvLajEvI944CidrZH67F0XyReM1Ceq9wUKLSlxW3mpnnhGgkplvCFInj4fDgysRPgSnpWoa9XLOkBnwmdB9fYP2Kke5hvSdhkKMWk='
    # PKr2 = 'fPRk0Vabm5hOJb1vHLN/ICbOF5Am22ZHIoamfrkoCzWkfohGYTVJjuIFbKWTxd0Zghc2HL9r7gM8B0MlL71XD2F+xerDYDdDBOrKfx+gujwIjaK9FsPaXBMXWLAP//m3/H//PcPrOGWIqlBAdnRlE8Wwis4tDoQakLwxJ6lXr3I='


    PKs1='CaUSwNaD+tEKUarnP7AurRP38lsUgWenjYQI/yOeb6tlFbrVYgIp1GuqkaXrnE3thQZbyDq/Rzrl8Z1g5oTa8JEJp47sxbX6pwvJkZVKzjLRKeX5zuLRvzq9uYlRLbfIQLbGzcpEj2niA/AUe6jNrfdkQNox+2gkWgysRYQaEd4='
    PKs2='qZGqHv1ArMvxcARuvwYC6wgDAMTbi/0RLPz3OBqz1iEe8B+Q6v+OsHO6ygse0d9A+rLctcOrF3jf7Zen/gYjEJUQQu4ykCyQD+vRGCy3YsYsLtB90lqKl7Hl4fET/6XaWqvyFy3GT9K3a43kMan0/QXoO5Cb5zRZ5wj7COZMSDU='

    Requestdata={
        "pkr1":PKs1,
        "pkr2":PKs2
    } 
    r = requests.get(ENDPOINT+"microservice/clpeks/pairingcheck",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)
    if Responddata['checked']:
        print("------------------------------------")
        print(Responddata['description'])
    else:
        print("--------------------FAILED--------------------")

    Requestdata={
        "pkr1":PKr1,
        "pkr2":PKr2
    } 
    r = requests.get(ENDPOINT+"microservice/clpeks/pairingcheck",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)
    if Responddata['checked']:
        print("------------------------------------")
        print(Responddata['description'])
    else:
        print("--------------------FAILED--------------------")

    # word = "wordto_encrption"
    
    # print(Qr,"-----qr--")
    # print(Qs,"~~~~~qs~~~~~")
    # Qs = 'M8jzyu99qrmHuMf9w/8V2wLCk2qM1JA9/4tAdL4ZV3dM4f4KjoM8yYYX9/CGFwFuoCbaquoWDIX8nMXufQqWTm5efokJ/F9L3Ooru+nKpd7s8pcyoJMSQ5aTav2/qHhDaP+sH/hYavNueN3vo9d2fS0/zt5QHawEgI17WdIvu3w='
    # Qr = 'o2z1cRNLT6CL9O3hAcybJXIsqVkyOGfNWv5WSujorAHWw3xg894FgwzbM1DT6G1e6rnt9HbqP4qKNgoiyqr7qBR11tUBxbvUvcF0Z4QKEEYNi+eVyhuy7nT/e/qtn2MqlO/bj4A6ho0SQHJNXmGvFtY3nFeXHbXpehwDjFMDeks='
    # print(Qr,'after check qr ')
    # print(Qs,'the check --------qs------2')


    print("word s --- ",words)
    Requestdata={
    "words": words,
    "pkr2": PKr2,
    "qs": Qs,
    "qr": Qr,
    "pks2": PKs2
    }
    r = requests.get(ENDPOINT+"microservice/clpeks/encript",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    encypteWords = Responddata
    # SKr2='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYUPkRhgB2L5T1cVRSYectveIdIwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
    Requestdata={
    "skr2": SKr2,
    "pks1": PKs1
    }

    
    print("----------------------\n",PKr2,"\n----------------------\n")
    r = requests.get(ENDPOINT+"microservice/clpeks/trapdoor/"+wordchecking,data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    T1 = Responddata["t1"]
    T2byte = Responddata["t2byte"]
    T3byte = Responddata["t3byte"]

    generted = [{'requiredTime': 128, 'ui': 'NGiMjBkL4peNPEsjFgA3oM/QW6ZI7s4OaCbTjrlncA2itDoeY5OLG3UDeC0iJkfqyWYFb94sT9y0kFDTyZvj/h/UErXNrxV9Roe1OaCMJW2cYuu6Eu5c40NNXuLP5EqoQ8DyeKLR+nW0fEPtpobAffxW+EbgY3NErPjq9dC4smU=', 'vi': 64527255189472499965968404597739980293507476760330075226685230302608155421463390134230116323321772752736984701575034742261645765856413716106842215271655153022526895892807088522857575661516616567651839699262000581385195735722921431663937840726847718667398239613157949281986098216750738129671368449193654483697}, {'requiredTime': 88, 'ui': 'gSdVmarkvfhCZOr9caFqGGuFQz1HeTcDyZ4FqQEt7AtDxQSb/Lr6GS/CErFmV+x05B0CxfMVGLRsUlPif3Be61gbl1RUCTVFYWzVCsAtw57n/DJ+MeAjG0+nqUEJ5Xeck5AgQkVC4/k8NbriY+gnGlZWHvDxgsdUxQU/EVyHywg=', 'vi': -63571629231987874470466124814514046684060288241417431570656665294099944473652041255494096063478701789097847087512582446993477336603516507155721039992771998327836573447804014881920888523981459259043801454867415437727193095142567589219452115191275594668266839104906745708221739743637074130510139395958349048866}, {'requiredTime': 101, 'ui': 'Ng7q+5HgQxMz09TiEJp+UehM/PUlwTRZdJ5t0PHiQgPUd0fpYFNNZ6JtBsQ+pPg7FOW6tXOLP/yF3C89+Z2n3lgVKgWXszmkB6I1vnaeeMD7F91Z0bKU2rN3xQWoezj7fG6gncLhW/Ls/9RdUhTwH0Tafjq7T/5JwvpT1j7U1rg=', 'vi': 18645651128100001383246338297399255565866003766958857200879330569423955710427331824742134861594163134415316207390529610054915825870079414448459504471134260073755923304490199351905248458842109159080178276638836178185633236370433192186652312450150613882182453159486751464819674410347073715839223472314609125400}]



    # SKs1='S0HQnrzbhr93akaPQF6ldxk+o+k='
    # SKs2='a0dQ/edJ3btzsEPi7+W9UdCqdVemYaZSoavRyJTh0/ETMj6g/ZdpMxivw2WBy7tE0xHBgg/MmWtgtSOzdbChTiTRYsAPa8cQlD4YXiHy8Jbx6co0ZUPmQhd0O8DYPPLFGsiBpM73LfzqTkuQn/VsZsioVZJlKJULScxXrnNDN2E='

    # fromandother = json.loads(generted)
    # fromandother = json.loads(json.dumps(fromandother))
    # print(type(fromandother),"----------",fromandother)
    print(type(encypteWords),"------------",encypteWords)

    Requestdata={
    "t1": T1,
     "encypteWords": generted,
    "t2byte": T2byte,
    "t3byte": T3byte,
    "sks1": SKs1,
    "sks2": SKs2
    }
    print("00000000---------------000000000")
    print(json.dumps(Requestdata))
    print("00000000---------------000000000")
    r = requests.get(ENDPOINT+"microservice/clpeks/test",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)
    
    index = 0;
    for Test in Responddata:
        index += 1
        if Test['test']:
            result+=1
            print("succefully find  at ",index)

# print("seccesful",result)


stop = timeit.default_timer()

print('Time: ', int(stop - start), " seconds ")