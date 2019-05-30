<?php
    
    $con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
	if(mysqli_connect_errno($con))
	{
		echo "Failed to connect to MySQL: " .mysqli_connect_errno();
	}
	mysqli_set_charset($con,"utf8");
	
	$id=$_POST['id'];
	$password=$_POST['password'];

	$check = "SELECT * from member WHERE id='$id' AND password='$password'";
	$aa=mysqli_query($con,$check);
	if($aa->num_rows==1){
		print "<script language=javascript>
		    setTimeout(function() {
		    window.opener.document.getElementById('userID').value = '$id'; 
		    opener.parent.check_login();
		    self.close(); //현재창 닫기
		    }, 1000); // 2초후 실행 1000당 1초
		</script>";
	}
	//window.opener.location.reload();
	//window.opener.document.getElementById('userID').value = '$id'; 
	//window.opener.location.href="javascript:check_login();";
	//opener.parent.check_login();
	else{  
        print "<script language=javascript> alert('아이디 또는 비밀번호가 틀렸습니다.'); location.replace('login.html'); </script>";
    } 
	
	mysqli_close($con);
?>
