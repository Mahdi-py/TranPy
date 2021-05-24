# TranPy

TranPy is a simple yet powerful translation python library. It can be used in any project. Basically it will allow you to make customized translations for your application
without having to handle everything. TranPy will allow you to save your customized translations in csv file and translate anything you want based on your translations. In addition 
to that you don't have any matches. TranPy will use google api to translate your text. 
<br> developed by Mahdi Saleh !

## Example of how to use
### adding new translation
```python
from TranPy.Translate import Translation
t = Translation(src="ar",dest="en", path="Translation")
t.add("ادخل اسم المستخدم", "Enter username")
```
<strong>src: </strong> source language such as; 'ar' for arabic, 'fi' for french, 'en' for english <br>
<strong>dest: </strong> destination language such as; 'ar' for arabic, 'fi' for french, 'en' for english <br>
<strong>path: </strong> path to which you wish to save csv file for the translation <br>
the csv file will be stored under the name src_dest.csv. For example in the above code the translations will be stored in the following path: <strong>Translation/ar_en.csv</strong>
### translate
```python
translation = t.translate("ادخل اسم المستخدم")
```
Note that if you have not added the translation for a specific statement, it will use google api to translate the statement 

## Dependencies 
* Python 3
* googletrans==3.1.0a0
* Other dependencies in requirements.txt

## Use with other application
Soon will add a tutorial for how to use it with jinja
## Installation 
soon  
