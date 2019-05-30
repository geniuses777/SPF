<?php
	$con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");

	$user = $_POST['user'];
	$company = $_POST['company'];

	//echo $user;
	//echo $company;

	$myp = "DELETE FROM interest where user = '$user' and name = '$company'";
	$result=mysqli_query($con,$myp);  
	if($result){  
		$sql = "UPDATE company set heart=heart-1 where name='$company';";
		$result2 = mysqli_query($con,$sql);
		print "<script language=javascript> alert('해당 관심종목이 삭제되었습니다.'); location.replace('mypage.html?id=$user');</script>";
    }  
    else{  
        print "<script language=javascript> alert('관심종목 실패 다시 시도해 주세요'); history.back(); </script>";
    } 
	
	mysqli_close($con);
?>