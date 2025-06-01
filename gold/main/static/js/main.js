// Ждём полной загрузки страницы
document.addEventListener('DOMContentLoaded', function() {
    // Находим все элементы карусели
    const indicators = document.querySelectorAll('.indicator');
    const slides = document.querySelectorAll('.carousel-slide img');

    // Добавляем обработчик клика для каждого индикатора
    indicators.forEach(indicator => {
        indicator.addEventListener('click', function() {
            // Получаем номер слайда из data-атрибута
            const index = this.getAttribute('data-index');

            // Удаляем активные классы у всех элементов
            document.querySelector('.indicator.active').classList.remove('active');
            document.querySelector('.carousel-slide img.active').classList.remove('active');

            // Добавляем активные классы выбранным элементам
            this.classList.add('active');
            slides[index].classList.add('active');

        });
    });
});