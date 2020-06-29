#Kakao TTS

카카오 음성 합성 REST API 를 이용한 TTS 만들기 예제 입니다.  
입력한 내용을 파일 이름으로 하는 mp3파일을 생성하고 재생합니다.


[referenced YouTube video](https://www.youtube.com/watch?v=PLAq297bCdw "Youtube")  

#사용법

##1. 코드 수정

*kakao-api-use-TTS.py 를 엽니다. (수정할 부분 : url , KakaoAK)

```python
url = "https://kakao~/synthesize"

headers = {
    "Content-Type": "application/xml",
    "Authorization": "KakaoAK kkkkkkkkkkkkkkkkkkkkkkkkkkkk",
}
```

*[Kakao developers](https://developers.kakao.com/ "kakao") 에 가입.
*내 애플리케이션 > 앱 설정 > 앱 키 에서 REST API 키 를 복사해 KakaoAK 뒤 kkk~를 삭제하고 붙여넣습니다.
    *내 애플리케이션이 없을 경우 애플리케이션 추가를 하면 됩니다.(앱이 없어도 요구하는 정보만 입력하면 생성가능)
    *음성 인식/합성 API를 사용하려면 [내 애플리케이션] > [음성] > [활성화 설정] 항목을 'ON'으로 설정합니다.
*문서 > 음성 > REST API > 음성 합성하기 에서 Sample - Request 의 Post 뒤 "주소" 를 복사해 url에 붙여넣습니다.

##1. 필요한 모듈

* requests
*playsound
    *한글을 입력하려면 파이썬이 설치된 폴더\Lip\site-packages\playsound.py 를 열어 def winCommand 의 encode를 'cp949'로 수정.

```python
    def winCommand(*command):
        buf = c_buffer(255)
        command = ' '.join(command).encode('cp949')
```
