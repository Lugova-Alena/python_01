import zipfile
import os

def unzip_file(zip_path, extract_to):
    """
    Разархивирует файлы из указанного zip-архива в заданную директорию.

    :param zip_path: Путь к zip-архиву.
    :param extract_to: Путь к директории, куда нужно извлечь файлы.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Файлы успешно извлечены в {extract_to}")
    except zipfile.BadZipFile:
        print(f"Ошибка: Файл {zip_path} не является zip-архивом или поврежден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    unzip_file("hw (1).zip", "data")