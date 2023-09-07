<?php
session_start();

// Verifica si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtén los valores del formulario
    $dni = $_POST["dni"];
    $name = $_POST["name"];
    $date = $_POST["date"];

    $response = process_player($name, $dni, $date);
    // Mensaje de éxito
    $_SESSION["mensaje"] = $response;

    // Redirige de vuelta al formulario
  //  header("Location: index.php");
    exit();
} else {
    // Redirige al formulario si no se ha enviado
   // header("Location: index.php");
    exit();
}

function process_player(string $dni, string $name, $date) {

    $data = array(
        'dni' => $dni,
        'name' => $name,
        'date' => $date
    );

    $data_json = json_encode($data);

    $service_url = 'http://127.0.0.1:5000'; // Reemplaza con la URL real del servicio

    $options = array(
        'http' => array(
            'method'  => 'POST',
            'header'  => 'Content-Type: application/json',
            'content' => $data_json
        )
    );

    $context = stream_context_create($options);

    $response = file_get_contents($service_url, false, $context);

    if ($response !== false) {
        return true;
    } else {
        return false;
    }
}

?>
