(function(e){function t(t){for(var r,a,c=t[0],u=t[1],i=t[2],l=0,p=[];l<c.length;l++)a=c[l],Object.prototype.hasOwnProperty.call(o,a)&&o[a]&&p.push(o[a][0]),o[a]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(e[r]=u[r]);d&&d(t);while(p.length)p.shift()();return s.push.apply(s,i||[]),n()}function n(){for(var e,t=0;t<s.length;t++){for(var n=s[t],r=!0,a=1;a<n.length;a++){var c=n[a];0!==o[c]&&(r=!1)}r&&(s.splice(t--,1),e=u(u.s=n[0]))}return e}var r={},a={app:0},o={app:0},s=[];function c(e){return u.p+"js/"+({}[e]||e)+"."+{"chunk-256496bb":"34c42180","chunk-31a07ecc":"8ea8e42d"}[e]+".js"}function u(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,u),n.l=!0,n.exports}u.e=function(e){var t=[],n={"chunk-256496bb":1,"chunk-31a07ecc":1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise((function(t,n){for(var r="css/"+({}[e]||e)+"."+{"chunk-256496bb":"800da18d","chunk-31a07ecc":"3ba004fa"}[e]+".css",o=u.p+r,s=document.getElementsByTagName("link"),c=0;c<s.length;c++){var i=s[c],l=i.getAttribute("data-href")||i.getAttribute("href");if("stylesheet"===i.rel&&(l===r||l===o))return t()}var p=document.getElementsByTagName("style");for(c=0;c<p.length;c++){i=p[c],l=i.getAttribute("data-href");if(l===r||l===o)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var r=t&&t.target&&t.target.src||o,s=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");s.code="CSS_CHUNK_LOAD_FAILED",s.request=r,delete a[e],d.parentNode.removeChild(d),n(s)},d.href=o;var f=document.getElementsByTagName("head")[0];f.appendChild(d)})).then((function(){a[e]=0})));var r=o[e];if(0!==r)if(r)t.push(r[2]);else{var s=new Promise((function(t,n){r=o[e]=[t,n]}));t.push(r[2]=s);var i,l=document.createElement("script");l.charset="utf-8",l.timeout=120,u.nc&&l.setAttribute("nonce",u.nc),l.src=c(e);var p=new Error;i=function(t){l.onerror=l.onload=null,clearTimeout(d);var n=o[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;p.message="Loading chunk "+e+" failed.\n("+r+": "+a+")",p.name="ChunkLoadError",p.type=r,p.request=a,n[1](p)}o[e]=void 0}};var d=setTimeout((function(){i({type:"timeout",target:l})}),12e4);l.onerror=l.onload=i,document.head.appendChild(l)}return Promise.all(t)},u.m=e,u.c=r,u.d=function(e,t,n){u.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},u.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},u.t=function(e,t){if(1&t&&(e=u(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(u.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)u.d(n,r,function(t){return e[t]}.bind(null,r));return n},u.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return u.d(t,"a",t),t},u.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},u.p="/",u.oe=function(e){throw console.error(e),e};var i=window["webpackJsonp"]=window["webpackJsonp"]||[],l=i.push.bind(i);i.push=t,i=i.slice();for(var p=0;p<i.length;p++)t(i[p]);var d=l;s.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},3478:function(e,t,n){"use strict";n("6874")},4951:function(e,t,n){},"56d7":function(e,t,n){"use strict";n.r(t);var r=n("2b0e"),a=function(){var e=this,t=e._self._c;return t("div",{attrs:{id:"app"}},[t("Header"),t("div",{staticClass:"nav-wrapper"},[t("div",{staticClass:"nav"},[t("router-link",{staticClass:"router-link",attrs:{to:"/transfer"}},[e._v("Перевод")]),t("router-link",{staticClass:"router-link",attrs:{to:"/"}},[e._v("Кошелек")]),t("router-link",{staticClass:"router-link",attrs:{to:"/account"}},[e._v("Мой аккаунт")])],1)]),t("router-view",{staticClass:"router-view"})],1)},o=[],s=function(){var e=this,t=e._self._c;return t("header",[this.user?t("div",{key:"userName"},[e._v(" "+e._s(this.user)+" ")]):t("button",{key:"enter",staticClass:"button-enter"},[t("p",{staticClass:"header-button"},[e._v("Войти")])])])},c=[],u=n("f871"),i={mixins:[u["a"]],data(){return{user:"Nikolay"}}},l=i,p=(n("6249"),n("2877")),d=Object(p["a"])(l,s,c,!1,null,"22d4ae10",null),f=d.exports,h={name:"App",components:{Header:f}},m=h,v=(n("f825"),Object(p["a"])(m,a,o,!1,null,null,null)),b=v.exports,y=n("8c4f"),g=function(){var e=this,t=e._self._c;return t("div",[t("Wallet")],1)},C=[],_=function(){var e=this,t=e._self._c;return t("div",{staticClass:"wallet-selector-wrapper"},[t("h3",{staticClass:"block-title"},[e._v("Кошелек")]),t("div",{staticClass:"perevod-wrapper"},[t("div",[t("p",{staticClass:"coin-count"},[e._v(" "+e._s(e.curAURC)+" AURC ")]),t("p",{staticClass:"coin-count"},[e._v(" "+e._s(e.curAUC)+" AUC ")])])])])},w=[],k={mixins:[u["a"]],data(){return{metals:[{name:"Золото",chamName:"Au",index:0},{name:"Серебро",chamName:"Ag",index:1},{name:"Платина",chamName:"Pt",index:2}],curAURC:"",curAUC:""}},async mounted(){try{this.curAURC=await this.sendReq("http://localhost:8000/api/users/get_acc_balance?user_id=1&currency=AURC","GET"),this.curAURC=this.curAURC[0]}catch(e){this.curAURC=0}try{this.curAUC=await this.sendReq("http://localhost:8000/api/users/get_acc_balance?user_id=1&currency=PDC","GET"),this.curAUC=this.curAUC[0]}catch(e){this.curAUC=0}}},A=k,j=(n("3478"),Object(p["a"])(A,_,w,!1,null,"52dd47af",null)),O=j.exports,x={name:"Home",components:{Wallet:O}},U=x,P=Object(p["a"])(U,g,C,!1,null,null,null),T=P.exports;r["a"].use(y["a"]);const E=[{path:"/",name:"Home",component:T},{path:"/transfer",name:"Transfer",component:()=>n.e("chunk-256496bb").then(n.bind(null,"69aa"))},{path:"/account",name:"Account",component:()=>n.e("chunk-31a07ecc").then(n.bind(null,"77be"))}],N=new y["a"]({mode:"history",base:"/",routes:E});var R=N;r["a"].config.productionTip=!1,new r["a"]({router:R,render:e=>e(b)}).$mount("#app")},6249:function(e,t,n){"use strict";n("4951")},6874:function(e,t,n){},"9e5b":function(e,t,n){},f825:function(e,t,n){"use strict";n("9e5b")},f871:function(e,t,n){"use strict";t["a"]={methods:{sendReq:async function(e,t,n=null){try{const a=new Headers;let o;n&&(a.append("Content-Type","application/json"),a.append("Accept","application/json"),a.append("Origin","http://localhost:8000"),o=JSON.stringify(n));const s=await fetch(e,{method:t,headers:a,body:o});if(200===s.status||201===s.status)var r=await s.json();else r="error";return r}catch(a){r="error";return r}}}}}});
//# sourceMappingURL=app.6b078158.js.map