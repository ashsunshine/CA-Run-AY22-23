<?php

    // You need to modify the array by adding the path to the respective images.
    $pokemon_arr = [
        "Spiritomb" => "../img/spiritomb.png",
        "Roserade" => "../img/roserade.png",
        "Milotic" => "../img/milotic.png",
        "Lucario" => "../img/lucario.png",
        "Togekiss" => "../img/togekiss.png",
        "Porygon-Z" => "../img/porygonZ.png"
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
                foreach ($pokemon_arr as $name => $img_link) {
                    echo "
                    <tr>
                        <td>
                            <img src='../img/pokeball.png'>
                        </td>
                        <td>
                            $name
                        </td>
                        <td>
                            <input type='checkbox' name='pokemon[]' value='$img_link'>
                        </td>
                    </tr>";
                }
                echo "<tr>
                    <td colspan='3'>
                        <input type='submit' value='Send Out'>
                    </td>
                </tr>"
            ?>
        </table>
    </form>
</body>
</html>