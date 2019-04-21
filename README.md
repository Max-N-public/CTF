# Security_IDE
<p>DEVELOPMENT WILL TAKE PART IN 3 PHASES</p>
<table>
	<tr>
		<th>1) Develop as a command line tool</th>
		<th>2) Develop with website interface : LOCALLY ONLY</th>
		<th>3) Implement frontend and backend functionality --> requires splitting up what is made currently into 2 parts</th>
	</tr>
</table>


<p><b>What I think about this more boldly, how about the functionality can be modular and extended to include things for general infosec for pentesting + other things. I can take all the largest developed projects and put them into "A SINGLE SECURITY IDE"</b></p>

The aim of this project is to provide integrated functionality for solving ctf problems with as little heavy lifting as possible. This service should be able to be easily deployed and act as an easy to use, highly avaible tool. Most ctf problems should be able to be templated and just require critical thinking skills also cutting down on the time required to research common loops and syntax for whatever software, after completing a ctf a ctf writeup template generator will help create html templates. Larger technologies will try to be found while smaller scripts and speciality items will be created in house. I forecast this project will take months, if not a full year. My aim is to complete as much functionality before college as possible.

TODO:
	Psuedocode
	cleanup repo


<h1>TECHNOLOGY STACK:</h1>
	Python templating + Django = backend services --> Anything that does work
	HTML/CSS/JS login screen + gdbgui (How to integrate as one?) <--> PHP as backend
		|
		-->I think create a dashboard (How to make unique for each user?) with whatever service is needed and integrate them together
		|
		-->Emulate the vsphere environment or guac format
	Kubernete clusters + docker --> Allows for (do you call them microservices?) --> selection for x86 x64 etc

	Run FTP filezilla service for downloading files / tools / previous challenges

	--> I want a user portal accessible from anywhere
		|
		|
		-->You can access dockers prestaged with different configured OS's
		-->Each OS will have a task selection like Forensics / pwnrev/ etc
			|
			--> They will be loaded with the tools required for each
	--> Where are the files stored --> FTP alongside the client server



<h1>TOPLOGY:</h1>
	~!!!!!!~-->Topology will be filled later after more research is done
		MAIN FOLDER
		|
		-->Writeup generation template
		|	|
		|	-->Is there a way for github api to sync changes to exteneral ftp server
		|
		-->CTF Solver
		|	|
		|	-->main.py (or do you call this init?) <-- Holds the switch cases and user interaction through console (add gui later?)
		|	|
		|	-->RUNME.exe that imports all required resources and updates
		|	|
		|	-->Dependacy programs
		|	|
		|	-->Pwn
		|	|
		|	-->Rev
		|	|
		|	-->Forensics
		|	|
		|	-->Crypto
		|	|
		|	-->Web
		|	|
		|	-->Misc / Linux / unusual categories / pentest
		|	|
		|	-->General tools like convert asci to hex + other (convience tools)
		-->Notes / Resources
			|
			-->Past writeups from other teamss
			|
			-->Tutorial slides
				|
				-->RPI slides
				|
				-->BinExp Indian guy slides














<h1>ALL BELOW WILL BE ORGANIZED LATER</h1>
<h1>PWN / REV Articles</h1>
<p>https://bitvijays.github.io/LFC-BinaryExploitation.html
https://css.csail.mit.edu/6.858/2017/readings/return-to-libc.pdf

http://www.paradyn.org/html/tools/unstrip.html</p>

<p>http://liveoverflow.com/</p>
<p>csaw365</p>
<p>	Learning:
		https://vplanetcoding.com/course1
		https://www.sololearn.com/Course/CPlusPlus/
	Debugging:
		http://www.pythontutor.com/visualize.html
</p>

https://inventory.rawsec.ml/tools.html

<h1>PS FOR PROJECT</h1>

*PROVIDES ONLINE ACCESS THROUGH DOCKERS*
-->What can i use django for?
-->Pick an OS and create a small docker with preset tools designed exactly for what is needed
-->Provide a preset ctf framework
-->Provide ftp functionaltiy
-->Provide login
Folder will look like
*writeups
	pastComp
		tamu
			rev/pwnetc
		pactf
			rev/crypto/etc
*Util
	crypto
		library with rsa/etc
	web
		bruteforces with hundreds of injects, cookies
		provides functionality to create your own post requests
	rev/pwn
		autoimports plugins designed for whatever the techonoloy is
		a link to the websites ftp server that has the ida program and other binaries
	Forensics
		Bruteforces and outputs things that worked into adove pdf
	Programming
		i dunno
		
		
		
		
		
		
		
		
		
		
		
TODO organize later 
create pwntools template --> make an os with the ctf template project prestalled along with dependancies and apps
https://github.com/nnamon/linux-exploitation-course
add pwn notes to command line
learn z3 and do pico
https://tuonilabs.wordpress.com --> really good writeups
https://ropemporium.com/ --> pwnable.kr --> reversing.kr
https://github.com/Naetw/CTF-pwn-tips
https://www.youtube.com/watch?v=NWPL5odSuLM
https://www.youtube.com/watch?v=5FJxC59hMRY
https://www.pwndiary.com
rpi modules
https://mmishou.wordpress.com/tutorials/
liveoverflow practice
make solver for revs
ie a brute forcer
create gdb cheatsheet for ctfs
	pattern_create 400 in.txt
	x/wx $rsp
	pattern_offset 0x41413741
	https://stackoverflow.com/questions/11506799/stack-resident-buffer-overflow-on-64-bit
	https://bytesoverbombs.io/exploiting-a-64-bit-buffer-overflow-469e8b500f10

echo ‘while true; do nc -vv -l -p 4444 -e ./ropasaurusrex; done’ > start.sh
bash start.sh

nm -D /lib/i386-linux-gnu/libc.so.6 | grep system
nm -D ./libc.so.6 | grep system
ldd ./ropasaurusrex
readelf -l ropasaurusrex
objdump -R ropasaurusrex
ROPgadget –binary ropasaurusrex –only “pop|ret”

inding the libc /bin/sh:
strings -tx libc.so.6 | grep “/bin/sh”

x64 --> rdi, rsi, rdx, rcx, r8, r9
x32 --> eax, ebx, ecx, edx, esi, edi, ebp
https://eli.thegreenplace.net/2011/09/06/stack-frame-layout-on-x86-64

gdb --command script.py ./executable.elf
(gdb) source script.py

use gdb with
pwndbg
peda
voltron

start gdb in diff versions of python
gdb --args python2 or python3

		
