In order to test the time taken by different AWS infrastructures, such as different sizes of EC2 instance and Lambda functions, I used the ssdeep and ppdeep Python modules to calculate the fuzzy hashes of 200 pdf e-books totalling about 5GB.
The experiments were carried out on Amazon Linux 2023 EC2 instances.  Before installing ssdeep it is necessary to run the following commands to install dependencies:

yum install gcc gcc-c++
yum groupinstall 'Development Tools'
yum install libffi-devel
yum install python3-pip
yum install python3-devel
yum install automake autoconf libtool
BUILD_LIB=1 pip install ssdeep

This repository contains a .zip file which was used to create the Lambda layer for the ssdeep package.  The ppdeep wrapper for ssdeep is a lot slower and this timed out when using a Lambda function as the maximum execution time is 15 minutes.
