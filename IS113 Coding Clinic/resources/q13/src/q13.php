<?php
    // PART A
    // You need to modify the array by adding the paths to the respective images.
    $pokemon_arr = [
        "Spiritomb" => "ADD_IMAGE_PATH_HERE",
        "Roserade" => "ADD_IMAGE_PATH_HERE",
        "Milotic" => "ADD_IMAGE_PATH_HERE",
        "Lucario" => "ADD_IMAGE_PATH_HERE",
        "Togekiss" => "ADD_IMAGE_PATH_HERE",
        "Porygon-Z" => "ADD_IMAGE_PATH_HERE"
    ];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Question 13</title>
</head>
<body>
    <h1>Pick the Pokemon that you want to send out to battle!</h1>
    <form method='POST' action='battle.php'>
        <table border='1'>
            <?php
                // PART B
                // Your CODE goes HERE

            ?>
        </table>
    </form>
</body>
</html>