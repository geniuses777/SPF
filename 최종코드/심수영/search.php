<?php 
    $con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
    if(mysqli_connect_errno($con))
    {
        echo "Failed to connect to MySQL: " .mysqli_connect_errno();
    }
    mysqli_set_charset($con,"utf8");

    $name = $_POST['company_name'];
    $user = $_POST['user'];
    
    if($name==NULL){
        print "<script language=javascript> alert('검색어를 입력해주세요.'); history.back(); </script>";
        exit();
    }

    //$check = "SELECT company_id from company WHERE name='$name'";

    $sql = "SELECT name from company WHERE name='$name'";

    $result=mysqli_query($con,$sql);
    $numrow = mysqli_num_rows($result); 

    if($numrow == 0){
        print "<script language=javascript> alert('존재하지 않습니다.'); history.back(); </script>";
        exit();
    }else{

      while ($row = mysqli_fetch_array($result)) {

        header("Location: /company.html?company=".$name."&id=".$user);
        }
    }

    mysqli_close($con);
 ?>
