document.querySelectorAll('input[name="mood"]').forEach((elem) => {
    elem.addEventListener('change', function(event) {
        // Скрыть все рекомендации
        document.querySelectorAll('.recommendation').forEach((rec) => {
            rec.style.display = 'none';
        });

        // Отобразить соответствующую рекомендацию
        const recommendationDiv = document.getElementById(`recommendation-${event.target.value}`);

        // Проверка наличия элемента рекомендации
        if (recommendationDiv) {
            recommendationDiv.style.display = 'block';

            // Получение данных с сервера
            fetch(`/api/recommendation/?mood=${event.target.value}`)
                .then(response => response.json())
                .then(data => {
                    console.log(data);  // Отладочный вывод
                    recommendationDiv.querySelector('p').textContent = data.recommendation;
                })
                .catch((error) => {
                    console.error('Ошибка:', error);
                });
        } else {
            console.error('Рекомендация не найдена для', event.target.value);
        }
    });
});
