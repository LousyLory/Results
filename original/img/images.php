<div class="grid">
<ul class="images">
<?php
//path to directory to open
$directory = "./";
$dir_handle = @opendir($directory) or die("Unable to open folder");

while(false !== ($file = readdir($dir_handle)))
{
  if($file != '.' && $file != '..' && $file != 'Thumbs.db') 
  {
    echo "<li class='picture' title='Remote2'> <img src='/Media/pics/".$file."'alt='test'/></li>";                      
  }
}
closedir($dir_handle);
?>
