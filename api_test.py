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

ENDPOINT = CYTOPTO_HEROKU
headers = {
     "Content-Type": "application/json"
}


for i in range(1):
    words = []
    for j in range(10):
        N =random.randint(0,19)
        word = ''.join(random.choices(string.ascii_uppercase +
                                string.digits, k = N))
        words.append(word)
    

    print("words generated: \n",words)
    wordchecking = words[1]
    print("word Searching: \n",wordchecking)
    Requestdata = ""
    r = requests.get(ENDPOINT+"microservice/clpeks/setup",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata['p'])

    p = Responddata['p']
    master_key_lambda = Responddata['master_key_lamda']
    PKc = Responddata["pkc"]

    senderid = "senderid"
    receiverid = "receiverid"
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
    # Qr = Qs
    # Dr = Qs


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
    # Sr = Ss

    # Ss = "JjU1s7gpBDRNm3NBPwIhMsty1NQ="
    # Sr = "EnMlqn7XtZWhk+lyS37THfn4zbI="

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

    PKs1 = Responddata["pku1"]
    PKs2 = Responddata["pku2"]


    Requestdata={
        "su":Sr
    }

    r = requests.get(ENDPOINT+"microservice/clpeks/gPubK",data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    PKr1 = Responddata["pku1"]
    PKr2 = Responddata["pku2"]

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

    Requestdata={
    "skr2": SKr2,
    "pks1": PKs1
    }

    

    r = requests.get(ENDPOINT+"microservice/clpeks/trapdoor/"+wordchecking,data=json.dumps(Requestdata),headers= headers)
    print(r)
    Responddata = r.json()
    print(Responddata)

    T1 = Responddata["t1"]
    T2byte = Responddata["t2byte"]
    T3byte = Responddata["t3byte"]

    generted = '[{"requiredTime":237,"vi":25105370939693355311086473508839741594674419505505693761136158634636568104818745377387657628256752017576323966878821082953252505656176227719231188022989833417619155332616230273710210164312768704720041525408914322423169004196598655776041152702781624203376519964420553367438801980161262789079643785376754001258,"ui":"DDT5QXcOZMFrle+zozCyVl5aykEZUq77LyFaCYSvqVS944yLwMU\/dbQpQ14kQvqESuMrn40CeYH\/otFTgZLNUA+fznMhB6Ajt5\/MR6ruRbykcVxHszfdSPm6MqCLA1esR4ckozwdbW+0EUXp4JB0nZyWUwFYZBxSukaptF\/KcYM="},{"requiredTime":200,"vi":47603230461033300442960445468432958376846642558028130414680421835388979040008498048481070332122171656116034263927118210112326720272343638499918881713946880523649261603963462801854299150713482019310442303522543416139668093555774419578816812904595525681936634084043049030880963983261680209886146434179629565801,"ui":"XLCqu0bvsgOkiIf8JEaLgMlR7hTVjojS7s7jcKDJxzx4aVWtDXDnqH1DrlPMkL6kdYcAEgJx54\/8Jh1ltGjeez8+FOkifWMMHtnxLsxeaOnSAaXCa5Pdaxktdq29FZGc+sD06hMX8bcwl875PQhOQaFk5sHMlF\/d4BqRuxXTS0U="},{"requiredTime":176,"vi":39998473449546785823758448957582903926391909757064592242551704777225645799113180197040993585292942529319035341981106267218046916070173005153007875736929071426284497983557964490439380349107775704210718836021501896221227499328789142512210729495009730853524764396784189102428050939155716399600200581366893829498,"ui":"L1mAgdQbi\/LKHBDVFBoc+RO0MPuIPrv6MlUD8ZucaKVztcm4N8j2AqW\/BCueMGPMAB1KooVzS2\/IMMx2UPyT1k9a32X5A0gXTjXaIFr0O2DS1ajvxSK2L6t3kBkskWYpp6T61JW\/KX1FlMm5FMzEwQ883SnafAHvl6c\/zX+B\/Iw="},{"requiredTime":189,"vi":22141756458340551264429017327177258757501706665666194360181141249316362677572008103985693374576829875961273053766940851638826089976924908076893720851396656568427771543398085816838589470420579380749744806117886287868053046023371489563659573340378415446797512899347366590509049029694863794474662844213518280295,"ui":"ECsOhB0LJIONY8nkHBP9sQawatxzvIVNKp1tF66gPu80z8dsCikC\/yzubzlg94GZNEu23dMbGZUSgIPktsZExEJ5dFM9xYDZ+6d+nwD8dkf2XrQwEx96SfxKeommBl75z2jv+bejXPeg\/A7hznvvF7QsTp1zR2YKG5TAGwoJeoE="}]'




    fromandother = json.loads(generted)
    fromandother = json.loads(json.dumps(fromandother))
    Requestdata={
    "t1": T1,
     "encypteWords": encypteWords,
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