import urllib.request
import urllib.parse
import json
#import lxml
#import re
import random

def json_from_url(url):
    #res = urllib.request.urlopen(url)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}) 
    res = urllib.request.urlopen(req)
    
    body = res.read().decode('utf-8')
    return json.loads(body)

def parse_surah(data):

    data=data["data"]
    ayah=data["ayahs"]
    audio=[]
    text=[]
    for x in ayah:
        text.append(x["text"])
        if (x["audio"] is not None):
            audio.append(x["audio"])
        elif (len(x["audioSecondary"]) > 0):
            audio.append(x["audioSecondary"][0])

    return (audio, text);

def parse_tafseer(data):

    data=data["data"][0]
    ayah=data["ayahs"]
    tafseer=[]
    for x in ayah:
        tafseer.append(x["text"])
    return tafseer

def clean_txt(txt):

    # Remove non-breaking spaces
    txt = txt.replace('\xa0', '')

    # Remove leading and trailing newlines/quotes
    return txt.strip()

readers   = ["ar.abdullahbasfar", "ar.abdurrahmaansudais", "ar.abdulsamad" ,"ar.shaatree", "ar.ahmedajamy", "ar.alafasy", "ar.hanirifai", "ar.husary", "ar.husarymujawwad", "ar.hudhaify", "ar.ibrahimakhbar", "ar.mahermuaiqly", "ar.muhammadayyoub", "ar.muhammadjibreel", "ar.saoodshuraym", "ar.parhizgar", "ar.aymanswoaid"]
readers_ar= ["بصفر", "السديس", "عبدالصمد" ,"الشثري", "العجمي", "العفاسي", "الرفاعي", "الحصري", "الحصري2", "الحذيفي", "اكبر", "المعيقيلي", "ايوب", "جبريل", "الشريم", "برهيزكار", "سويد"]
surahs   = ("الفاتحه","البقره","ال عمران","النساء","المائده","الانعام","الاعراف","الانفال","التوبه","يونس","هود","يوسف","الرعد","ابراهيم","الحجر","النحل","الاسراء","الكهف","مريم","طه","الانبياء","الحج","المؤمنون","النور","الفرقان","الشعراء","النمل","القصص","العنكبوت","الروم","لقمان","السجده","الاحزاب","سبا","فاطر","يس","الصافات","ص","الزمر","غافر","فصلت","الشورى","الزخرف","الدخان","الجاثيه","الاحقاف","محمد","الفتح","الحجرات","ق","الذاريات","الطور","النجم","القمر","الرحمن","الواقعه","الحديد","المجادله","الحشر","الممتحنه","الصف","الجمعه","المنافقون","التغابن","الطلاق","التحريم","الملك","القلم","الحاقه","المعارج","نوح","الجن","المزمل","المدثر","القيامه","الانسان","المرسلات","النبا","النازعات","عبس","التكوير","الانفطار","المطففين","الانشقاق","البروج","الطارق","الاعلى","الغاشيه","الفجر","البلد","الشمس","الليل","الضحى","الشرح","التين","العلق","القدر","البينه","الزلزله","العاديات","القارعه","التكاثر","العصر","الهمزه","الفيل","قريش","الماعون","الكوثر","الكافرون","النصر","المسد","الاخلاص","الفلق","الناس")

if  __name__ =='__main__':
     # test code

     try:
        reader_i=readers_ar.index('الشريم')
     except ValueError:
        reader_i=0

     reader  =readers[reader_i]
     print(reader_i)
     print(reader)
     
     reader=random.choice(readers)
     i=random.choice(range(1, 114))
     surah=str(surahs.index(surahs[i])+1)
     t="http://api.alquran.cloud/v1/surah/"+surah+"/"+reader
     print(t)
     #sample = '{"code":200,"status":"OK","data":{"number":114,"name":"\u0633\u0648\u0631\u0629 \u0627\u0644\u0646\u0627\u0633","englishName":"An-Naas","englishNameTranslation":"Mankind","revelationType":"Meccan","numberOfAyahs":6,"ayahs":[{"number":6231,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.alafasy\/6231","text":"\u0628\u0650\u0633\u0652\u0645\u0650 \u0627\u0644\u0644\u0651\u064e\u0647\u0650 \u0627\u0644\u0631\u0651\u064e\u062d\u0652\u0645\u064e\u0670\u0646\u0650 \u0627\u0644\u0631\u0651\u064e\u062d\u0650\u064a\u0645\u0650 \u0642\u064f\u0644\u0652 \u0623\u064e\u0639\u064f\u0648\u0630\u064f \u0628\u0650\u0631\u064e\u0628\u0651\u0650 \u0627\u0644\u0646\u0651\u064e\u0627\u0633\u0650","numberInSurah":1,"juz":30,"manzil":7,"page":604,"ruku":556,"hizbQuarter":240,"sajda":false},{"number":6232,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.alafasy\/6232","text":"\u0645\u064e\u0644\u0650\u0643\u0650 \u0627\u0644\u0646\u0651\u064e\u0627\u0633\u0650","numberInSurah":2,"juz":30,"manzil":7,"page":604,"ruku":556,"hizbQuarter":240,"sajda":false},{"number":6233,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.alafasy\/6233","text":"\u0625\u0650\u0644\u064e\u0670\u0647\u0650 \u0627\u0644\u0646\u0651\u064e\u0627\u0633\u0650","numberInSurah":3,"juz":30,"manzil":7,"page":604,"ruku":556,"hizbQuarter":240,"sajda":false},{"number":6234,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.alafasy\/6234","text":"\u0645\u0650\u0646\u0652 \u0634\u064e\u0631\u0651\u0650 \u0627\u0644\u0652\u0648\u064e\u0633\u0652\u0648\u064e\u0627\u0633\u0650 \u0627\u0644\u0652\u062e\u064e\u0646\u0651\u064e\u0627\u0633\u0650","numberInSurah":4,"juz":30,"manzil":7,"page":604,"ruku":556,"hizbQuarter":240,"sajda":false},{"number":6235,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.alafasy\/6235","text":"\u0627\u0644\u0651\u064e\u0630\u0650\u064a \u064a\u064f\u0648\u064e\u0633\u0652\u0648\u0650\u0633\u064f \u0641\u0650\u064a \u0635\u064f\u062f\u064f\u0648\u0631\u0650 \u0627\u0644\u0646\u0651\u064e\u0627\u0633\u0650","numberInSurah":5,"juz":30,"manzil":7,"page":604,"ruku":556,"hizbQuarter":240,"sajda":false},{"number":6236,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.alafasy\/6236","text":"\u0645\u0650\u0646\u064e \u0627\u0644\u0652\u062c\u0650\u0646\u0651\u064e\u0629\u0650 \u0648\u064e\u0627\u0644\u0646\u0651\u064e\u0627\u0633\u0650","numberInSurah":6,"juz":30,"manzil":7,"page":604,"ruku":556,"hizbQuarter":240,"sajda":false}],"edition":{"identifier":"ar.alafasy","language":"ar","name":"Alafasy","englishName":"Alafasy","format":"audio","type":"versebyverse"}}}'
     sample ='{"code":200,"status":"OK","data":{"number":90,"name":"\u0633\u0648\u0631\u0629 \u0627\u0644\u0628\u0644\u062f","englishName":"Al-Balad","englishNameTranslation":"The City","revelationType":"Meccan","numberOfAyahs":20,"ayahs":[{"number":6024,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6024","text":"\u0628\u0650\u0633\u0652\u0645\u0650 \u0627\u0644\u0644\u0651\u064e\u0647\u0650 \u0627\u0644\u0631\u0651\u064e\u062d\u0652\u0645\u064e\u0670\u0646\u0650 \u0627\u0644\u0631\u0651\u064e\u062d\u0650\u064a\u0645\u0650 \u0644\u064e\u0627 \u0623\u064f\u0642\u0652\u0633\u0650\u0645\u064f \u0628\u0650\u0647\u064e\u0670\u0630\u064e\u0627 \u0627\u0644\u0652\u0628\u064e\u0644\u064e\u062f\u0650","numberInSurah":1,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6025,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6025","text":"\u0648\u064e\u0623\u064e\u0646\u0652\u062a\u064e \u062d\u0650\u0644\u0651\u064c \u0628\u0650\u0647\u064e\u0670\u0630\u064e\u0627 \u0627\u0644\u0652\u0628\u064e\u0644\u064e\u062f\u0650","numberInSurah":2,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6026,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6026","text":"\u0648\u064e\u0648\u064e\u0627\u0644\u0650\u062f\u064d \u0648\u064e\u0645\u064e\u0627 \u0648\u064e\u0644\u064e\u062f\u064e","numberInSurah":3,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6027,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6027","text":"\u0644\u064e\u0642\u064e\u062f\u0652 \u062e\u064e\u0644\u064e\u0642\u0652\u0646\u064e\u0627 \u0627\u0644\u0652\u0625\u0650\u0646\u0652\u0633\u064e\u0627\u0646\u064e \u0641\u0650\u064a \u0643\u064e\u0628\u064e\u062f\u064d","numberInSurah":4,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6028,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6028","text":"\u0623\u064e\u064a\u064e\u062d\u0652\u0633\u064e\u0628\u064f \u0623\u064e\u0646\u0652 \u0644\u064e\u0646\u0652 \u064a\u064e\u0642\u0652\u062f\u0650\u0631\u064e \u0639\u064e\u0644\u064e\u064a\u0652\u0647\u0650 \u0623\u064e\u062d\u064e\u062f\u064c","numberInSurah":5,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6029,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6029","text":"\u064a\u064e\u0642\u064f\u0648\u0644\u064f \u0623\u064e\u0647\u0652\u0644\u064e\u0643\u0652\u062a\u064f \u0645\u064e\u0627\u0644\u064b\u0627 \u0644\u064f\u0628\u064e\u062f\u064b\u0627","numberInSurah":6,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6030,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6030","text":"\u0623\u064e\u064a\u064e\u062d\u0652\u0633\u064e\u0628\u064f \u0623\u064e\u0646\u0652 \u0644\u064e\u0645\u0652 \u064a\u064e\u0631\u064e\u0647\u064f \u0623\u064e\u062d\u064e\u062f\u064c","numberInSurah":7,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6031,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6031","text":"\u0623\u064e\u0644\u064e\u0645\u0652 \u0646\u064e\u062c\u0652\u0639\u064e\u0644\u0652 \u0644\u064e\u0647\u064f \u0639\u064e\u064a\u0652\u0646\u064e\u064a\u0652\u0646\u0650","numberInSurah":8,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6032,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6032","text":"\u0648\u064e\u0644\u0650\u0633\u064e\u0627\u0646\u064b\u0627 \u0648\u064e\u0634\u064e\u0641\u064e\u062a\u064e\u064a\u0652\u0646\u0650","numberInSurah":9,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6033,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6033","text":"\u0648\u064e\u0647\u064e\u062f\u064e\u064a\u0652\u0646\u064e\u0627\u0647\u064f \u0627\u0644\u0646\u0651\u064e\u062c\u0652\u062f\u064e\u064a\u0652\u0646\u0650","numberInSurah":10,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6034,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6034","text":"\u0641\u064e\u0644\u064e\u0627 \u0627\u0642\u0652\u062a\u064e\u062d\u064e\u0645\u064e \u0627\u0644\u0652\u0639\u064e\u0642\u064e\u0628\u064e\u0629\u064e","numberInSurah":11,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6035,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6035","text":"\u0648\u064e\u0645\u064e\u0627 \u0623\u064e\u062f\u0652\u0631\u064e\u0627\u0643\u064e \u0645\u064e\u0627 \u0627\u0644\u0652\u0639\u064e\u0642\u064e\u0628\u064e\u0629\u064f","numberInSurah":12,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6036,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6036","text":"\u0641\u064e\u0643\u0651\u064f \u0631\u064e\u0642\u064e\u0628\u064e\u0629\u064d","numberInSurah":13,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6037,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6037","text":"\u0623\u064e\u0648\u0652 \u0625\u0650\u0637\u0652\u0639\u064e\u0627\u0645\u064c \u0641\u0650\u064a \u064a\u064e\u0648\u0652\u0645\u064d \u0630\u0650\u064a \u0645\u064e\u0633\u0652\u063a\u064e\u0628\u064e\u0629\u064d","numberInSurah":14,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6038,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6038","text":"\u064a\u064e\u062a\u0650\u064a\u0645\u064b\u0627 \u0630\u064e\u0627 \u0645\u064e\u0642\u0652\u0631\u064e\u0628\u064e\u0629\u064d","numberInSurah":15,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6039,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6039","text":"\u0623\u064e\u0648\u0652 \u0645\u0650\u0633\u0652\u0643\u0650\u064a\u0646\u064b\u0627 \u0630\u064e\u0627 \u0645\u064e\u062a\u0652\u0631\u064e\u0628\u064e\u0629\u064d","numberInSurah":16,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6040,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6040","text":"\u062b\u064f\u0645\u0651\u064e \u0643\u064e\u0627\u0646\u064e \u0645\u0650\u0646\u064e \u0627\u0644\u0651\u064e\u0630\u0650\u064a\u0646\u064e \u0622\u0645\u064e\u0646\u064f\u0648\u0627 \u0648\u064e\u062a\u064e\u0648\u064e\u0627\u0635\u064e\u0648\u0652\u0627 \u0628\u0650\u0627\u0644\u0635\u0651\u064e\u0628\u0652\u0631\u0650 \u0648\u064e\u062a\u064e\u0648\u064e\u0627\u0635\u064e\u0648\u0652\u0627 \u0628\u0650\u0627\u0644\u0652\u0645\u064e\u0631\u0652\u062d\u064e\u0645\u064e\u0629\u0650","numberInSurah":17,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6041,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6041","text":"\u0623\u064f\u0648\u0644\u064e\u0670\u0626\u0650\u0643\u064e \u0623\u064e\u0635\u0652\u062d\u064e\u0627\u0628\u064f \u0627\u0644\u0652\u0645\u064e\u064a\u0652\u0645\u064e\u0646\u064e\u0629\u0650","numberInSurah":18,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6042,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6042","text":"\u0648\u064e\u0627\u0644\u0651\u064e\u0630\u0650\u064a\u0646\u064e \u0643\u064e\u0641\u064e\u0631\u064f\u0648\u0627 \u0628\u0650\u0622\u064a\u064e\u0627\u062a\u0650\u0646\u064e\u0627 \u0647\u064f\u0645\u0652 \u0623\u064e\u0635\u0652\u062d\u064e\u0627\u0628\u064f \u0627\u0644\u0652\u0645\u064e\u0634\u0652\u0623\u064e\u0645\u064e\u0629\u0650","numberInSurah":19,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false},{"number":6043,"audio":"http:\/\/cdn.alquran.cloud\/media\/audio\/ayah\/ar.abdulsamad\/6043","text":"\u0639\u064e\u0644\u064e\u064a\u0652\u0647\u0650\u0645\u0652 \u0646\u064e\u0627\u0631\u064c \u0645\u064f\u0624\u0652\u0635\u064e\u062f\u064e\u0629\u064c","numberInSurah":20,"juz":30,"manzil":7,"page":594,"ruku":532,"hizbQuarter":238,"sajda":false}],"edition":{"identifier":"ar.abdulsamad","language":"ar","name":"Abdul Samad","englishName":"Abdul Samad","format":"audio","type":"versebyverse"}}}'
     g = json.loads(sample)
     l=parse_surah(g)
     for x in l:
       print(x)
