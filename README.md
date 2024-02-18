# Портфолио
&emsp;Привет!  
&emsp;Меня зовут Константин Григорьев, я развиваюсь в направлении Data Science.  
**Содержание**  
- [Портфолио](#портфолио)
  - [Образование](#образование)
      - [Курсы и тренинги](#курсы-и-тренинги)
      - [Дополнительная информация](#дополнительная-информация)
      - [Резюме](#резюме)
  - [Стек технологий](#стек-технологий)
  - [Выполненные проекты](#выполненные-проекты)
    - [2023: Pet-проект](#2023-pet-проект)
    - [2023: Практическая работа](#2023-практическая-работа)
    - [2023: Курсовая работа](#2023-курсовая-работа)
    - [2022: Ознакомительная практика в ФКУ «ГосТех»](#2022-ознакомительная-практика-в-фку-гостех)
    - [Некоторые проекты, выполненные во время обучения в "Школе 21"](#некоторые-проекты-выполненные-во-время-обучения-в-школе-21)
  - [Дипломы и сертификаты](#дипломы-и-сертификаты)
    - [Сертификат финалиста This is SPARTA data.sprint](#сертификат-финалиста-this-is-sparta-datasprint)
    - [Диплом победителя ДКЭ 2023 по специальности Data Science](#диплом-победителя-дкэ-2023-по-специальности-data-science)
    - [Сертификат прохождения курса Kaggle "Intermediate Machine Learning"](#сертификат-прохождения-курса-kaggle-intermediate-machine-learning)
    - [Сертификат прохождения курса МУИВТЕХ "Основы технологического предпринимательства"](#сертификат-прохождения-курса-муивтех-основы-технологического-предпринимательства)

## Образование
- Обучаюсь на 3-ем курсе бакалавриата МУИВ. Факультет информационных технологий.  
- С октября 2023-го года прохожу обучение в АНО "Школа 21", образовательном проекте от Сбера для разработчиков, бывшем филиале школы 42.  

#### Курсы и тренинги
- 2023 Правительство Москвы, Добровольный Квалификационный Экзамен по Data Science.
- 2022 МФТИ, “Быстрый старт в искусственный интеллект” 45 ак. ч.
- 2022 ЧОУВО “МУ ИМ. С. Ю. ВИТТЕ”, “Основы технологического предпринимательства” 24 ак. ч.

#### Дополнительная информация
- Английский язык, B2

#### Резюме
&emsp;Резюме можно увидеть по <a href="https://docs.google.com/document/d/1dGomIFwV9CrbjELwAdm7i6G82fdemjrJ7BARTZvZYPo/edit?usp=sharing">ссылке</a>.
## Стек технологий 
- **Программирование**: Python, C, SQL;
- **­Базы данных**: PostgreSQL, MySQL, SQLite;
- **­Машинное обучение**: Scikit-learn, Tensorflow, PyTorch, CatBoost, XGBoost;
- **­Визуализация данных**: Matplotlib, Seaborn;
- **­Обработка данных**: NumPy, Pandas;
- **Веб-разработка**: HTML, CSS, Flask;
- **­Операционные системы**: Windows, Linux, MacOS;
- **­А также**: регулярные выражения, Beautiful Soup, Tkinter, Docker, Git, Bash, Excel, SSH, сети.  
## Выполненные проекты
&emsp;В основном выполнял проекты, связанные с анализом данных и классическим машинным обучением.  
___
### 2023: Pet-проект
**“Students Adaptability ML”**  
<a href="https://github.com/Skupydoom/portfolio/tree/main/source/Students_adaptability_ML">Ссылка</a> на исходный код.  

**Задачи:**  
- По имеющимся данным о студентах онлайн-курсов обучить модель предсказания их уровня адаптивности (насколько сложный будет для них курс).

**Используемые технологии:**
- Python.
- Docker.
- Разведывательный анализ данных.
- Библиотеки анализа данных: NumPy, Pandas, Seaborn.
- Библиотеки ML: Scikit-learn, CatBoost.
- Flask, Gunicorn.
- Ансамблевый метод: стекинг моделей машинного обучения.

**Результаты:**  
- Приложение в виде Docker Image, которое принимает запрос с данными о студенте и возвращает его уровень готовности пройти курс.
- Выполнил полный цикл задачи машинного обучения: проанализировал данные, обучил модель и подготовил для запуска в работу готовое приложение.


**Описание:**  
&emsp;В проекте изучается датасет, содержащий персональную информацию об онлайн студентах.  
&emsp;Цель состояла в предсказании их уровня адаптации или, другими словами, вероятность успешного прохождения курса.  
&emsp;В Jupyter ноутбуке данные были разделены на тренировочные и тестовые, был проведён анализ характеристик датасета, обучено и сверено по метрике F1 несколько моделей машинного обучения.  
&emsp;Лучшие из моделей были объединены в одну с помощью стекинга (ансамблевый метод).  
&emsp;Финальная стек-модель сохранена в Docker Image.  
В конце работы получились следующие файлы:
- Jupyter ноутбук "data_analysis.ipynb" с обширным анализом данных;
- Датасет "students_adaptability_level_online_education.csv";
- Файлы с зависимостями: "Pipfile" и "Pipfile.lock";
- Скрипт "train.py", который обучает финальную модель и сохраняет её в бинарный файл;
- Скрипт веб-сервис "predict.py". Может быть запущен с помощью Gunicorn;
- Бинарный файл "model.bin" с важными переменными натренированной модели;
- Скрипт "predict_test.py" для тестирования веб-сервиса.
- Dockerfile для развёртывания веб-сервиса;

___
### 2023: Практическая работа
**“Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов”**  
<a href="https://github.com/Skupydoom/portfolio/tree/main/source/Анализ%20данных%20аэропортов%2C%20визуализация%20и%20применение%20машинного%20обучения%20для%20проверки%20наличия%20регулярных%20рейсов">Ссылка</a> на исходный код и отчёт.  

**Задачи:**  
- Провести полный анализ данных 75000  аэропортов.
- Обучить модель предсказания наличия регулярных рейсов у аэропорта по его характеристикам.

**Используемые технологии:**  
- Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost, Jupyter Notebook, Google Earth Pro.

**Результаты:**  
- Произвёл подробный анализ аэропортов и очистил данные.
- Поставил и проверил несколько гипотез, визуализировал статистические срезы.
- Натренировал несколько моделей машинного обучения и выбрал лучшую: алгоритм случайного леса с ROC AUC = 0.80.

**Описание:**  
&emsp;В проекте исследовался датасет с данными о 75000 аэропортов по всему миру.  
&emsp;Он содержит анализ данных, очистку от цифрового мусора, вывод статистических характеристик и диаграмм, обучение моделей машинного обучения и подбор гиперпараметров.  
&emsp;В приложении Google Earth Pro был импортирован датасет и получено на глобусе мира расположение каждого аэропорта с его описанием.  
&emsp;Также было предложено несколько гипотез о зависимости характеристик и проверено на данных.  
&emsp;После я разделил данные на обучающие и тренировочные, обучил несколько моделей машинного обучения, проверил матрики accuracy, precision, recall и ROC AUC score. Лучшим оказался алгоритм случайного леса. Используя кросс-валидацию данных и отрисовку графиков, я подобрал оптимальные гиперпараметры модели.  
&emsp;После обучения финальной модели сравнил все метрики и сделал вывод о том, что модель случайного леса склонна к переобучению.  
&emsp;Некоторые изображения из отчёта:
<table>
  <tr>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/airports_location.png" alt="Расположение аэропортов" width="500"/></img>
    </td>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/google_earth_pro_all_airports.png" alt="Аэропорты в Google Earth Pro" width="500"/></img>
    </td>
  </tr>
  <tr>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/google_earth_pro_airport_description.png" alt="Описание аэропортов в Google Earth Pro" width="500"/></img>
    </td>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/numeric_data_correlation.png" alt="Матрица корреляции числовых данных" width="500"/></img>
    </td>
  </tr>
  <tr>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/scheduled_service_countries.png" alt="Регулярные рейсы по странам" width="500"/></img>
    </td>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/n_estimators_selection.png" alt="Подбор гиперпараметра n_estimators" width="500"/></img>
    </td>
  </tr>
  <tr>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/metrics_comparison_one.png" alt="Сравнение метрик всех моделей (1)" width="500"/></img>
    </td>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/overfitted_model.png" alt="Переобученная модель" width="500"/></img>
    </td>
  </tr>
  <tr>
    <td>
        <img src="./Images/Анализ данных аэропортов, визуализация и применение машинного обучения для проверки наличия регулярных рейсов/metrics_comparison_two.png" alt="Сравнение метрик всех моделей (2)" width="500"/></img>
    </td>
  </tr>
</table>

___
### 2023: Курсовая работа
**“Интерактивное приложение для доступа к ML-моделям с сервера”**  
<a href="https://github.com/Skupydoom/portfolio/tree/main/source/Интерактивное%20приложение%20для%20доступа%20к%20ML-моделям%20с%20сервера">Ссылка</a> на исходный код.  

**Задачи:**  
- Клиент-серверное приложение с авторизацией.

**Используемые технологии:**  
- Работа с базами данных.
- Система авторизации пользователей.
- Сетевое взаимодействие.
- Python, CustomTkinter, Tkinter, Flask, Requests, Sqlite3.
- SQL.

**Результаты:**  
- Готовое приложение с возможностью авторизации и получения внутренней информации.
- Значительно улучшил навыки разработки бэкенд части приложений на Python.

**Описание:**  
&emsp;Проект представляет собой клиент-серверное приложение. Сервер может быть запущен исполнением скрипта ./server/server.py.  
&emsp;Графический интерфейс запускается скриптом ./client/main.py.  
&emsp;Пользователя встречает следующее окно регистрации:  

<table>
  <tr>
    <td>
        <img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/registration_unfilled.png" alt="Registration unfilled" width="300"/></img>
    </td>
    <td>
        <img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/registration_filled.png" alt="Registration filled" width="300"/></img>
    </td>
  </tr>
</table>

&emsp;После введения данных и нажатия кнопки регистрации происходит передача данных серверу, запись в базу данных пользователей:  
<img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/data_base_view.png" alt="Registration unfilled" width="400"/></img>

&emsp;В случае успешной записи идёт перенаправление на основное окно:  
<table>
  <tr>
    <td>
        <img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/model_selection_window.png" alt="Registration unfilled" width="500"/></img>
    </td>
    <td>
        <img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/models_list_and_description.png" alt="Registration filled" width="500"/></img>
    </td>
  </tr>
</table>

&emsp;Здесь человек может выбрать понравившуюся модель из списка и получить описание.  
&emsp;Также реализован вход по логину и паролю:  
<img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/login_window.png" alt="Registration unfilled" width="300"/></img>

&emsp;Есть кнопка переадресации со страницы логина на страницу регистрации и наоборот.  
&emsp;Тема может быть изменена на тёмную или системную при её выборе из списка:  
<img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/main_window_dark.png" alt="Registration unfilled" width="300"/></img>

&emsp;Клиент и сервер показывают в консоли отладочную информацию при различных действиях пользователей:  
<table>
  <tr>
    <td>
        <img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/app_log.png" alt="Registration unfilled" width="500"/></img>
    </td>
    <td>
        <img src="./Images/Интерактивное приложение для доступа к ML-моделям с сервера/server_log.png" alt="Registration unfilled" width="500"/></img>
    </td>
  </tr>
</table>

___
### 2022: Ознакомительная практика в ФКУ «ГосТех»
**“Разработка сценариев реализации угроз с использованием MITRE ATT&CK на примере цифровой подстанции. Рассмотрение вопросов автоматизации процесса формирования сценариев угроз”**  
&emsp;<a href="https://github.com/Skupydoom/portfolio/tree/main/source/Ознакомительная%20практика%20в%20ФКУ%20«ГосТех»">Ссылка</a> на отчёт.  

**Задачи:**  
- Произвести анализ устройства цифровой подстанции.
- Определить программное обеспечение, которое можно применить при формировании модели угроз для данного объекта и сформулировать принцип автоматизации моделирования.

**Используемые технологии:**   
- MITRE ATT&CK, MITRE Navigator, ADTool, правила CAPA, MITRE CARET, Microsoft threat modeling tool, банк данных угроз информационной безопасности ФСТЭК России.

**Результаты:**  
- Получил практические навыки формирования целей и задач группового проекта.
- Написал подробный отчёт по анализу темы.
- Научился формировать сценарии угроз с помощью современных инструментов.

**Описание:**  
&emsp;Отчёт представляет собой статью с результатами практической работы нашей группы студентов.  
В документе описана гипотетическая ситуация:  
- Есть автоматизированная цифровая подстанция на электростанции. От неё питается центр обработки данных с большим количеством клиентов, в том числе в лице крупных компаний.

&emsp;В отчёте исследуется предположительная схема работы ЦПС, её структура обеспечения надёжности. Далее предполагается, какие объекты могут быть атакованы путём кибератаки на саму подстанцию. После с помощью программного обеспечения MITRE ATT&CK и MITRE Navigator и концепции "Kill chain" описываются возможные сценарии атак злоумышленников.  
&emsp;Во втором разделе приведены сервисы для помощи в автоматизации формирования сценариев угроз.
___
### Некоторые проекты, выполненные во время обучения в "Школе 21"  
- Реализация оригинальной игры "Понг" на языке C.
- Реализация клеточного автомата "Game Of Life" на языке C.
- Реализация Bash утилит Cat и Grep.
- Реализация библиотеки C string.h с дополнительным функционалом.
- Базовое ознакомление с Linux (Ubuntu Server LTS 20.04).
- Настройка сети на виртуальных машинах с Linux и их взаимодействие.
___
## Дипломы и сертификаты
### Сертификат финалиста This is SPARTA data.sprint
<img src="./diplomas_and_certificates/This_is_SPARTA_data_sprint.jpg" alt="Сертификат финалиста This is SPARTA data.sprint" width="700"/></img>

### Диплом победителя ДКЭ 2023 по специальности Data Science
<img src="./diplomas_and_certificates/DKE_2023_Data_Scientist.jpg" alt="Диплом победителя ДКЭ 2023 Data Science" width="700"/></img>

### Сертификат прохождения курса Kaggle "Intermediate Machine Learning"
<img src="./diplomas_and_certificates/Konstantin_Grigorev_Intermediate_Machine_Learning.png" alt="Сертификат Kaggle Intermediate Machine Learning" width="700"/></img>

### Сертификат прохождения курса МУИВТЕХ "Основы технологического предпринимательства"
<img src="./diplomas_and_certificates/MuivTech_business.jpg" alt="Сертификат МУИВТЕХ Основы технологического предпринимательства" width="700"/></img>