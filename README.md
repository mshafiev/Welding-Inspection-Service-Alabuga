### README.md

# Welding Inspection Service

## Описание

Welding Inspection Service — это веб-приложение для детекции сварки, использующее YOLO модель для анализа изображений. Приложение позволяет загружать изображения сварки с камеры или устройства и получать результат детекции.

## Требования

- Python 3.9+
- Docker

## Установка

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/yourusername/welding-inspection-service.git
   cd welding-inspection-service
   ```

2. **Создание и активация виртуального окружения (опционально)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для bash
   ```

3. **Установка зависимостей**

   ```bash
   pip install -r requirements.txt
   ```

## Использование

### Запуск приложения локально

1. **Запуск Flask приложения**

   ```bash
   python app.py
   ```

2. Откройте браузер и перейдите по адресу `http://localhost:5000`

### Запуск с использованием Docker

1. **Сборка Docker-образа**

   ```bash
   docker build -t welding-inspection-app .
   ```

2. **Запуск Docker-контейнера**

   ```bash
   docker run -p 5000:5000 welding-inspection-app
   ```

3. Откройте браузер и перейдите по адресу `http://localhost:5000`

## Структура проекта

```
welding-inspection-service/
│
├── app.py                # Основной файл приложения Flask
├── model.py              # Файл с моделью YOLO
├── Dockerfile            # Dockerfile для создания образа
├── requirements.txt      # Список зависимостей
├── README.md             # Этот файл README
└── templates/
    └── index.html        # HTML-шаблон для интерфейса пользователя
```

## Пример использования

### Основная страница

На основной странице приложения отображается поток с камеры. Пользователь может сделать фото или загрузить его с устройства для анализа.

### Результаты анализа

Результаты анализа отображаются на экране, включая идентификатор и название обнаруженного объекта.

## Разработано

Эта система является экономически выгодной, так как для её работы требуется только камера и планшет. Использование Docker позволяет легко развертывать и масштабировать приложение на любых платформах, минимизируя затраты на инфраструктуру и обслуживание.


### Dockerfile

Убедитесь, что у вас правильный Dockerfile:

```Dockerfile
# Используем базовый образ Python 3.9
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Обновляем pip перед установкой зависимостей
RUN pip install --upgrade pip

# Удаляем все предустановленные пакеты
RUN pip freeze > packages.txt && pip uninstall -r packages.txt -y && rm packages.txt

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Копируем все файлы приложения в контейнер
COPY . .

# Устанавливаем порт, который будет слушать контейнер
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "app.py"]
```
