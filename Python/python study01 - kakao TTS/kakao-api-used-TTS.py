#Reference site
#https://www.youtube.com/watch?v=PLAq297bCdw
#http://developers.kakao.com/

import requests
from playsound import playsound
#(ios -> import subprocess )

url = "https://카카오음성합성주소"

headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk",
}

def make_data(x): #def=define =정의하다. 함수를 정의할 때 사용. 
    data = """
    <speak>
    <voice>%s</voice>
    </speak>
    """ % x     # '%s' %x -> s에 x 값을 넣는다는 뜻. x=cmd=input

    return data.encode("utf-8")

cmd = input("입력하세요(Enter): ")
data = make_data(cmd)
r = requests.post(url, data=data, headers=headers)

with open("%s.mp3"% cmd, "wb") as f:
    f.write(r.content)

playsound("%s.mp3" % cmd)
#(ios -> subprocess.run(["afplay", "audio.mp3"]) )