const V="yokdil-v1";const FILES=["./","./index.html","./manifest.webmanifest","./icon-180.png","./icon-192.png","./icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==V).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{const r=e.request;if(r.method!=="GET")return;
 e.respondWith(caches.open(V).then(async c=>{const hit=await c.match(r,{ignoreSearch:true})||(r.mode==="navigate"?await c.match("./index.html"):null);
  const net=fetch(r).then(res=>{if(res&&res.ok&&new URL(r.url).origin===location.origin)c.put(r,res.clone());return res}).catch(()=>null);
  return hit||net.then(x=>x||new Response("Çevrimdışı",{status:503}))}))});
