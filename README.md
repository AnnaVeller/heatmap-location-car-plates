# Построение частотной heatmap (тепловой карты) нахождения автомобильных номеров на видео или онлайн камерах
1. [*Кратко*](#1)
2. [*Подробно*](#2)
    1. [Установка под GPU](#2.1)
    2. [Установка под CPU](#2.2)
    3. [Расположение файлов](#2.3)
    4. [Аргументы командной строки](#2.4)
    5. [Примеры работы](#2.5)

------------



## *Кратко* <a name='1'></a>
[Runprocess.Py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/RunProcess.py "Runprocess.Py")
Запускает видео/стрим и создает файл, с координатами найденных номеров

[DrawHeatmap.py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/DrawHeatmap.py "DrawHeatmap.py")
По готовому файлу номеров рисует heatmap

## *Подробно* <a name='2'></a>
### Установка под GPU <a name='2.1'></a>
    pip3 install tensorflow-gpu==1.15.2 
    pip3 install Keras==2.2.*
    pip3 install mrcnn
    pip3 install Nomeroff-net-gpu


### Установка под CPU <a name='2.2'></a>
    pip3 install tensorflow==1.15.2 
    pip3 install Keras==2.2.*
    pip3 install mrcnn
    pip3 install Nomeroff-net

### Расположение файлов <a name='2.3'></a>
В папке [video](https://github.com/AnnaVeller/heatmap-location-car-plates/tree/master/video "video") находятся видео, которые могут быть обработаны. Чтобы их использовать - необходимо указать одно из них в командной строке при запуске скрипта [Runprocess.Py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/RunProcess.py "Runprocess.Py") *(см. раздел аргументы командной строки)*.

В папке [files_heatmap](https://github.com/AnnaVeller/heatmap-location-car-plates/tree/master/files_heatmap "files_heatmap") расположены файлы разрешения*txt*, полученные скриптом [Runprocess.Py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/RunProcess.py "Runprocess.Py"). А также картинки heatmap, полученные скриптом [DrawHeatmap.py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/DrawHeatmap.py "DrawHeatmap.py").

### Аргументы командной строки <a name='2.4'></a>
###### При запуске [Runprocess.Py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/RunProcess.py "Runprocess.Py") можно указать аргументы:

`--video=test.mp4` *Название файла видео из папки video или ссылка на  онлайн камеру. По умолчанию test.mp4*

`--file=test.txt` *Название файла, куда будет записаны координаты номеров (файлы сохраняются в папку files_heatmap). По умолчанию [название__видео].txt*

`--type=v или --type=s`  *Тип того, что было передано в --video. v-видео, s-стрим. По умолчанию видео*

`--gpu=no или --gpu=yes` *Используется ли GPU. По умолчанию не используется*


###### При запуске [DrawHeatmap.py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/DrawHeatmap.py "DrawHeatmap.py"):

`--file=test.txt` *Название файла с координатами номеров. По умолчанию указано test.mp4*

`--k=40` *Характеристика разбивки на зоны. Желательный интервал [20, 100]. При 20 - большее количество зон, при 100 - зон меньше. По умолчанию указано 40*

### Примеры полученных изображений heatmap <a name='2.5'></a>

###### 1) Запустили [Runprocess.Py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/RunProcess.py "Runprocess.Py") таким образом:

`python3 RunProcess.py --video=multy_mini.MOV --file=multy_mini.txt --type=v --gpu=no`

что было бы аналогично из-за дефолтных настроек этому:

`python3 RunProcess.py --video=multy_mini.MOV`


###### 2) Запускаем [DrawHeatmap.py](https://github.com/AnnaVeller/heatmap-location-car-plates/blob/master/DrawHeatmap.py "DrawHeatmap.py"):

`python3 DrawHeatmap.py --file=multy_mini.txt --k=60 --show=True`

После этого мы видим на экране картинку ~~c какой-то хренью~~ c отображением 15 точек для каждого номера и heatmap, а также они сохраняются в [files_heatmap](https://github.com/AnnaVeller/heatmap-location-car-plates/tree/master/files_heatmap "files_heatmap").

###### 3) Затем мы поэкспериментируем с k. 
Поставим k = 60, 40, 30, 20.

##### Наши результаты:

сверху: слева k=60, справа=40,

снизу: слева=30, справа=20

![Heatmap для разных k](https://sun9-51.userapi.com/JtsdlH3HYkWhJnzDsKmFMA688_Gcy1pfNEPZuQ/nW9JRUeg1Eo.jpg "Heatmap для разных k")


![](https://sun9-51.userapi.com/Q_gE-4KeRhZQdYfBE8WdQ243A0Kh4Z2Qg3_UtQ/uy2miVzbd1Q.jpg)
