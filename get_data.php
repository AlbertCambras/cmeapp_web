<?php
session_start();

// Verifica si se ha enviado el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtén los valores del formulario
    $dni = $_POST["dni"];
    $name = $_POST["name"];
    $date = $_POST["date"];

    $response = process_player($name, $dni, $date);

    if ($response !== false) {
        // Configura los encabezados para descargar el PDF
        header("Content-Type: application/pdf");
        header("Content-Disposition: attachment; filename=certificado.pdf");

        // Imprime el contenido del PDF
        echo $response;
        exit();
    } else {
        $_SESSION["mensaje"] = "Error al generar el PDF.";
    }
}

// Redirige de vuelta al formulario si algo salió mal
header("Location: index.php");
exit();

function process_player(string $dni, string $name, $date) {
    $data = array(
        'dni' => $dni,
        'name' => $name,
        'date' => $date
    );

    $data_json = json_encode($data);

    $service_url = 'http://localhost:5000/procesar'; // Reemplaza con la URL real del servicio

    $options = array(
        'http' => array(
            'method'  => 'POST',
            'header'  => 'Content-Type: application/json',
            'content' => $data_json
        )
    );

    $context = stream_context_create($options);

    $response = file_get_contents($service_url, false, $context);

    return $response;
}
?>
