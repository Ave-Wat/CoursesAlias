#!/bin/bash

user=$1
pass=$2

net use h:\\courses.ads.carleton.edu\courses /user:ads.carleton.edu\$user
echo $pass
