const CACHE_NAME = 'dsa-tracker-v1';

self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(self.clients.claim());
});

// A basic fetch handler is required by Chrome to trigger the PWA Install prompt.
self.addEventListener('fetch', (e) => {
  e.respondWith(
    fetch(e.request).catch(() => new Response('App is running offline.'))
  );
});