Monitin project by Ruth Galchuk
============================
Software product that checking monitin of files upon the VirusTotal database.
It can read files and folders, and give the following information on each one:
a.	MD5 hash
b.	Is it an executable?
c.	Date changed (readable time)
d.  File size in Mb
e.  Rate

Files
---------
- Check_Monitin.py -
- Client.py -
- My_Dir, New_Dir - directories with 4 files for checking

Instructions
------------
Field "rate"  based on the VirusTotal response. The hash is sent to the API.
If the hash is not found in the database, its value will be equal to 0.9 (dangerous).
If the hash has been found, its danger level is calculated as follows: rate = 'positives' / 'total'