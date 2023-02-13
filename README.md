pip freeze
python -m venv venv => создание виртуального окруженя
source venv/Scripts/activate => активация виртуального окружения
deactivate => деактивация виртуального окруженя
echo 'venv' > .gitignore => добавить в gitignore окружение
pip install + название библиотеки => установка библиотеки
pip freeze > requirements.txt => создание файла
pip uninstall -y -r  requirements.txt => удалить все библиотеки