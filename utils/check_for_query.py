import os
import time
def checkForQueryImage(queryFolder, frequency_s):
    while true:
        if not os.listdir(queryFolder):
            time.sleep(frequency_s)
        else:
            for file in os.listdir(queryFolder):
                if file.endswith(".png") or file.endswith(".jpg"):
                    print("found input at", os.path.join(queryFolder, file))
                    return file