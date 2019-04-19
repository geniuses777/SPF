<?php
    
    $con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
	if(mysqli_connect_errno($con))
	{
		echo "Failed to connect to MySQL: " .mysqli_connect_errno();
	}
	mysqli_set_charset($con,"utf8");
	
	$id=$_POST['id'];
	$password=$_POST['password'];
	$pwc=$_POST['pwc'];

	if($password!=$pwc){
	print "<script language=javascript> alert('비밀번호가 다릅니다'); location.replace('sign_up.html'); </script>";

	exit();
	}
	if($id==NULL || $password==NULL || $pwc==NULL){
	print "<script language=javascript> alert('빈칸을 다 채워주세요'); location.replace('sign_up.html'); </script>";
	exit();
	}
	$check = "SELECT * from member WHERE id='$id'";
	$aa=mysqli_query($con,$check);
	if($aa->num_rows==1){
	print "<script language=javascript> alert('중복된 아이디 입니다.'); location.replace('sign_up.html'); </script>";
	exit();

}

	$myp = "INSERT INTO member(id,password) VALUES('$id','$password')";
	$result=mysqli_query($con,$myp);  
	if($result){  
		print "<script language=javascript> alert('회원가입 성공'); onclick="self.close();" </script>";
    }  
    else{  
        print "<script language=javascript> alert('회원가입 실패 다시 시도해 주세요'); location.replace('sign_up.html'); </script>";
    } 
	
	mysqli_close($con);
?>
