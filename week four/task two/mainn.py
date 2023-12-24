import os
import shutil
import datetime


def is_recent_file(file_path):
    file_stats = os.stat(file_path)
    modification_time = datetime.datetime.fromtimestamp(file_stats.st_mtime)
    creation_time = datetime.datetime.fromtimestamp(file_stats.st_ctime)
    current_time = datetime.datetime.now()
    time_difference_modification = current_time - modification_time
    time_difference_creation = current_time - creation_time
    return time_difference_modification < datetime.timedelta(days=1) or time_difference_creation < datetime.timedelta(days=1)


def update_file(file_path):
    with open(file_path, 'a') as f:
        f.write('\nUpdated on ' + str(datetime.datetime.now()))


if not os.path.exists('last_24hours'):
    os.makedirs('last_24hours')


recent_files = [f for f in os.listdir('.') if os.path.isfile(f) and is_recent_file(f)]


for file in recent_files:
    update_file(file)
    shutil.move(file, 'last_24hours/' + file)