# corpus-linguistics
Презентация: https://docs.google.com/presentation/d/1gDYAc5G6Hmo9eKNq9K31qgqoiaa7H2PTL5AKbH-JpBk/edit#slide=id.p

Документы хранятся в plain text. Отдельно генерируется файл metainfo.txt с метаинформацией, которая на данный момент состоит только из ссылки на статью вики.
Для удобства документы разделены на подпапки по алфавиту.

metainfo.txt имеет следующий формат:

...

ARTICLE_NAME : <link>

ARTICLE_NAME : <link>

...

## Токенизатор

В качестве токенизаторов были быбраны стандартные токенизаторы nltk(PennTreebank), построенном на регулярных выражениях. Этот токенизатор оставляет знаки препинания в качестве отдельных токенов. Всего в итоге получилось 419086 предложений и примерно 15М слов(подсчитано к прошлому разу). Разметка составлялая отдельно для каждой статьи и структура папок разметок имеет схожий формат с таковым у корпуса: "<Путь до разметки>\<Первая буква статьи>\<Имя статьи>.csv". Каждая запись имеет в файле разметки имеет следующий формат: <Номер токена в тексте статьи>,<Номер предложения>,<Сам токен>,<Позиция токена в тексте>. Ниже представлен пример такой разметки.

Id,sentence,token,pos

...

24,1,Столица,142

25,1,страны,150

26,1,—,157

27,1,Вильнюс,159

28,1,.,166

29,2,Площадь,169

30,2,—,177

31,2,65,179

32,2,300,182

33,2,км²,186

34,2,.,189

...

Пример по одной статье: https://docs.google.com/document/d/1WJHdjS2bVbtd3MRF2YDrVv9I3TdwKa9fg4I7Wqi8Et8/edit?usp=sharing
Скрипт токенизации: https://github.com/Sarkin/corpus-linguistics/blob/master/Tokenizer.ipynb

### Дальнейшие планы
Далее хотелось бы добавить в разметку по крайней мере начальную форму слов и некоторые метки из словаря Зелезняка. Тогда разметка бы выглядела следующим образом:

Id,sentence,token,pos,origin,label
0,0,Литвой,0,Литва,"сущ ж"
