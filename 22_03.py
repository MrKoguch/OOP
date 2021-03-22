from setuptools import setup
# 'Floats.subpack' в packages если есть подпапки (подпакеты)

# package_data={"Floats": ['blob1', 'data/*'] * - помогает вытащить все файлы из папки

# install_requires=['numpy==1.1'] подкачать зависимые библиотеки определенной версии
# или не определенной версии != 1.1, !=1.3 или >=1.1, <2.0, != 1.3

# python_requires="" версия питона

# data_files=[('lib', ['']) создание директориии зa пределами пакета

# zip_safe=False - что перед установкой надо распаковать (data_files дает False)

# Сбор проекта
# python название_файла_с_setup_скриптом sdist архив с проектом сохроняет в папке dist
# python название_файла_с_setup_скриптом bdist_egg data_files=[('lib', ['data/lib/*'])] надо использовать
# полное название заместо *. b - значит динарник
# python название_файла_с_setup_скриптом bdist_wheel, но надо установить через pip библиотеку wheel

setup(name="Floats",
      version="0.1.1",
      packages=["Floats"],
      package_data={"Floats": ['blob1', 'data/*']},
      install_requires=['numpy==1.1'],
      python_requires=">=3.7, <3.9",
      zip_safe=False)
