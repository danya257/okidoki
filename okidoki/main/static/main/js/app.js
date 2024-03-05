// Получение модального окна и кнопки для его открытия
var modal = document.getElementById("modal");
var btn = document.getElementById("cart-button");

// Получение элемента для закрытия модального окна
var closeBtn = document.getElementsByClassName("close")[0];

// Открытие модального окна при клике на кнопку
btn.addEventListener("click", function() {
    modal.style.display = "block";
    loadCartContent();
});

// Закрытие модального окна при клике на кнопку "Закрыть"
closeBtn.addEventListener("click", function() {
    modal.style.display = "none";
});

// Закрытие модального окна при клике за пределами окна
window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});

// Загрузка содержимого корзины с помощью Ajax-запроса
function loadCartContent() {
    var request = new XMLHttpRequest();
    request.open('GET', '/cart/detail', true);

    request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
            // Успешно загружено содержимое корзины
            document.getElementById("cart-content").innerHTML = request.responseText;
        } else {
            // Обработка ошибки
            console.error("Ошибка загрузки корзины");
        }
    };

    request.onerror = function() {
        // Обработка ошибки
        console.error("Ошибка загрузки корзины");
    };

    request.send();
}
