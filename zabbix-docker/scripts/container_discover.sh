#!/bin/bash

# get container list count
ZBX_CONTAINER_ARGS=`docker ps -q | wc -l`

OS_CHK=`uname`
case "${OS_CHK}" in
   "Linux")
            LIST=`docker ps -q | xargs -L1 docker inspect | jq ".[].Name" | sed 's/"//g' | sed 's/\///'` ;;
   *)
            echo "ZBX_NOTSUPPORTED"
            exit 1 ;;
esac

if [ "${LIST}" = "" ] ;then
    echo "ZBX_NOTSUPPORTED"
    exit 1
fi

echo "{"
echo "  \"data\":["
FIRST=1
for VER in ${LIST}
do
   if [ ${FIRST} -eq 1 ] ; then
      echo ""
      FIRST=0
   else
      echo ","
   fi
   echo -e -n "\t\t{ \"{#CONTAINERNAME}\":\"${VER}\" }"
done
echo ""
echo "  ]"
echo "}"
