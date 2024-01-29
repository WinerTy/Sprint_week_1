# REST API
![Изображение](https://sun1-85.userapi.com/h-4yU_2Q3pRdfmsnjYJEYTTC2L3ZV9BGqdz6rw/VQMnoWvzX5k.jpg)


## Описание
На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами.

После преодоления очередного перевала, турист заполняет отчёт в формате PDF и отправляет его на электронную почту федерации. Экспертная группа ФСТР получает эту информацию, верифицирует, а затем вносит её в базу, которая ведётся в Google-таблице.

Весь процесс очень неудобный и долгий и занимает в среднем от 3 до 6 месяцев.
### Задачи 
ФСТР заказала разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

### Работа мобильного приложения

- Внесение информации о новом объекте (перевале) в карточку объекта.
- Редактирование в приложении неотправленных на сервер ФСТР данных об объектах, 
на перевале не всегда работает Интернет.
- Заполнение ФИО и контактных данных (телефон и электронная почта) с последующим 
их автозаполнением при внесении данных о новых объектах.
- Отправка данных на сервер ФСТР.
- Получение уведомления о статусе отправки (успешно/неуспешно).
- Согласие пользователя с политикой обработки персональных данных в случае 
нажатия на кнопку «Отправить» при отправке данных на сервер.

### Данные
Мобильное приложение передает такие данные:
- данные о пользователе: ФИО, телефон и email;
- название перевала и его описание;
- координаты перевала, его высота и сложность восхождение в разное время года;
- несколько фотографий перевала.

## Реализация

### Запрос/ответ
API отвечает и получает JSON как тело запроса
```
{
    "beauty_title": "Tester_beauty_title",
    "title": "Tester_Title",
    "other_titles": "Tester_other_title",
    "connect": "Test_connect",
    "level": {
        "summer": "2B",
        "autumn": "2A",
        "winter": "1A",
        "spring": "3C"
    },
    "user": {
        "fam": "Tester",
        "name": "TesterAPI",
        "otc": "Testers",
        "email": "Tester@emaple.com",
        "phone": 123456789
    },
    "coord": {
        "latitude": 222.0,
        "longitude": 221232.0,
        "height": 222
    },
    "images": [
        {
            "title": "test",
            "image": "test_image.png"
        }
    ]
}
```
#### Результаты JSON 

 - **status** — код HTTP, целое число:
   - 500 — ошибка при выполнении операции;
   - 400 — Bad Request (при нехватке полей);
   - 200 — успех.
 - **message** — строка:
   - Причина ошибки (если она была);
   - Отправлено успешно;
   - Если отправка успешна, дополнительно возвращается id вставленной записи.
 - **id** — идентификатор, который был присвоен объекту при добавлении в базу данных.

**Примеры:**
 - { "status": 500, "message": "Ошибка подключения к базе данных","id": null}
 - { "status": 200, "message": null, "id": 42 }
![Изображения](

## ```Метод GET submitData```
Данный метод, позволяет получать информацию из Базы данных.

Метод GET поддерживает следующее:
**Получение всех записей**
- Данный метод доступен по ссылке api/v1/submitData/
![Изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_GET_all.png)
**Получение записи по ID**
- Данный метод позволяет получить определленую информацию основываясь на ее ID
- Доступен по ссылке api/v1/submitData/**ID**
![Изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_get_id_submitData.png)
**Получение записей по Email**
- Данный метод позволяет получать все объекты от опубликованные от пользователя с Email который указан в поиске
- Доступен по ссылке api/v1/submitData/?user__email=**email**
![Изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_get_email_submitData.png)

## ```Метод POST submitData```
Данный метод вызывается, когда пользователь нажимает на кнопку **Отправить** в мобильном приложении

После нажатия на кнопку на API приходит JSON который был описан выше.
На его основе создается запись в Базе данных.

### ```Метод POST submitData``` имеет несколько статусов:
- **status** 200 означает что запрос был обработан и успешно записан в Базу данных.
![Изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_POST_accepted.png)
- **status** 400 означет, что запрос не был обработан т.к в каком-то из полей была совершена ошибка.
![Изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_POST_deny.png)

### ```Метод PATCH submitData``` 
Данный метод используется для изменения сохраненных объектов
Также имеет несколько статусов:
- **status** 200 означает, что изменения в объекте были успешно применены и сохранены в Базу данных.
![изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_PATCH_accept.png)
- **status** 400 означает, что при изменении объекта произошла ошибка т.к обязательные поля были пустыми, статус объекта был изменен либо изменения были применины к информации о пользователе.
  
**Было пропущено обязательное поле**
![изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_PATCH_missingfield.png)
**Статус был изменен**
![изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_PATCH_changestatus.png)
**Изменение информации о пользователе**
![изображение](https://raw.githubusercontent.com/WinerTy/Sprint_week_1/main/readme_img/method_PATCH_useredit.png)

## Схемы и информацию по запросам к API
Схемы были реализованы с помощью swagger, и доступны по ссылкам:
- **api/v1/docs/**
- **api/v1/redoc/**
