<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CMEApp</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

<body>
    <!-- Contenedor del formulario -->
    <div class="form-container">
        <?php
        session_start();
        if (isset($_SESSION["mensaje"])) {
            echo "<p>" . $_SESSION["mensaje"] . "</p>";
            unset($_SESSION["mensaje"]);
        }
        ?>

        <h1>Ingresar datos</h1>
        <form action="get_data.php" method="post">
            <label for="name">NAME:</label>
            <input type="text" id="name" name="name" required><br><br>

            <label for="name">DNI:</label>
            <input type="text" id="dni" name="dni" required><br><br>

            <label for="date">Fecha:</label>
            <input type="date" id="fecha" name="fecha" value="<?php echo date('Y-m-d'); ?>" ><br><br>

            <input type="submit" value="Enviar">
        </form>
    </div>
</body>

</html>
