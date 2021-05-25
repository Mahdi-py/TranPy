from googletrans import Translator as T
import csv
import os
import inspect


class Translator:
    def __init__(self, src, dest, path):
        '''
        :param src: source language such as; 'ar' for arabic, 'fi' for french, 'en' for english
        :param dest: destination language such as; 'ar' for arabic, 'fi' for french, 'en' for english
        :param path: path to which you wish to save csv file for the translation
        '''
        self.src = src
        self.dest = dest
        self.__stack_trace = inspect.stack()
        self.path = self.__getpath(path)
        self.data = None
        self.is_translated = True

    def __getpath(self, path):
        if os.path.isabs(path):
            return "{}/{}_{}.csv".format(path, self.src, self.dest)
        p = path
        csv_path = "{}/{}_{}.csv".format(p, self.src, self.dest)
        current_path = self.__stack_trace[1][1]
        splitter = "\\" if "\\" in current_path else "/"
        split_path = current_path.split(splitter)
        path = "{}/{}".format("/".join(split_path[:-1]), csv_path)
        return path


    def __google(self, text):
        gTran = T()
        result = gTran.translate(text, src=self.src, dest=self.dest).text
        return result

    def __init_csv(self):
        """
        This function will create a csv if there is not one
        :return:
        """
        with open(self.path, mode="w") as csv_file:
            fieldnames = ["text", "translation"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()

    def __load_data(self):
        data = {}
        with open(self.path, mode="r") as csv_file:
            fieldnames = ["text", "translation"]
            reader = csv.DictReader(csv_file, fieldnames=fieldnames)
            for i, row in enumerate(reader):
                if i != 0:
                    data[row["text"]] = row["translation"]
        self.data = data

    def __save_data(self):
        with open(self.path, mode="w") as csv_file:
            fieldnames = ["text", "translation"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for text in self.data:
                translation = self.data[text]
                writer.writerow({'text': text, 'translation': translation})

    def add(self, text, translation):
        '''
        This function will add translation to the csv file
        :param text: text you wish to translate
        :param translation: the translation
        '''
        if not os.path.exists(self.path):
            self.__init_csv()
        self.__load_data()
        self.data[text] = translation
        self.__save_data()

    def translate(self, text):
        '''
        This function will translate the text you entered. It will look for translation in the csv file.
        If there is not any, it will translate it using google apis
        :param text: text you wish to translate
        :return: translated text
        '''
        if not self.is_translated:
            return text
        try:
            translation = self.data[text]
        except:
            translation = self.__google(text)
        return translation
