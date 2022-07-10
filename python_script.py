import configargparse
import os
import shutil

# ПРИМЕР КАК НАДО ЗАПИСАТЬ ЦЕЛИ!!!!!!!!!
# ГДЕ ПИСАТЬ ЦЕЛИ? ГДЕ И ПРИМЕРНО ЧТО ЗАПИСАТЬ НАПИСАНО В БОЛЬШИХ КОММЕНТАРИЯХ (Т.Е. МЕЖДУ КАВЫЧКАМИ)

# os.system('make hello')


"""
Как пользоваться?
На вход: можно указать 3 тэга, для каждого тега нужно указать свои параметры. 
Что и как писать можно и НУЖНО узнать запустив скрипт с ключом -h.
Можно на вход указать файл конфигурации. В нем записать именно то, что хотите передать. Это сделано для того,
чтобы вы не писали гигантскую строку в консоли. Если нужен пример файла, он будет лежать рядом с этим скриптом.
ВНИМАНИЕ! Если вы укажете и файл конфигурации, и параметры, то прога работать будет с параметрами из консоли.
Но лучше так не делать.

На выход: если вы не лохи и мы не лохи, то завершится все успешно и в папочке /home/user/result будут папки с
картинкой/видео, смотря че ввели

Успехов! ДАНЯ!!! Ни нада ниче менять без спроса)))
"""

def create_makedirs(old_directory: str):
    if not os.path.isdir(old_directory):
        os.makedirs(old_directory)


def create_mkdir(old_directory: str):
    if not os.path.isdir(old_directory):
        os.mkdir(old_directory)


def get_filename_without_full_path(path_to_file: str) -> str:
    reversed_path_name = (''.join(reversed(path_to_file)))
    reversed_name_without_path = reversed_path_name.partition('/')[0]
    name_without_path = (''.join(reversed(reversed_name_without_path)))
    return name_without_path
    
#make argparser
configurator = configargparse.ArgParser()
configurator.add_argument('-v', '--video_filepath', required=False, help='path to video')
configurator.add_argument('-i', '--image_filepath', required=False, help='path to image')
configurator.add_argument('--prev', action='store_true', help='previous process')
configurator.add_argument('--proc', action='store_true', help='process')
configurator.add_argument('--post', action='store_true', help='post process')

#make config file
configurator.add_argument(
    '-c', '--config',
    required=False,
    is_config_file=True,
    action='store',
    help='config file path',
)

#check parameters
try:
    args = configurator.parse_known_args()
except:
    print('Exception: Config file not exist')
    exit(-1)

#make dirs for temp and result
temp_path_name = os.path.expanduser('~') + '/data/temp/'
result_path_name = os.path.expanduser('~') + '/data/result/'
flag_tag = False

create_makedirs(temp_path_name)
create_makedirs(result_path_name)

#exicute programm with parameters
if args[0].prev is True:

    print('Start preprocessing...')

    flag_tag = True

    if args[0].image_filepath is None:
        raise Exception("No parametres -i images_file_path.jpg")

    if os.path.isfile(args[0].image_filepath) is False:
        raise Exception("Image file no exist")

    #make dir for image
    temp_image_path_name = temp_path_name + 'image/'
    result_image_path_name = result_path_name + 'image/'

    create_mkdir(temp_image_path_name)
    create_mkdir(result_image_path_name)

    # get file name from input dir

    name_without_path = get_filename_without_full_path(args[0].image_filepath)
    temp_image_path_name += name_without_path
    result_image_path_name += name_without_path
    shutil.copy(args[0].image_filepath, temp_image_path_name)

    """
    Запуск препроцесинга

    1. make цель отвечающая за GPEN

    """
    os.system('make run_prev')

    #go to result
    shutil.copy(temp_image_path_name, result_image_path_name)
    os.remove(temp_image_path_name)

    print('Finish preprocessing...')

if args[0].proc is True:

    print('Start processing...')

    flag_tag = True

    if (args[0].image_filepath is None) or (args[0].video_filepath is None):
        raise Exception("No parametres -i images_file_path.jpg and/or -v video_file_path.mp4")
        
    if os.path.isfile(args[0].image_filepath) is False:
        raise Exception("Image file no exist")

    if os.path.isfile(args[0].video_filepath) is False:
        raise Exception("Video file no exist")
    
    #make dir for image
    temp_video_path_name = temp_path_name + 'video/'
    result_video_path_name = result_path_name + 'video/'

    temp_image_path_name = temp_path_name + 'image/'
    result_image_path_name = result_path_name + 'image/'

    # temp_audio_path_name = temp_path_name + 'audio/'
    # result_audio_path_name = result_path_name + 'audio/'

    create_mkdir(temp_video_path_name)
    create_mkdir(result_video_path_name)
    create_mkdir(temp_image_path_name)
    create_mkdir(result_image_path_name)
    # create_mkdir(temp_audio_path_name)
    # create_mkdir(result_audio_path_name)

    # get file name from input dir
    name_image_without_path = get_filename_without_full_path(args[0].image_filepath)
    temp_image_path_name += name_image_without_path
    result_image_path_name += name_image_without_path
    shutil.copy(args[0].image_filepath, temp_image_path_name)

    name_video_without_path = get_filename_without_full_path(args[0].video_filepath)
    temp_video_path_name += 'video.mp4'
    shutil.copy(args[0].video_filepath, temp_video_path_name) 

    """
    Запуск процессинга

    1. make цель отвечающая за SimSwap
    2. make цель отвечающая за bash-script отделение звука от видео
    3. make цель отвечающая за DeepFake голоса
    4. make цель отвечающая за bash-script соединения звука и видео

    """
    os.system('make run_proc')

    #go to result
    shutil.copy(temp_video_path_name, result_path_name + 'video/result_' + name_video_without_path)
    os.remove(temp_video_path_name)

    shutil.copy(temp_image_path_name, result_image_path_name)
    os.remove(temp_image_path_name)

    print('Finish processing...')
    
if args[0].post is True:

    print('Start post processing...')

    flag_tag = True

    if args[0].video_filepath is None:
        raise Exception("No parametres -v video_file_path.mp4")
    
    if os.path.isfile(args[0].video_filepath) is False:
        raise Exception("Video file no exist")
    
    #make dir for image
    temp_video_path_name = temp_path_name + 'video/'
    result_video_path_name = result_path_name + 'video/'

    # temp_audio_path_name = temp_path_name + 'audio/'
    # result_audio_path_name = result_path_name + 'audio/'

    create_mkdir(temp_video_path_name)
    create_mkdir(result_video_path_name)

    # create_mkdir(temp_audio_path_name)
    # create_mkdir(result_audio_path_name)

    name_video_without_path = get_filename_without_full_path(args[0].video_filepath)
    temp_video_path_name += 'video.mp4'
    shutil.copy(args[0].video_filepath, temp_video_path_name) 
    """
    Запуск постпроцессинга

    0. make цель отвечающая за bash-script отделение звука от видео
    1. make цель отвечающая за разделения видео на кадры
    2. make цель отвечающая за GPEN каждой картинки из папки
    3. make цель отвечающая за bash-script соединения кадров обратно в видео
    4. make цель отвечающая за bash-script соединение звука и видео

    """ 
    os.system('make run_post')

    #go to result
    shutil.copy(temp_video_path_name, result_path_name + 'video/result_' + name_video_without_path)
    os.remove(temp_video_path_name)

    # os.remove(temp_audio_path_name)
    print('Finish post processing...')

if not flag_tag:
    raise Exception("No tags!")

print("Work success!")
