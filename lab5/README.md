## Игра "Угадай по фото"

Вход: файл names.txt содержащий имена для угадывания
(например из http://www.biographyonline.net/people/famous-100.html можно взять имена)

Написать игру "Угадай по фото"

3 уровня сложности:
1) используются имена только 1-10
2) имена 1-50
3) имена 1-100

- из используемых имен случайно выбрать одно
- запустить поиск картинок в Google по выбранному
- получить ~30-50 первых ссылок на найденные по имени изображения
- выбрать случайно картинку и показать ее пользователю для угадывания
  (можно выбрать из выпадающего списка вариантов имен)
- после выбора сказать Правильно или Нет

п.с. сделать серверную часть, т.е. клиент играет в обычном браузере обращаясь к веб-серверу.

п.с. для поиска картинок желательно эмулировать обычный пользовательский запрос к Google
или можно использовать и Google image search API
https://ajax.googleapis.com/ajax/services/search/images? или др. варианты
НО в случае API нужно предусмотреть существующие ограничения по кол-ву запросов
т.е. кешировать информацию на случай исчерпания кол-ва разрешенных (бесплатных)
запросов или другим образом обходить ограничение.
Т.е. игра не должна прерываться после N запросов (ограничение API)

п.с. желательно "сбалансировать" параметры поиска
(например искать только лица, использовать только первые 1-30 найденных и т.п.)
для минимизации того что найденная картинка не соответствует имени

p.s. Отчет и исходный код .zip (или ссылку на github) также высылать на isu.ifmo.ru