from abc import ABC, abstractmethod
import zipfile
import os

class AbstractExtractor(ABC):
    @abstractmethod
    def extract(self, zip_path, extract_to):
        pass

class ZipExtractor(AbstractExtractor):
    def extract(self, zip_path, extract_to):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
                print(f"Файлы успешно извлечены в {extract_to}")
        except zipfile.BadZipFile:
            print(f"Ошибка: Файл {zip_path} не является zip-архивом или поврежден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    extractor = ZipExtractor()
    extractor.extract("hw (1).zip", "data")