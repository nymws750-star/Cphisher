<?php
$file = 'logs.txt';
$ip = $_SERVER['REMOTE_ADDR'];
$ua = $_SERVER['HTTP_USER_AGENT'];
$date = date('Y-m-d H:i:s');
$data = "DATE: $date | IP: $ip | UA: $ua\n";
file_put_contents($file, $data, FILE_APPEND);
header('Location: 00');
exit;
?>