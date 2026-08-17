# Парсер PEP с использованием Scrapy

Проект для автоматического сбора информации о Python Enhancement Proposals (PEP) с официального сайта [peps.python.org](https://peps.python.org/).

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd scrapy_parser_pep
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## 🚀 Использование

### Запуск парсера

Для сбора данных о всех PEP:
```bash
scrapy crawl pep
```

### Сохранение результатов

Результаты автоматически сохраняются в CSV файлы в папке `results/`:
- `pep_*.csv` - полный список всех найденных PEP
- `status_summary_*.csv` - сводка по статусам PEP

## 📊 Формат данных

Каждый собранный PEP содержит следующие поля:
```python
{
    'number': '1',              # Номер PEP
    'name': 'Purpose...',       # Название
    'status': 'Accepted'        # Статус
}
```
