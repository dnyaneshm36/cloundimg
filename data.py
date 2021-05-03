import json
import requests

enc1 = '[{"requiredTime":120,"Vi":2541416710790635682204073387370207829447412709159031452285943439880719240150829404327282326934960066283495867756001411346263370079328772677782706652412514023488965058980230926323422928595130185596655998539455632305158593243359186023441926375043564603950936893591187748046989382798157070549448416206514828272,"Ui":"Lx583OUpgMugV1U596Q3OsWxuTZxpfnm9ckTijc1uU+S7UVOyU\\/RguDM3Zy+WqZxfLHKy2Qck3VxfeXtAE7e4G7pPBv0uzunP3RBUmWyp9+WEctBgCwATH+vk9a4Ij37zrVF7wPNezPegNWU7+Rvn\\/zWTH4NTE0LxYaI90FPHuk="},{"requiredTime":103,"Vi":45552133548684576608549065958136737337826300873504533491969188142520363792125389574945046944554622922567007750123147997992500933627841898137366074304791275654844076154373496774862253200366733422481982256018436890516647939576709263876208245616582603249948776122255925229298469170560075819063166344392286819386,"Ui":"XY+0gyueiHksrF9MPCXeMLEjF5JP\\/hZU4HxzOgN1DvY\\/3WCrItwFYFb7hGl\\/XM+W7w6H6aQQ7c8BNOQ5+6sR+2jpySi+rHOANpyLNRrZnZHWLpb3qPKUuMaB5wsyngmx9bKSWV0\\/ONEliITJVyWcuhjKVhVqWlriFoJZIycfwoA="},{"requiredTime":88,"Vi":-69850097898258019188312094656582609478474273363721425756147158137647003241292022252553037029040806973516019396082831585532124903286179224537294218238874737884029232421794789684261555416117061856859216706989199725372697050185464512660950902878043944272055520268302366577917828911991366205070997568763024987580,"Ui":"Na5CyUrjMg7pi+0c9OsnfTW64Hm1UwahvyUX7B3RhH59OeYmgs1zcMmSV48iR6X2P\\/hdNCVDubEFzSOyHuR2Jjwv5MCOH6TV0PoleC+wXistViXZnWFNBOnp84RG08yXh0YNj1TEN+92RXzEdJ6Hg4+sMv5g7qBMuWW5btjzxqU="},{"requiredTime":95,"Vi":-72736635306361007447965681741619479622029411545840261087793755025049403351220672171946798792455446680272101130264455825392785720376272091341080716378684296369417569452761386372546345073572910826300310296114575773072595974621153581268886894683320925789246312184327158267702208622687674572974255875486728689954,"Ui":"HcFCtRTvkmVPy2e3Il6UQN9jnFWumVM3OyOeCrHl6QANnuvWxovdeGVkSGC3\\/q9GyJOLP9vQ4OYQhqILqTQ0KqX0WuKsU1FFXzTcIIIuvUD5LQ5TI5c1Y0e0noMj7DIGvpqb+qlJFFntcQwP9azz3spfcK\\/JB\\/z+fydGrmN7nfE="},{"requiredTime":84,"Vi":29677820317614536141900866476221032301964894903891596781664170939076006770423631147622785074147779573604946500356714724871605737213225782761685724900739952646251893160714055069972062563135030819732440245599902230004112860688779616304948212211724739517753334322053160847427472907704866847140129340924336580334,"Ui":"cLy69gSKJy9k38Sb8AObjIOx\\/cJN\\/uuCw8av6chvYl2h\\/QQJPJT8gdf+VpWop5OoFY1t8fFwJgEzJblAFukRLo3S\\/+rf0nVfytQh6ARRwOdAFmo+x9lr09ydTZgGRHKhzFIJm9it9hGNtDpJCOAbEA33y05\\/h6b3oNSYmFVns6U="},{"requiredTime":90,"Vi":26533083022178069582520342182905541072725417297850767105534870609700668049414766361043447769352606417778729783971223258164297047438987777356192868265629521098223939537541706023660561758685067801302220050777058952203087625923676783024563111194530329363006550659697854842682550829997892867524480393122569555454,"Ui":"h4ytoprDdwW7B2fxEJruw5DIhwXaIT8P73lTnlfZMqo01UEpCtR4UTx7mg8DkFWq83DJdMiRoVVLWGshMAkxXoNYt432XwK1rOgxPCPchFmpdPI1zyUrY5Ck5nXFHOXUhEi1zb63MvW8L0cLRpRZZ4HLmtnieElWmuOmMhmhpmU="},{"requiredTime":83,"Vi":3635190180329201581432824197357864873983153716251931128683749717995315865869707733264148029170983119351900322021950121856555733177012881071014406311575612772586950532893570340677888425077532707140130049829796704435730145736602172435231519045513221275853021505061045201003939074579845757464551846058743963843,"Ui":"nkj6ZPNqnOWNqwkmkUqjIVLQTQ\\/eY6t403xjloLblNpGSjjNEXlabc7pl1MxK3xum1yUvzkHKdFP\\/E2ULPcHoQiboZxxXvWZeL7FQRG1wuONeS7AEaNwR1O+di\\/kMEYBsj6V4x5c88U6d+\\/Ni3F0h1J8OYL90jCDmgaSziV\\/z7Y="},{"requiredTime":81,"Vi":43439323749426874441523183370135283244501411222961637844879846285236888297689325752002860520286231485086498456742760940254803770478430911436757048220736163427883593790112130667520176827683388964111448192014584048607077546549659380565183745881401483692445445722494205054278809098933169786572412639398067312427,"Ui":"EvhOSv50LDJ48qU1ORxhwbPoRgSbYcBDUUE+vrONo0ahchGev4WPGWCwlJNMe1PI5HEB8CnBpEI0SGz8ryAHNSb4YfoOo\\/9jh5oUC3O+eruXQhJtbLTvbg1y3RlGRQPEVKkHrF6S39Lf8oDCOV1Lv2+Ali0YaoSH0snKez\\/AkzA="}]'

# enc2 = [{'requiredTime': 251, 'ui': 'LD41SS1Y6ki4ZsrRSHCyEqs4mpQOA5NY/vnxWb3M4Nq9En735ActIRZza2dM6i41n5bUuqfN1VrHvJR3viv9w4N9fLDBVtmSEnmsbBV4AJuABzXOe0pQmYkS03xpcN8aVWj7CNKdmEHChD1koHHiJqYNFRK3uZ6ZwoBdDmvYEw8=', 'vi': 17899571807498677666802706972146443657416616482090917516083691724938259563099258562279951039054112610900992611659720390789574662167895375242621310045911622559381676413659574528641936292767378611054015241466739263502107987686761716055024354361187330731444337429263651603269646192174335326645313287259278205704}, {'requiredTime': 177, 'ui': 'lSQsxx6ultpQOFHcjNfDSRVKvN94JJq9Emgw9huuTf1/gdGxLj23kYEh6GyvcjJwp/v3pC9WTkpJeDeYaitAAorO1tsHfg9SuBJQaydldzZvIvCtn7SgoFiqZqZ0foSgu4EteVklCzUIFPFypjJg6hSp4jB6sc1jtIQDucsZ518=', 'vi': 84607508331576134314942438643816496154887025618934338120623934353669269939357220191817269195950417753245993019523219127034391666817148899292492870007963539262283784661323508592988276961749416092707434633136191332104759314742241881860520571035634266413127964580225572044386682999723457381995746917477522275580}, {'requiredTime': 218, 'ui': 'ad70ZnhI6gvLVwGtw/F1Z81eHkWifmbjdcQvObXuifXByhTEcKvYnQYz6oXIbQCubccV5hhN3PyQGOqyt8dZpmK4QcYYbnSQbTb9iQaHl/kmGaT5qogg0IH3L5MaICgxASSkch1FENLlSZg5IGZx/QI/GEXVeYrycv1nTKjge7M=', 'vi': 78142473817713237267529845682568130470135779138712941451626644632759095593919692016666448845774900050126359049476899754737596102624013090723810546561732654142379157084527257734080000157186871551525075354409059325122052102227057127347088994686072199135286436856752080417871107569306677580141011856489782708344}, {'requiredTime': 178, 'ui': 'FakzXlKGMysnBTCbzyWDGRxPHKou4szCBZCdhpc4rOYdkhZAMoC+mGmVx/vCM/vH14hDw69n7q18buvMMd82hHy6bGOH+WygOm9JsLSieX96tGqyMFbgUn/XxItZxzFw8wG7VYqFYanO67RYUge6fv5ILoV7C2g1Q3PJf67F+Nk=', 'vi': 16118098829951753277506265763138884465229921970230945664395880617483253511078158790482963937525749724102320255601449453813248546361398037179566709726619823760710178845090807322666917910734215027847092849275171160985668033335314294664077675019790180178102814093319400974388039822551686129501996954563456081014}, {'requiredTime': 230, 'ui': 'lny1Xo2T2ZH7kvqMt4XnnQ/AY7PV1ARtrWW07TC/uys9qVe++Z9ss1VfdcnpaI7H4pRufkA/iB2jeRvnGteopH3+sDjwg5UpxbArzX1AhZl9NHlFxO7h7gXtSvjYa9ZWW5Myn7a5eoDf2WYnrWCtrcDgoipPU3xHVRlcNx9Lypw=', 'vi': 58491948227153317863827796336255567219834592935438991838480517035519406064740897246515682779134450385880123181899570797379902883166537894198950495848310449242652733354777311892290145304685356661610011229747257927040455952393226660011125911152758759352119108007033628487264043165041088601709866432494528478154}, {'requiredTime': 233, 'ui': 'OMcooQ7FLovXbCaBDT36PsIlaEyBJ1cHPl3au0A7UUDJLi8/Qps5qge6wtR5XA+cCom765GCiPVCxBpornVdXEvPP95N8zfuasV3IiYm9XexXJNB3CvLfI1PzqWojiLEol6AkXBulTv0S3YCoFcLzMqbuYb0I3glc380Cp5Abro=', 'vi': 36514426828244391886018321739621118717219102859146119314506479388799492030427842657494457520218305361288662680019407893810671341330812763202236411101382729361204184384001731175296151905679014222906512709073527701724255212434573302866358044573887078605073778229602306249707940188990606859927650677780628177311}, {'requiredTime': 177, 'ui': 'gaFegYs3zt5vJM1dh9RhHxOw3KSYKKgt+xc2N8dngxzCKAnkVNR+mq01nSn8njwiSEaEzEr38+K+fN/cizloQw6iFAR9kcBs3vZiNlFnY/oP9TmKGXSCg0GHFzGBSjPOCqqx1P+hwLKBiaOnU3YMvP5m9RbWH++cTPr3UHshanE=', 'vi': -81692478780300531214444844536845084634254492691696159037113986074511924161542043914815203691595999735322729966185496320406590657516188608192408741873958577986008271150053559704692759143388271609789099425821237451600077501697705906877465676545929058762461077070282311148613277703960841955501045364342651291267}, {'requiredTime': 178, 'ui': 'YDDwyDNNWGo/DXSjAxMYoQzmzFgNw5lP0FixtMx8ERmvsW/0DTwN8XnUlhMDwWYe704/YmBlVNReFrHY3hhUQiIyF3Dk135d85dq/RtD6uvb/pTPaxdT/v6kJ4C2O/GXSRtazCQZwiFlNxEQxHsgnDNixPSya1ZLoX13hOCrFjI=', 'vi': -71329642489080544817299038810737682192462032823334134613980574945821585044628693158311967663657846190360416129437993935937360418825678284655363290607694014104149423600751595548839761073125337619151770532808106809698476969571210425841399746896620194109070458974396505886971684116648530244725904366246556769062}, {'requiredTime': 229, 'ui': 'jwHsf+Fg5qqahsCwkNJAaznWUP4BkNjpFeAs/Civ6uG3IoGj+a/Bm3h17vm7c3IXIsaEVJHm/N8mMbBrSNVt9W6/b8Do5SwHPbrhwX5W549oN+vCW1GtQpslJQZJt5gdcbbScdw+JAyiPgOffBuGHYT7VUhJBGuF3OTyZMweYDs=', 'vi': 43465629876919739571515048999391931849603170668255648898637226189565431964260222993064721421464531352174200776327582399774035801464287896239723562150683037375026369966786241009291896363291518045203745005952468301097679584938027175589673768277772922724601263666978258127737542032536950171043499696933518184804}, {'requiredTime': 183, 'ui': 'MRgfRpQmCUvCFGcAVNQFTKvNCPrPtVmJTTGgTDudhHElWbKL8JeAe1EUTbpAHygMpiku10YZogHmTnS9HDBnxB3Tq1+hvmR1PBOz6rk3XcpD1EpCb0gFElyejVAXAXl/arf6VJOwnE1srYW23hPZ60uazpLDRALogOJnStQBjAI=', 'vi': -77299927500001443444257272934048179717717419473421604054503809454357840940266731588625509723523381368729680229467387883842919130929020415436758648563603835431472255362783947850836123096754963831259909072717104746349018384305992482150548341407721471124506024460687828973423468908908756353809327461328944238586}]
# enc1 = enc1[1:-1]
# print(type(enc1[:-1]))


print(type((json.loads(enc1))))
# print(json.dumps(enc1))

LOCALHOST = "http://localhost:8080/"
CYTOPTO_HEROKU = "https://criptography-dnyanesh.herokuapp.com/"

ENDPOINT = CYTOPTO_HEROKU
headers = {
     "Content-Type": "application/json"
}


if True:


    PKr2 = 'UZchF7H6mefP2qiQgwCUIR3eG8aWF0r+fXUqopYAhB3/lLyuXJzrDwEH7rags9nJDAtn4LMW0ykQskFwtTlPBHxwYeifTcPiu48b/H5jKh6qFOuuv6RPxrpriVeHwnJ7YPerluMdFTWBqGOcwDJwE1QfhKYMHmK04RUUxj57gCU='
    Qs  ='fNMa5U+xNRtVJV5o52Wd+LQXrWdOtCJxIvJsiR2mAHIgW5guM72fLI8NZTa/npI/6vQOHrr4RCa+hV790VgLDXlXT0mwFxCpyHnTtXheLVdnxGyc4xaQ+8mslvn7bfyX56KruHb1qPmeB9DHqIBUPQuSsyuHT6wTeecB45nbmeA='
    Qr  = 'o2z1cRNLT6CL9O3hAcybJXIsqVkyOGfNWv5WSujorAHWw3xg894FgwzbM1DT6G1e6rnt9HbqP4qKNgoiyqr7qBR11tUBxbvUvcF0Z4QKEEYNi+eVyhuy7nT/e/qtn2MqlO/bj4A6ho0SQHJNXmGvFtY3nFeXHbXpehwDjFMDeks='
    PKs2 = 'fiON8IwWTnmZVimRVQmTcrOtyxzU+nHKlyvC5c8ZI4hwxxwOBqxlXRJTUo2AhQEiu6Lqvy5JcXbk2+VKLB9PlZCEjo6/xwoESvybjZI/Oj2+oWhPankGOSdTkEY0xCxAoy+FCWvkV+ppUj3h+eGtSlODDxYPGJzcRX0HQjLKs1E='
    SKr2 = 'X5JaSXZvJbgc95qSGldvuzsq3/s8Z/6B98yk8PmoqN3+XmytgAyKs9IQluUT6WG31NTTI6CRr6U+NNzyAVKrkIbcK7ipj+SWrkWAdsNZLhB/ndTsQUlZ1Ct7vhBPK8smWFdWTnMV+fmoTikb2vQ+5bMyD5sNJUnknpu/iQ9sHLM='
    PKs1 = 'FIXwfT4VOgq8svVgvVlHW1LPUmy2JmGdK7kN1+9bDxFsdscUX4eU8sRNwt9PoEtr+GrDLHGwGDFNrLAv0shx82J8krSU8WCCa7wk7PXl1e7MJFTOoJmg6jlOz/vlOK2T7qfj5naji31+LQcTnJQxLRatF+lefepwO3gIlFBoEp0='
    SKs1 ='TLypQVNo/wFjuFlUW0OSPdSIzHo='
    SKs2 ='Zhxt2zuV5113v0awXGmTRz6xGEH2G9j3plDx7ou8r5EWc73si4abAjqDKYRv9r//+Z5rIJR/CNW37YQGgoYVRFCvKShs95zk9uQFAGLlxrpmg9jcfHUC3RjC2OqGpuV/DloQOT7YhKWe+5kdhT1e2PJ6h+tUJIYBCwusp+47QvA='
    wordchecking = 'help'
    words = ['word', 'help' ,'to' ,'the' ,'hell' ]
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
            print("succefully find  at ",index)