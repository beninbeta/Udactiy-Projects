import os

def extract_place(item):
    return item.split("_")[1]
#print(extract_place("2016-11-04_Berlin_09/42/22.jpg"))

def create_dirs(places):
    for place in places:
        os.mkdir(place)
        
def organize_photos(directory):
    os.chdir(directory)
    orginials = os.listdir()
    places = []
    for file_name in orginials:
        place = extract_place(file_name)
        if place not in places:
            places.append(place)
    create_dirs(places)
    for file_name in orginials:
        place = extract_place(file_name)
        os.rename(file_name, os.path.join(place, file_name))

#organize_photos("Photos")
print("Files Moved")

if __name__ == '__main__':
    organize_photos("Photos")