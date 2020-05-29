
<?php
//$command = escapeshellcmd('python C:/Users/SHREYANSH/Desktop/attack/keyss.py');
$output = shell_exec('python keyss.py');
var_dump($output);
echo "success";
?>