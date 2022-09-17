import os
import glob
# Move all anime from the /[AnimeDropbox] to its location and if there is no location make one.
debug = 0
if debug:
    dropbox = "C:/Python/rename_anime/[AnimeDropbox]/"
    to_path = "C:/Python/rename_anime/"
else:
    dropbox = "A:/Anime/[AnimeDropbox]/"
    to_path = "A:/Anime/"
    os.chdir("A:")

def get_list_of_dir():
    list_of_dir = []
    for dir in only_dir_list:
        folder_name = dir.split("\\")[-2]
        list_of_dir.append(folder_name)
    return list_of_dir

only_dir_list = glob.glob(f"{to_path}/*" + os.path.sep)

# Got a list of dir in the to path
dir_list = os.listdir(dropbox)
cur_dir_list = get_list_of_dir()
for video_file in dir_list:
    if ".mkv" not in video_file:
        continue
    Components = video_file.split("] ")[1].split(" - ")
    if len(Components) > 2:
        folder_name = ""
        for i, comp in enumerate(Components):
            if i == len(Components)-2:
                folder_name += comp
                break
            else:
                folder_name += comp + " - "
    else:
        folder_name = Components[0]
    if folder_name not in cur_dir_list:
        print(f"Making new folder: {to_path+folder_name}")
        os.mkdir(to_path+folder_name)
        cur_dir_list.append(folder_name)
    old_name = dropbox+video_file
    new_name = to_path + f"{folder_name}/" + video_file
    print(f"Now moving {old_name} to {new_name}")
    if os.path.exists(new_name):
        os.remove(old_name)
    else:
        os.rename(old_name, new_name)
