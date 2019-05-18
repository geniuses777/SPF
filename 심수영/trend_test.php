<?php
	$con = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");

	$sql="SELECT company_id, name from company";     // SELECT 구문을 통해 DB를 불러옵니다.

    $result=mysqli_query($con,$sql);

    $numrow = mysqli_num_rows($result);   //총 몇 개의 행을 불러왔는지 확인합니다.    

    for($i=0; $i<5; $i++){                 //행(ROW) 수 만큼 

        $row[$i]=mysqli_fetch_array($result);     // mysql_fetch_array를 반복합니다.

    }    
    for($i = 0; $i < 5; $i++){             // mysql_fetch_array를 실행할 때마다 배열을 생성합니다. 

        $IDArr[$i] = $row[$i][0];  // $ComCodeArr[0]의 값이 IN_ComName 컬럼의 첫번째 값임을 정의 
        $nameArr[$i] = $row[$i][1];
    }

    for($i =0; $i<5; $i++){
      echo $IDArr[$i];
      echo $nameArr[$i];
    }

    $Arr = json_encode($ListArr,JSON_UNESCAPED_UNICODE);

    mysqli_close($con);   

?>