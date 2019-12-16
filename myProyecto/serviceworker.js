var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/css/estilos.css',
    'productos/',
    'carro/',
    'quienes/',
    'formulario/',
    'admistracion/',
    'version/',
    '',
    '',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

        
      fetch(event.request)
      .then(function(result){
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
   
    );
});

// inicio de codigos para las notificaciones

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyBgp64lIVoYVqklugo604_DsXfPympYCmM",
  authDomain: "petalos-chaval.firebaseapp.com",
  databaseURL: "https://petalos-chaval.firebaseio.com",
  projectId: "petalos-chaval",
  storageBucket: "petalos-chaval.appspot.com",
  messagingSenderId: "570435480699",
  appId: "1:570435480699:web:c58794f0ac8c316f2bc6de"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload) {

  let title = payload.notification.title;

  let options = {
      body:payload.notification.body,
      icon:payload.notification.icon
  }

  self.registration.showNotification(title, options);

});