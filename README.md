# Pi_Calculator by julien_Blue
This program calculates the value of Pi using the Chudnovsky Algorithm in an successive approximation.\n
Calculated value of Pi will be written to an automatically generated
external file (pi.txt) in the folder where the Pi_Calculator_(v.X.XX).py file is located.
pi.txt will be overwritten if it already exists.
Program will be interrupted if the Pi_Calculator.py file is stored in an write protected folder.

## v1.10 (26.03.2019)
	- implemented the Brent & Salamin algorithm due to more efficiency
	- inspired by DorFuchs
## v1.04 (19.09.2018)
	- output file will get it's name by the precision of pi
	- plus() returns the 's' variable to ensure proper context precision and roundings
	- sys module will only be imported to exit the program if an PermissionError occurs 

## v1.03 (10.08.2018)
	- Removed unnecessary exception while writing to external file
	- removed blank exception, only catching PermissionError if occurs when trying to open external file 

## v1.02 (17.04.2018)
	- Fixed measurement of time being unnecessarily accurate (17 decimal places)
	- Added more comments to the code

## v1.01 (20.03.2018)
	- Fixed program crash when Pi_Calculator.py file is executed in an write protected folder
	- Value of decimal digits can be set in console manually at program start

## v1.00 (**.02.2018)
	- Initial release

This changelog is inspired by the Pi_calculator(vX.XX).py file.
Hopefully this will help keep the releases tidy and understandable.
