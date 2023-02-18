<?php
    if (!isset($_POST['pokemon'])) {
        header("Location: q13.php");
    }
    else {
        //var_dump($_POST['pokemon']);
        echo "<h1>You sent out: </h1>";
        $pokemon_img_array = $_POST['pokemon'];
        $i = 0;
        foreach ($pokemon_img_array as $pokemon_img) {
            echo "<img src='$pokemon_img'>";
            $i++;
            // If there are already 3 pokemon images in a row.
            if ($i == 3) {
                echo "<br>";
                $i = 0;
            }
        }
    }

?>