<?php
$serialize=serialize('淘力网运营后台');
echo $serialize."<br>";
$unserialize=unserialize($serialize);
echo $unserialize;