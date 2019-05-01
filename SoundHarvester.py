import os

print("")

directr = input("Please what is the directory containing the files?: ")

#example directory = "V:\Quotes\Prod\Release"

outfile = open('AutoPlayList.m3u', "w")

content = []

for subdir, dirs, files in os.walk(directr):

    for file in files:
        filepath = subdir + os.sep + file

        if filepath.endswith(".mp3"):
            bline = str(filepath)
            outfile.write(bline + '\n')

outfile.close()

print("")

print("Your output file can be found in this folder, as 'AutoPlayList.m3u.'")

print("")