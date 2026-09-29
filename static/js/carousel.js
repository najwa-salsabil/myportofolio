document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
        var track = carousel.querySelector('[data-carousel-track]');
        var prevBtn = carousel.querySelector('[data-carousel-prev]');
        var nextBtn = carousel.querySelector('[data-carousel-next]');
        var index = 0;

        function update() {
            var count = track.children.length;
            if (index >= count) index = 0;
            track.style.transform = 'translateX(-' + (index * 100) + '%)';
            var single = count <= 1;
            if (prevBtn) prevBtn.style.display = single ? 'none' : '';
            if (nextBtn) nextBtn.style.display = single ? 'none' : '';
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', function () {
                var count = track.children.length;
                index = (index - 1 + count) % count;
                update();
            });
        }

        if (nextBtn) {
            nextBtn.addEventListener('click', function () {
                index = (index + 1) % track.children.length;
                update();
            });
        }

        carousel.addEventListener('carousel:refresh', function () {
            index = 0;
            update();
        });

        update();
    });
});