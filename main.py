import requests 
from time import sleep
from bs4 import BeautifulSoup as bs4
from requests.sessions import session
import urllib.parse
s = requests.Session()
res = s.get("https://emailmg.homestead.com/roundcube/")

soup = bs4(res.text,"lxml")

token = soup.find("input", {"name":"_token"})
token=(token.get('value'))

print(token)
data=f"_token={token}&_task=login&_action=login&_timezone=Europe%2FParis&_url=&_user=info0%40audiref.org&_pass=%40Kako1337"
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '140',
'Content-Type': 'application/x-www-form-urlencoded',

'Host': 'emailmg.homestead.com',
'Origin': 'https://emailmg.homestead.com',
'Referer': 'https://emailmg.homestead.com/roundcube/',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
resp = s.post('https://emailmg.homestead.com/roundcube/?_task=login',headers=headers,data=data)
cookie=(res.cookies.get_dict())
sleep(1)
#s.cookies.update(cookie)
res = s.get("https://emailmg.homestead.com/roundcube/?_task=settings&_action=identities")
print((res.cookies.get_dict()))
soup = bs4(res.text,"lxml")
#https://emailmg.homestead.com/roundcube/?_task=settings&_action=edit-identity&_iid=6140857&_framed=1
id = soup.find_all("tr")
print(id)
id=str(id[0].get("id"))
id=(id.split('rcmrow')[1])
res = s.get(f"https://emailmg.homestead.com/roundcube/?_task=settings&_action=edit-identity&_iid={id}&_framed=1")

soup = bs4(res.text,"lxml")

token = soup.find("input", {"name":"_token"})

token=(token.get('value'))
print(token)

data = f"_token={token}&_framed=1&_task=settings&_action=save-identity&_iid={id}&_name=teeeeeeeest&_organization=&_reply-to=&_bcc=&_signature="

headers={
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
"Accept-Encoding": 'gzip, deflate, br',
"Accept-Language": 'en-US,en;q=0.9,fr;q=0.8',
"Cache-Control": 'max-age=0',
"Connection": 'keep-alive',
"Content-Length": '153',
"Content-Type": 'application/x-www-form-urlencoded',
"Host": 'emailmg.homestead.com',
"Origin": 'https://emailmg.homestead.com',
"Referer": f'https://emailmg.homestead.com/roundcube/?_task=settings&_action=edit-identity&_iid={id}&_framed=1',
"sec-ch-ua": '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
"sec-ch-ua-mobile": '?0',
"sec-ch-ua-platform": '"Windows"',
"Sec-Fetch-Dest": 'iframe',
"Sec-Fetch-Mode": 'navigate',
"Sec-Fetch-Site": 'same-origin',
"Sec-Fetch-User": '?1',
"Upgrade-Insecure-Requests": '1',
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

res = s.post("https://emailmg.homestead.com/roundcube/",headers=headers,data=data)

headers={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
'Connection': 'keep-alive',
'Host': 'emailmg.homestead.com',
'Referer': 'https://emailmg.homestead.com/roundcube/?_task=mail&_mbox=INBOX',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

res=s.get("https://emailmg.homestead.com/roundcube/?_task=mail&_mbox=INBOX&_action=compose",headers=headers,allow_redirects=False)



email = ""
email=(urllib.parse.quote(email))
print(res.status_code)
_id=(res.headers['Location'].split("_id=")[1])
message =(urllib.parse.quote("""<p>&nbsp;</p>
<div id="_rc_sig">
<h1>TEST HTML</h1>
</div>"""))
print(_id)


res = s.get(f"https://emailmg.homestead.com/roundcube/{res.headers['Location']}")
print(res.text)

soup = bs4(res.text,"lxml")

token = soup.find("input", {"name":"_token"})

token=(token.get('value'))

print(token)

data=f"_token=DqwYNxkZfT5pviX19zKywSRcT4qMaoNP&_task=mail&_action=send&_id={_id}&_attachments=&_from=6140857&_to=_cc=&_bcc=&_replyto=&_followupto=&_subject=from+script&editorSelector=html&_priority=0&_store_target=INBOX.Sent&_draft_saveid=15&_draft=&_is_html=1&_framed=1&_message={message}"

