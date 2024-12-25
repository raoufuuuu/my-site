document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('action-button');
    button.addEventListener('click', () => {
        alert("Thank you for visiting Raouf Site!");
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const galleryButton = document.getElementById('gallery-button');
    galleryButton.addEventListener('click', () => {
        window.location.href = 'gallery.html';
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.getElementById('fullscreen-overlay');
    const overlayImage = overlay.querySelector('img');
    const galleryImages = document.querySelectorAll('.gallery img');

    // عرض الصورة بحجم الشاشة عند النقر عليها
    galleryImages.forEach(image => {
        image.addEventListener('click', () => {
            overlayImage.src = image.src; // نسخ رابط الصورة
            overlay.style.display = 'flex'; // إظهار نافذة العرض
        });
    });

    // إغلاق نافذة العرض عند النقر على الخلفية أو الصورة
    overlay.addEventListener('click', () => {
        overlay.style.display = 'none'; // إخفاء النافذة
        overlayImage.src = ''; // تفريغ الصورة
    });
});

