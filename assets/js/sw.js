const CACHE_NAME = 'library-cache-v1';
const OFFLINE_URL = '/offline.html';
const OFFLINE_IMAGE = '/assets/img/no-internet.gif';

const FILES_TO_CACHE = [
  '/',
  OFFLINE_URL,
  OFFLINE_IMAGE,
  '/assets/css/styles.css', // if needed
  '/assets/js/main.js'      // if needed
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(FILES_TO_CACHE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.map(key => {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request).catch(() => {
      if (event.request.destination === 'image') {
        return caches.match(OFFLINE_IMAGE);
      } else if (event.request.destination === 'document') {
        return caches.match(OFFLINE_URL);
      }
    })
  );
});
