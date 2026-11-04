import os,base64,sys
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
src,out,pw=sys.argv[1],sys.argv[2],open(sys.argv[3]).read().strip()
html=open(src,encoding='utf8').read()
salt=base64.b64decode(open(sys.argv[4]).read().strip()) if len(sys.argv)>4 else os.urandom(16);iv=os.urandom(12);IT=310000
key=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=IT).derive(pw.encode())
ct=AESGCM(key).encrypt(iv,html.encode('utf8'),None)
b=lambda x:base64.b64encode(x).decode()
loader='''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><title>YÖKDİL Koçu</title>
<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="YÖKDİL"><meta name="theme-color" content="#2563EB" media="(prefers-color-scheme: light)"><meta name="theme-color" content="#161B26" media="(prefers-color-scheme: dark)">
<style>body{margin:0;font:17px/1.5 -apple-system,system-ui,sans-serif;background:#F7F9FC;color:#18233A;display:grid;place-items:center;min-height:100vh}
.box{box-sizing:border-box;width:min(360px,calc(100vw - 32px));background:#fff;border:1px solid #DCE4E2;border-radius:20px;padding:24px 20px;box-shadow:0 8px 30px rgba(0,0,0,.06)}
h1{font-size:22px;margin:0 0 4px}p{margin:0 0 16px;color:#5D6E75;font-size:15px}input[type=password]{width:100%;box-sizing:border-box;font:inherit;padding:12px 14px;border:1.5px solid #DCE4E2;border-radius:12px}
button{width:100%;margin-top:12px;font-family:inherit;font-weight:600;font-size:17px;padding:13px;border:0;border-radius:12px;background:#2563EB;color:#fff}label{display:flex;gap:8px;align-items:center;margin-top:12px;font-size:15px}#m{color:#C0412A;min-height:1.4em;margin:10px 0 0}
@media(prefers-color-scheme:dark){body{background:#0E1719;color:#E6EEF0}.box{background:#162225;border-color:#24363A}input[type=password]{background:#0E1719;color:#E6EEF0;border-color:#24363A}}</style></head>
<body><form class="box" id="f" autocomplete="on"><h1>YÖKDİL Koçu</h1><p>Bu uygulama kilitli. Şifreni gir.</p>
<input type="text" name="username" value="sero" autocomplete="username" hidden><input type="password" id="pw" autocomplete="current-password" placeholder="Şifre" required>
<label><input type="checkbox" id="rm" checked> Bu telefonda hatırla</label><button id="go">Aç</button><p id="m" role="status"></p><button type="button" id="inst" hidden style="background:#fff;color:#2563EB;border:1.5px solid #2563EB">Ana ekrana uygulama olarak ekle</button></form>
<script type="text/plain" id="d">__CT__</script>
<script>
(function(){var S="__SALT__",I="__IV__",IT=__IT__,K="yokdil_lock_key";
function b2u(s){var b=atob(s),u=new Uint8Array(b.length);for(var i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return u}
if("serviceWorker" in navigator){var hadC=!!navigator.serviceWorker.controller;navigator.serviceWorker.register("sw.js",{updateViaCache:"none"}).then(function(r){r.update()}).catch(function(){});navigator.serviceWorker.addEventListener("controllerchange",function(){if(hadC&&!window.__rl){window.__rl=1;location.reload()}})}
window.addEventListener("beforeinstallprompt",function(e){e.preventDefault();window.__bip=e;var b=document.getElementById("inst");if(b)b.hidden=false});
try{navigator.storage&&navigator.storage.persist&&navigator.storage.persist()}catch(e){}
async function open_(raw){var key=await crypto.subtle.importKey("raw",raw,"AES-GCM",false,["decrypt"]);
 var ct=b2u(document.getElementById("d").textContent.trim());var pt=await crypto.subtle.decrypt({name:"AES-GCM",iv:b2u(I)},key,ct);
 var html=new TextDecoder().decode(pt);document.open();document.write(html);document.close()}
async function derive(pw){var base=await crypto.subtle.importKey("raw",new TextEncoder().encode(pw),"PBKDF2",false,["deriveBits"]);
 return new Uint8Array(await crypto.subtle.deriveBits({name:"PBKDF2",salt:b2u(S),iterations:IT,hash:"SHA-256"},base,256))}
var m=document.getElementById("m");document.getElementById("inst").onclick=function(){var e=window.__bip;if(e){e.prompt();e.userChoice.then(function(){window.__bip=null;document.getElementById("inst").hidden=true})}};
if(!window.crypto||!crypto.subtle){m.textContent="Bu tarayıcı kilidi açamıyor. iPhone’da Safari, Android’de Chrome ile https adresinden aç."}
(async function(){var s=null;try{s=localStorage.getItem(K)}catch(e){}if(s){try{await open_(b2u(s));return}catch(e){try{localStorage.removeItem(K)}catch(_){}}}})();
document.getElementById("f").onsubmit=async function(e){e.preventDefault();m.textContent="Açılıyor…";
 try{var raw=await derive(document.getElementById("pw").value.trim());
  if(document.getElementById("rm").checked){try{localStorage.setItem(K,btoa(String.fromCharCode.apply(null,raw)))}catch(_){}}
  await open_(raw)}catch(err){m.textContent="Şifre yanlış. Tekrar dene."}};
})();</script></body></html>'''
loader=loader.replace('__SALT__',b(salt)).replace('__IV__',b(iv)).replace('__IT__',str(IT)).replace('__CT__',b(ct))
open(out,'w',encoding='utf8').write(loader);print('locked',len(loader)//1024,'KB')
