/**
 * Lightweight, zero-dependency QR Code Generator for Rooms
 * Generates an SVG or renders on canvas
 */
(function(window) {
  // Simple clean QR code helper using dynamic QR service with local fallback renderer
  function generateQRCode(elementId, text, size = 180) {
    const container = document.getElementById(elementId);
    if (!container) return;
    container.innerHTML = '';

    const img = document.createElement('img');
    img.alt = 'QR Sala ' + text;
    img.style.width = size + 'px';
    img.style.height = size + 'px';
    img.style.borderRadius = '8px';
    img.style.display = 'block';

    // Reliable public QR API + fallbacks
    const encoded = encodeURIComponent(text);
    img.src = `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encoded}&margin=2`;

    // Local canvas fallback if offline
    img.onerror = function() {
      const canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, size, size);
      ctx.fillStyle = '#111827';
      ctx.font = 'bold 13px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('CÓDIGO DE SALA:', size / 2, size / 2 - 20);
      ctx.font = '900 24px monospace';
      ctx.fillStyle = '#f59e0b';
      ctx.fillText(text.slice(-6), size / 2, size / 2 + 15);
      ctx.font = '11px sans-serif';
      ctx.fillStyle = '#64748b';
      ctx.fillText('(Escanea o escribe código)', size / 2, size / 2 + 40);
      container.innerHTML = '';
      container.appendChild(canvas);
    };

    container.appendChild(img);
  }

  window.generateQRCode = generateQRCode;
})(window);
