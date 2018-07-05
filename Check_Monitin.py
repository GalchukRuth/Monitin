import hashlib
import os
import requests
import time

URL = 'https://www.virustotal.com/vtapi/v2/file/report'
API_KEY = '471a3e27495d9d7af52c760de32ff44242d027a55ce55990ce910db00fcec3c6'

# Getting file content
def fileContent(file_path):
    with open(file_path, 'rb')as f:
        content = f.read()
    return content

# Calculate file hash MD5
def file2Hash(content):
    h = hashlib.md5()
    h.update(content)
    return h.hexdigest()

# Checking file for executable extension (exe, dll, sys, SYS) or content (MZ)
def isExecutable(content, file_path):
    str_mz = 'MZ'
    str_exe = '.exe'
    str_sys = '.sys'
    str_SYS = '.SYS'
    str_dll = '.dll'
    if content.find(str_mz) == 0:
        if file_path.find(str_exe) > -1:
            status = 'mz exe'
        elif file_path.find(str_dll) > -1:
            status = 'mz dll'
        elif file_path.find(str_sys) > -1:
            status = 'mz sys'
        elif file_path.find(str_SYS) > -1:
            status = 'mz SYS'
        else:
            status = 'mz without exe'
    else:
        status = 'no mz'
    return status

# Getting change time for file
def getTime(file_path):
    file_time = os.path.getctime(file_path)
    return time.strftime("%d %b %Y %H:%M:%S", time.gmtime(file_time))

# Calculating rate by hash from VirusTotal site
def getRateFromVirusTotal(hash):
    response = requests.get(URL, params={'apikey':API_KEY,'resource':hash})
    data = response.json()
    if data['verbose_msg'] == 'Scan finished, information embedded':
        pos = data['positives']
        total = data['total']
        rate = float(pos) / float(total)
    else:
        #for new file not checking in VirusTotal
        rate = 0.9
    return rate

# Calculating monitin from single file -> to dictionary ---> not used
def singleFile2Dic(file_path):
    dic = {}
    f_size = float(os.path.getsize (file_path)) / 1024
    content = fileContent(file_path)
    f_hash = file2Hash(content)
    f_exec = isExecutable(content, file_path)
    f_time = getTime(file_path)
    f_rate = getRateFromVirusTotal(f_hash)
    dic.update({'md5': f_hash, 'is_exec': f_exec, 'time': f_time, 'rate': f_rate, 'size': f_size})
    return dic

# Calculating monitin from single file -> to list
def singleFile2List(file_path):
    lst = []
    content = fileContent(file_path)
    f_hash = file2Hash(content)
    lst.append(float(os.path.getsize (file_path)) / 1024)
    lst.append(isExecutable(content, file_path))
    lst.append(getTime(file_path))
    lst.append(getRateFromVirusTotal(f_hash))
    return lst

# Calculating monitin for all files under a folder
def directory(dir_path):
    dic = {}
    for i in os.listdir(dir_path):
        full_path = dir_path + '\\' + i
        if os.path.isfile(full_path):
            dic[i] = singleFile2List(full_path)
    return sortDicByRate(dic)

# Sorting by rate
def sortDicByRate(dic):
    sort_lst = sorted(dic.iteritems(), key=lambda v: v[1][3], reverse=True)
    return sort_lst