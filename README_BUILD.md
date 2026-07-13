# Создание EXE файла для FNF BotPlay GUI

## Способ 1: Автоматическая сборка (РЕКОМЕНДУЕТСЯ)

### Шаг 1: Установка зависимостей
```bash
pip install -r requirements-build.txt
```

### Шаг 2: Создание EXE файла
```bash
python build_exe.py
```

Эта команда создаст файл `FNF_BotPlay_GUI.exe` в папке `dist/`

---

## Способ 2: Ручная сборка с PyInstaller

### Шаг 1: Установка PyInstaller
```bash
pip install pyinstaller
```

### Шаг 2: Сборка (простая версия)
```bash
pyinstaller --onefile --windowed --name FNF_BotPlay_GUI main.py
```

### Шаг 3: Сборка (полная версия с иконкой и данными)
```bash
pyinstaller --name=FNF_BotPlay_GUI `\
  --onefile `\
  --windowed `\
  --icon=assets/icon.ico `\
  --add-data=config.json:. `\
  --hidden-import=PyQt5 `\
  --hidden-import=loguru `\
  --hidden-import=pydantic `\
  --hidden-import=PIL `\
  --hidden-import=cv2 `\
  --collect-all=PyQt5 `\
  main.py
```

---

## Результат

После успешной сборки:
- **Основной файл**: `dist/FNF_BotPlay_GUI.exe`
- **Можно запустить**: Двойной клик по файлу или `FNF_BotPlay_GUI.exe`
- **Размер**: ~200-300 MB (зависит от версии Python и библиотек)

---

## Оптимизация размера

Для уменьшения размера EXE можно использовать:

```bash
pyinstaller --onefile --windowed --name FNF_BotPlay_GUI `\
  --icon=assets/icon.ico `\
  --add-data=config.json:. `\
  --hidden-import=PyQt5 `\
  --noupx `\
  --upx-dir=. `\
  --strip `\
  main.py
```

---

## Возможные проблемы и решения

### Проблема: "ModuleNotFoundError: No module named 'PyQt5'"
**Решение**: Установите все зависимости:
```bash
pip install -r requirements-build.txt
```

### Проблема: Файл слишком большой
**Решение**: Используйте опцию `--onefile` и удалите ненужные модули

### Проблема: EXE не запускается
**Решение**: 
1. Установите все зависимости
2. Проверьте, что файл `main.py` находится в корне проекта
3. Запустите с консоли для просмотра ошибок: `FNF_BotPlay_GUI.exe`

---

## Распространение

Для распространения EXE файла пользователям:

1. **Один файл**: Скопируйте `dist/FNF_BotPlay_GUI.exe`
2. **С конфигом**: Скопируйте `FNF_BotPlay_GUI.exe` и `config.json` в одну папку
3. **С иконкой**: Создайте ярлык на рабочем столе

---

## Требования для пользователя

- Windows 7 или выше (64-bit рекомендуется)
- ~500 MB свободного места на диске
- Установленный Friday Night Funkin

---

## Создание установщика (опционально)

Для создания установщика используйте NSIS или Inno Setup:

```bash
pip install pyinstaller-nsis
```
