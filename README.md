# DeepFakeProject
Проект для практики МАИ по DeepFake
В этом репозитории находится проект по созданию DeepFake приложения для увековечивания исторических личностей от студентов МАИ.

Принцип работы: по старым фотографиям выбранного деятеля будет создаваться маска для видео с лицом лектора. Таким образом лекцию будет "проводить" сам учёный. Для этого нужно решить задачу по FaceSwap, используя нейронные сети и готовые обученные модели по улучшению качества и колоризации: Gpen, и наложении маски лица: SimSwap.
Для этого было создано 4 команды под руководством выбранного teamlead: съёмочная группа, data engineering, data science и группа продвижения проекта.
В ветке **DE** можно найти папку с GPEN, SimSwap.
## GPEN - готовые обученные модели по улучшению качества и колоризации фотографий 
Примеры работы GPEN на одной студентке:

<img src="https://user-images.githubusercontent.com/92042521/178322303-f7237688-a359-406e-84da-a48318450eeb.jpg" width="800" height="800">

Наш коллаб (рабочий) GPEN <a href="https://colab.research.google.com/drive/1fPUsJCpQipp2Z5B5GbEXqpBGsMp-nvjm?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>.

## SimSwap - программа, позволяющая по фотографии считать маску лица и наложить на видеоролик. 
Приимер:

![image](https://user-images.githubusercontent.com/92042521/178327206-e002ee55-236e-45ef-bc88-c06fd1c6931d.png)



Наш коллаб (рабочий) SimSwap <a href="https://colab.research.google.com/drive/1fPUsJCpQipp2Z5B5GbEXqpBGsMp-nvjm?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>.


## Общий коллаб
Общий коллаб с вышеперчисленными программами, дополненными командой **DS**
<a href="https://colab.research.google.com/drive/1uw7_z9-jqFSFLXDW3cgM7lww_SLrF4l4#scrollTo=u-JxHWn_xmLw&uniqifier=1"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google colab logo"></a>.

**Содержит**:

повышение качества/GPEN 

Сравнение лиц/face_recogniton

Повышение качества/GPEN

Дипфейк/SimSwap

## Dokers
ссылка на dockerhub, содержащей образы SimSwap, Gpen-img, ubunta-img 

https://hub.docker.com/u/21deepfake12
