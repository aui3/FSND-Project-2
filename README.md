FSND- Project 2 Tournament Results
=============

<b>Steps to set up the developement enviroment</b>



1. Please install a virtual machine to run the project. Follow instructions <a href=https://www.udacity.com/wiki/ud088/vagrant">here </a> to install the virtual machine. This virtual machine is configured using vagrant and provides the necessary environment setup to run the project.


2. Please make sure that you follow the instructions under "Run the virtual machine". At the command prompt Run

	*vagrant up* 

	*vagrant ssh* 

	browse to directory by *cd \vagrant*)
 

2. You should now be connected to your vagrant machine and inside the folder <b>\vagrant</b>. Change directory to 'tournament' by *cd \tournament*



3. Copy all source files from the project here. (This should be *tournament.py*, *tournament.sql* and #tournament_test.py*)


4. Open psql. Type *psql* on command prompt.



5. Run *\i tournament.sql* to set up the database and views


6. Exit out of psql by (Ctrl +d).


7. At the command prompt run *python tournament_test.psql*




