# coding:utf-8

import sys
import os
import requests
import json
import urllib

apikey = os.environ.get("DOCOMO_APIKEY")

def dialogue(utt):

    query = {"APIKEY": apikey}
    url = "https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?%s" % (urllib.urlencode(query))
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    timeout = 30

    response = requests.post(
        url,
        headers = headers,
        data = json.dumps({
            "utt": utt,
            "context": "",
            "nickname": u"光",
            "nickname_y": u"ヒカリ",
            "sex": u"女",
            "bloodtype": "B",
            "birthdateY": "1997",
            "birthdateM": "5",
            "birthdateD": "30",
            "age": "16",
            "constellations": u"双子座",
            "place": u"東京",
            "mode": "dialog"
        }),
        timeout = timeout
    )

    res_json = response.json()

    result = json.dumps(response.json(), indent = 4)
    return res_json["utt"]

if __name__ == '__main__':
    print(dialogue(sys.argv[1]))
