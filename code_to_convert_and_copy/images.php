<?php
    header("Content-Type: text/javascript");
    $AllowedExtensions = array(".gif", ".jpg", ".png", "jpeg");
    echo "var images = new Array();";
    $d = dir("./");
    while (false !== ($entry = $d->read()))
    {
        if($entry != '.' && $entry != '..' && is_file($entry) && in_array(substr($entry,-4), $AllowedExtensions))
        {
            echo "images.push('{$entry}');";
        }
    }
    $d->close();
?>