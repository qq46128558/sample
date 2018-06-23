#!/bin/bash
cd /data/httpd/ecstore/gitdev
git pull
cp -r * ..
/usr/local/php53/bin/php /data/httpd/ecstore/app/base/cmd update
echo 'Update Completed!'

