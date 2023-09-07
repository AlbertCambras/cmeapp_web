<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
</head>

<body>
    <?php
        session_start();
        if (isset($_SESSION["mensaje"])) {
            echo "<p>" . $_SESSION["mensaje"] . "</p>";
            unset($_SESSION["mensaje"]); // Limpiar el mensaje para que no se muestre nuevamente
        }
    ?>

    <h1>Formulario</h1>
    <form action="get_data.php" method="post">
        <label for="dni">DNI:</label>
        <input type="text" id="dni" name="dni" required><br><br>

        <label for="name">Nombre:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="date">Fecha:</label>
        <input type="date" id="date" name="date" required><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>

</html>