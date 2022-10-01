# mediasoft-httpservice


### Tests and linter status:
[![Actions Status](https://github.com/ajib6ept/mediasoft-httpservice/workflows/check-code/badge.svg)](https://github.com/ajib6ept/mediasoft-httpservice/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/08a9b64cfc25fe0692b1/maintainability)](https://codeclimate.com/github/ajib6ept/mediasoft-httpservice/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/08a9b64cfc25fe0692b1/test_coverage)](https://codeclimate.com/github/ajib6ept/mediasoft-httpservice/test_coverage)
***


Реализовать сервис, который принимает и отвечает на HTTP запросы.

**Функционал**
1. В случае успешной обработки сервис должен отвечать статусом 200, в случае любой ошибки — статус 400.
2. Сохранение всех объектов в базе данных.f
3. Запросы
- GET /city/ — получение всех городов из базы;
- GET /city_id/street/ — получение всех улиц города;(city_id — идентификатор города)
- POST /shop/ — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи.
- GET /shop?street=&city=&open=0/1 — получение списка магазинов;

i. Метод принимает параметры для фильтрации. Параметры не обзательны. В случае отсутствии параметров выводтся все магазины, если хоть один параметр есть, то по нему выполнется фильтраци. <br>
ii. Важно!: в объекте каждого магазина выводится название города и улицы, а не id записей.<br>
iii. Параметр open: 0 - закрыт, 1 - открыт. Данный статус определетс исходя из параметров ¢Время открыти», ¢Время закрытия» и текущего времени сервера.

### Объекты:
**Магазин**:
- Название
- Город
- Улица
- Дом
- Время открытия
- Время закрытия

**Город**:
- Название

**Улица**:
- Название
- Город

!! Замечание: поле id у объектов не указаны, но подразумевается что они есть.<br>
!! Важно: Выстроить связи между таблицами в базе данных.

Инструменты:
- Фреймворк для обработки http запросов Django + Django REST framework
- Реляционная БД (PostgreSQL - предпочтительно, MySQL и тд)
- Запросы в базу данных через ORM (ORM на выбор).
