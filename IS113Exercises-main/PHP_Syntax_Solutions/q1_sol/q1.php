<?php

function calculate_perimeter($length,$breadth) {
    return $length * 2 + $breadth * 2;
}

function calculate_area($length,$breadth) {
    return $length * $breadth;
}


// Do not change the $length and $breadth variables unless you are using your own test cases.
$length = 5;
$breadth = 10;

$perimeter = calculate_perimeter($length,$breadth); // Replace 0 with the function call to calculate perimeter using $length and $breadth
$area = calculate_area($length,$breadth); // Replace 0 with the function call to calculate area using $length and $breadth

// Expected Perimeter: 30
// Expected Area: 50
echo "The perimeter of the rectangle is $perimeter<br>";
echo "The area of the rectangle is $area";



?>