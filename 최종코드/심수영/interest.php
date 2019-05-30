<?php
    
    $con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
	if(mysqli_connect_errno($con))
	{
		echo "Failed to connect to MySQL: " .mysqli_connect_errno();
	}
	mysqli_set_charset($con,"utf8");
	
	$name=$_POST['company'];
	$user=$_POST['user'];

	/*echo $name;
	echo $user;*/

	$check = "SELECT * from interest WHERE user='$user' and name='$name'";
	$aa=mysqli_query($con,$check);
	if($aa->num_rows==1){
	print "<script language=javascript> alert('이미 관심종목 되어있습니다.'); history.back(); </script>";
	exit();
	}

	$myp = "INSERT INTO interest(user,name) VALUES('$user','$name')";
	$result=mysqli_query($con,$myp);  
	if($result){  
		print "<script language=javascript> alert('관심종목 되었습니다!!'); history.back(); </script>";
		$sql = "UPDATE company set heart=heart+1 where name='$name';";
		$result2 = mysqli_query($con,$sql);
    }  
    else{  
        print "<script language=javascript> alert('로그인해야합니다.'); history.back(); </script>";
    } 
	
	mysqli_close($con);
?>
