import os
import json

def netscapeToJson(filename):
    x="Cookies//"+filename
    myfile = open(x, "r")
    cookie = []
    myline = myfile.readline()
    # print(filename)
    while myline:
        key = {}
        x = myline.split()
        key['domain'] = x[0]
        key['httpOnly'] = x[1] == "TRUE"
        key['path'] = x[2]
        key['secure'] = x[3] == "TRUE"
        key['expirationDate'] = int(x[4])
        key['name'] = x[5]
        key['value'] = x[6]      
        cookie.append(key)
        myline = myfile.readline()
    myfile.close()
    filepath = path + filename
    file1 = open(filepath, 'w')
    file1.writelines(str(json.dumps(cookie, indent=2)))
    file1.close()

if __name__=="__main__":
    
    path = 'cookies_json//'    
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)
    
    # Get the list of all files and directories
    pathc = "Cookies"
    dir_list = os.listdir(pathc)

    print("TASK STARTED...")

    for h in dir_list:
        netscapeToJson(h)

    print("TASK COMPLETED...")
