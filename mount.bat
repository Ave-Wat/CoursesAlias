@ECHO OFF

set user=%1
set pass=%2

net use h:\\courses.ads.carleton.edu\courses /user:ads.carleton.edu\%user% %pass%
