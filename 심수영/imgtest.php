<?php
	$db = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
	$sql = "SELECT image from stock_hye where company_name='CJ'";
	$sth = $db->query($sql);
	$result=mysqli_fetch_array($sth);
	echo '<img src="data:image/jpeg;base64,'.base64_encode($result['image']).'" width=20px; height=20px;/>';
?>