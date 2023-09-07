<?php
session_start();

// Verifica si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtén los valores del formulario
    $dni = $_POST["dni"];
    $name = $_POST["name"];
    $date = $_POST["date"];

    $comando = "python3 -c 'from main.py import process; resultado = process(\"$dni\", \"$name\", \"$date\"); print(resultado)'";
    exec($comando, $output);
    $mensaje = implode("\n", $output);

    // Mensaje de éxito
    $_SESSION["mensaje"] = $mensaje;

    // Redirige de vuelta al formulario
    header("Location: index.php");
    exit();
} else {
    // Redirige al formulario si no se ha enviado
    header("Location: index.php");
    exit();
}
?>
