<?php
include('flag.php');
if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    highlight_file(__FILE__);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (!isset($_POST['query']))
        die('No query.');
    $query = $_POST['query'];
    if ($query == md5($query)) {
        echo $flag;
    } else {
        echo 'Hash does not match plain.';
    }
}
?>