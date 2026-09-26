document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
        var track = carousel.querySelector('[data-carousel-track]');
        var slides = Array.prototype.slice.call(track.children);
        var prevBtn = carousel.querySelector('[data-carousel-prev]');
        var nextBtn = carousel.querySelector('[data-carousel-next]');
        var index = 0;

        function update() {
            track.style.transform = 'translateX(-' + (index * 100) + '%)';
        }

        if (slides.length <= 1) {
            if (prevBtn) prevBtn.style.display = 'none';
            if (nextBtn) nextBtn.style.display = 'none';
            return;
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', function () {
                index = (index - 1 + slides.length) % slides.length;
                update();
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', function () {
                index = (index + 1) % slides.length;
                update();
            });
        }

        update();
    });
});