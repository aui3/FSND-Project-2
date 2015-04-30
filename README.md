FSND- Project 2 Tournament Results
=============

<b>Steps to set up the developement enviroment</b>



1. Follow instructions <a href="https://www.udacity.com/wiki/ud088/vagrant">here </a> to install the virtual machine required to run this project. This virtual machine is configured using vagrant and provides the necessary environment setup to run the project.


2. Please make sure that you follow the instructions under "Run the virtual machine". At the command prompt run the following command

	a) <b>vagrant up</b>

	b) <b>vagrant ssh</b>

	c) <b>cd \vagrant</b>
 

2. You should now be connected to your vagrant machine and inside the folder <b>\vagrant</b>. Change directory to 'tournament' by 

	d) <b>cd \tournament</b>



3. Copy all source files from the project here. (This should be *tournament.py*, *tournament.sql* and *tournament_test.py*)



4. Set up the data base to for the project by connecting to psql. At the command prompt type:

	e) <b>psql</b> 



5. To set up the database and views at the command prompt run

	f) <b>\i tournament.sql</b>


6. Exit out of psql by (Ctrl +d)


7. At the command prompt run

	g) <b>python tournament_test.psql</b>




