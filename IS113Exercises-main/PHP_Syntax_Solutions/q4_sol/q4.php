<?php

$num = 20; // DO NOT MODIFY THIS

while ($num > 0) {
    if ($num % 3 == 0 && $num % 5 == 0) {
        echo "FIZZBUZZ";
    }
    else if ($num % 3 == 0) {
        echo "FIZZ";
    }
    else if ($num % 5 == 0) {
        echo "BUZZ";
    }
    
    echo "<br>";

    $num--;
}


?>