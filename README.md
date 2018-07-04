SIEM project by Ruth Galchuk
============================
Software product that checking monitin of files.
It can read files and folders, and give the following information on each one:
a.	MD5 hash
b.	Is it an executable?
c.	Date changed (readable time)
d.  File size in Mb
e.  Rate

Files
-----
- Check_Monitin.py -
- Client.py -
- Monitin_Dir - directory with 4 files from checking

Instructions
------------
2.	Save all the data in a dictionary called "Results".
3.	Add a "rate" to each scanned file.
4.	Go over the example json response. What does the field "verbose message" do? Is it useful in our project?
5.	Under each detecting software, there are a few sub-fields. What is the field "result"?
6.	What is the field "update" and why is it relevant?
7.	After you've examined the response structuere, your Monitin project should check files upon the VirusTotal database.
8.	Check your connectivity, and try to send a test hash (get a hash of something known, like cmd.exe). Send the hash and print out the whole json you're getting in return.
9.	After testing successfully, add the API requests as part of your code. For every file, in addition to the data that you've printed before (question 1 above), add a "rate" field, based on the VirusTotal response.
The flow is:
a.	Send the hash to the API and save the result.
b.	Translate it to json and read the relevant fields.
c.	Was the hash found in the database? If not, give it a rate of 0.9 (dangerous).
d.	If the hash was found, calculate its danger rate and add it to the Results dictionary.
e.	Print the amount of viruses that have identified the file as malware.

* Make sure you test using single files, so you don't exceed the free limits.


