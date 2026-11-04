const V="yokdil-v3";const FILES=["./","./index.html","./manifest.webmanifest","./icon-180.png","./icon-192.png","./icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(FILES.map(f=>new Request(f,{cache:"reload"})))).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
// Sayfa: önce internet (en yeni sürüm), internet yoksa ya da 5 sn içinde gelmezse kayıtlı sürüm.
self.addEventListener("fetch",e=>{const r=e.request;if(r.method!=="GET"||new URL(r.url).origin!==location.origin)return;
 const isPage=r.mode==="navigate"||/\/(index\.html)?$/.test(new URL(r.url).pathname);
 if(isPage){e.respondWith(caches.open(V).then(async c=>{
   const net=fetch(r,{cache:"no-store"}).then(res=>{if(res&&res.ok){c.put("./index.html",res.clone())}return res});
   const timeout=new Promise(ok=>setTimeout(ok,5000,null));
   try{const res=await Promise.race([net,timeout]);if(res)return res}catch(_){}
   return (await c.match("./index.html"))||net.catch(()=>new Response("Çevrimdışı",{status:503}))}));return}
 e.respondWith(caches.open(V).then(async c=>{const hit=await c.match(r,{ignoreSearch:true});
  const net=fetch(r).then(res=>{if(res&&res.ok)c.put(r,res.clone());return res}).catch(()=>null);
  return hit||net.then(x=>x||new Response("",{status:503}))}))});
