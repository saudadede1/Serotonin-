# Çevrimdışı HTML'den telefon uygulaması (PWA) için düz index.html üretir.
import sys
src,out=sys.argv[1],sys.argv[2]
off=open(src,encoding='utf8').read()
head='<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="YÖKDİL"><meta name="apple-mobile-web-app-status-bar-style" content="default">'
off=off.replace('<title>',head+'<title>',1)
reg='<script>if("serviceWorker" in navigator&&location.protocol.startsWith("http")){navigator.serviceWorker.register("sw.js").catch(function(){})}try{navigator.storage&&navigator.storage.persist&&navigator.storage.persist()}catch(e){}</script>'
off=off.replace('</body></html>',reg+'\n</body></html>')
open(out,'w',encoding='utf8').write(off)
