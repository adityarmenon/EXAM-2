import os
folder = " /home/arm/Downloads"
extensions = (".jpg, .pdf, .png,")

for file in os.listdir(folder):
    if file.lower().endswit(extensions)
    print(file)