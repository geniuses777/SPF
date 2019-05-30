<?
$con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
	if(mysqli_connect_errno($con))
	{
		echo "Failed to connect to MySQL: " .mysqli_connect_errno();
	}
	mysqli_set_charset($con,"utf8");
 
$message = $_POST['message'];
 
if($message != "")
{
 $sql = "INSERT INTO `chat` VALUES('','$message')";
 mysql_query($sql);
}
 
$sql = "SELECT `Text` FROM `chat` ORDER BY `Id` DESC";
$result = mysql_query($sql);
 
while($row = mysql_fetch_array($result))
 echo $row['Text']."\n";
 
 
?>