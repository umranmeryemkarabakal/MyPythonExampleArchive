# MyPythonExampleArchive

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
</p>

## Overview

An archive of Python practice sets (PG-A-01 … PG-A-07): language basics, higher-order functions, decorators, iterators and generators, standard-library modules, SQLite, unit tests, Selenium browser tests, JSON/Base64 handling and pandas.

## Proje hakkında

Python çalışma setlerinin arşivi. Her `PG-A-xx` klasörü bir konu grubunu içerir.

## İçerik

- `PG-A-01`: temel yapı, paketler, hata yakalama, yüksek mertebe fonksiyonlar, decorator, iterator, generator, `datetime`, `os`, `re`
- `PG-A-02`: string, veri tipleri, operatörler, döngüler, debug, SQLite (`chinook.db`) ve 12 ödev
- `PG-A-03`: iç içe döngüler, listeler, kümeler, `timeit`
- `PG-A-04`: `unittest` ile test projesi ve Selenium ile web testleri
- `PG-A-05`: Base64, `json` ve `os` modülleri
- `PG-A-06`: çözümlü alıştırmalar
- `PG-A-07`: `random`, lambda, built-in fonksiyonlar, getter/setter, pandas

## Kurulum ve çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Selenium testleri için ChromeDriver'ı `webdriver-manager` otomatik indirir; depodaki eski `chromedriver.exe` kaldırıldı.

## Dosya yapısı

```text
MyPythonExampleArchive/
├── PG-A-01/
│   ├── 00-notes.txt
│   ├── 01-PythonBasics.py
│   ├── 02-pythonBasics.py
│   ├── 03-package_exceptionHandling.py
│   ├── 04-higherOrderFunction.py
│   ├── 05-higherOrderFunction.py
│   ├── 06-decorator.py
│   └── … ve 5 öğe daha
├── PG-A-02/
│   ├── 01-string.py
│   ├── 02-data_types.py
│   ├── 03-operators.py
│   ├── 04-loops.py
│   ├── 05-debug.py
│   ├── 06-database.py
│   ├── 07-database.py
│   └── … ve 13 öğe daha
├── PG-A-03/
│   ├── 01-basics.py
│   ├── 02-mat_libr.py
│   ├── 03-nested_loops.py
│   ├── 04-lists.py
│   ├── 05-character.py
│   ├── 06-list_set.py
│   ├── 07-timeit.py
│   └── 08-set_ex.py
├── PG-A-04/
│   ├── PythonSeleniumProject/  (6 dosya)
│   └── PythonTestingProject/  (3 dosya)
├── PG-A-05/
│   ├── Base64Notes/  (2 dosya)
│   ├── json_module/  (4 dosya)
│   └── os_module/  (3 dosya)
├── PG-A-06/
│   ├── 01-divisor.py
│   ├── 02-average.py
│   ├── 03-search.py
│   ├── 04-factorial.py
│   ├── 05-find_red_region.py
│   ├── 06-plot.py
│   ├── 07-list_set.py
│   └── … ve 7 öğe daha
└── PG-A-07/
    ├── 01-random_randint.py
    ├── 02-lambda.py
    ├── 03-built_in.py
    ├── 04-get_set.py
    ├── 05-pandas.py
    ├── 06-pandas.py
    ├── 07-types.py
    └── … ve 2 öğe daha
```
