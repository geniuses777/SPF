<?php 
	$con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
    if(mysqli_connect_errno($con))
    {
        echo "Failed to connect to MySQL: " .mysqli_connect_errno();
    }
    mysqli_set_charset($con,"utf8");
	//$mysqli = new mysqli('localhost', 'root', 'wp0119', 'custom'); //mysql로 접근 하도록 설정
    $id = $_POST['id'];
    $password = $_POST['password'];
   

    $sql = "SELECT * FROM member WHERE id = '$id' AND password = '$password'"; //my sqli 연결의 끈을 생성시키고, 쿼리를 실행
      //고른다 모든것 member테이블로부터 id와 pwd가 일치하는 것을
    $res = mysqli_query($con,$sql); //실행결과는 $res에 저장
     
    if($res->num_rows==1){
       
        //header("Location: /subject_print22.php?id=".$id); 
    
    }  
    else{  
       print "<script language=javascript> alert('아이디 또는 비밀번호가 틀렸습니다.'); location.replace('index.html'); </script>";
      
    } 
   
 
?>