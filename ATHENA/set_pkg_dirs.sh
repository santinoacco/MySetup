#! bin/sh


PKGNAME= $1
FULLRELEASE= $2

mkdir $PKGNAME && cd $PKGNAME;
mkdir $PKGNAME, build, run && cd build;
asetup $FULLRELEASE && cmake ../source/ && make;


