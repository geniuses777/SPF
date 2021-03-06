<!DOCTYPE html>
<html>
<head>
  <title>SPF(Stock Price Forest)</title>
  <style>
    *{
      margin:0px;
      background-color:#ededed;
    }
    div * {
      background-color: white;
    }
    /*header*/
    .header{
      width:50%;
      margin:0 auto;
      height:140px;
      padding:10px;
      background-color: white;
      border-bottom: 1px solid #9e9e9e7a;
    }
    .header>.topDef{
      height:25%;
      width:100%;
      font-family: Arial, Helvetica, sans-serif;
    }
    .header>.topDef>#logo{
      width:30%;
      font-size: 25px;
      float:left;
      margin-left: 280px;
    }
    .header>.topDef>#logo>a:link { color: #03a9f4ad; text-decoration: none;}
    .header>.topDef>#logo>a:visited { color: #03a9f4ad; text-decoration: none;}
    .header>.topDef>#logo>a:hover { color: #03a9f4ad; text-decoration: none;}

    .header>.topDef>#login{
      width:10%;
      float: right;
    }
    .header>.topDef>#login>a:link { color: black; text-decoration: none;}
    .header>.topDef>#login>a:visited { color: black; text-decoration: none;}
    .header>.topDef>#login>a:hover { color: black; text-decoration: none;}
    .search{
      width: 100%;
      height: 60px;
    }
    .search>.blank{
      border:1px solid black;
      width:90%;
      height: 45px;
      font-size: 15px;
      margin:6px;
      padding-left: 10px;
    }
    .search>.img{
      height:35px;
    }
    .list{
      width: 100%;
      height: 50px;
    }
    .list>.list1{
      width:25%;
      height:80%;
      border-bottom: 3px solid black;
      float: left;
      text-align: center;
      font-size: 20px;
      font-weight: bold;
      padding-top: 13px;
    }
    .list>.list1>a:link{color: black; text-decoration: none;}
    .list>.list1>a:visited{color: black; text-decoration: none;}
    .list>.list1>a:hover{color: black; text-decoration: none;}

    .list>.list2>a>.item{
      width:25%;
      float: left;
      text-align: center;
      font-size: 20px;
      padding-top: 13px;
    }
    .list>.list2>a:link{color: black; text-decoration: none;}
    .list>.list2>a:visited{color: black; text-decoration: none;}
    .list>.list2>a:hover{color: black; text-decoration: none;}

    /*stock_graph*/
    .graph{
      width: 50%;
      height:260px;
      background-color: white;
      margin: 10px auto;
      padding: 10px;
      border-top: 1px solid #9e9e9e7a;
      border-bottom: 1px solid #9e9e9e7a;
    }
    .graph>.left{
      width: 50%;
      height: 100%;
      float: left;
      background-color: pink;
    }
    .graph>.right{
      width: 50%;
      height: 100%;
      float: right;
      background-color: yellow;
    }

    /*상승률&하락률*/
    .updown{
      width: 51.5%;
      height:300px;
      background-color: white;
      margin: 10px auto;
      border-top: 1px solid #9e9e9e7a;
      border-bottom: 1px solid #9e9e9e7a;
    }
    .updown>.wrapper{
        width: 100%;
    }
    .updown>.wrapper>.up{
        width: 50%;
        float: left;
        padding: 10px;
    }
    .updown>.wrapper>.up>#nav{
        width: 100%;
        height: 30px;
        padding-top:10px;
        padding-bottom: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        border-bottom: 2px solid black;
    }
    .updown>.wrapper>.up>.rank{
        width: 100%;
        height: 100%;
    }
    .updown>.wrapper>.up>.rank>.item{
        width: 100%;
        height: 40px;
    }
    .updown>.wrapper>.up>.rank>.item>.company{
        width: 70%;
        height: 100%;
        float: left;
    }
    .updown>.wrapper>.up>.rank>.item>.price{
        width: 30%;
        height: 100%;
        float: right;
    }
    .updown>.wrapper>.down{
        width: 50%;
        height: 100%;
        float: left;
    }
  </style>
</head>
<body>
  <!--header-->
    <div class="header">
      <div class="topDef">
        <div id="logo"><a title="Stock Price Forest" href="/">Stock Price Forest</a></div>
        <div id="login"></div>
        <form><input type="hidden" id="userID" value=""></form>
      </div>
      <form action="search.php" method="post">
        <div class="search">
          <input type="text" class="blank" name="company_name" placeholder="키워드, 종목명, 종목코드 검색">
          <input type="IMAGE" class="img" src="search.png" name="Submit" value="Submit"  align="absmiddle">
        </div>
      </form> 
      <div class="list">
        <div class="list2">
          <a href='javascript:void(0);' onclick="go_home();"><div class="item">홈</div></a>
        </div>
        <div class="list1">
          <a href='javascript:void(0);' onclick="go_trend();"><div class="item">증시동향</div></a>
        </div>
        <div class="list2">
          <a href="/news"><div class="item">뉴스</div></a>
          <a href="/mypage"><div class="item">마이페이지</div></a>
        </div>
      </div>
    </div>

    <!--stock_graph-->
    <div class="graph">
      <div class="left">
      </div>
      <div class="right">
      </div>
    </div>

    <!--상승률&하락률-->
    <div class="updown">
        <div class="wrapper">
            <div class="up">
                <div id="nav">상승률</div>
                <div class="rank">
                    <div class="item">
                        <div class="company"></div>
                        <div class="price"></div>
                    </div>
                </div>
            </div>
            <div class="down">
            </div>
        </div>
    </div>
</body>
</html>
<script>
    function newPop()
  {
    window.open('login.html', '_blank', 'width=470px,height=610px,toolbars=no,scrollbars=no');
  }

  var id = "";

  get_id();
  if(!id) {myHTML='<a href="login.html" onclick="newPop(); return false;">로그인</a>';}
  else {myHTML='<a href="trend.html?" onclick="return confirm('+'\''+'정말 로그아웃하시겠습니까?'+'\''+');">로그아웃</a>';}
  document.getElementById("login").innerHTML=myHTML;

  function check_login()
  {
    id = document.getElementById('userID').value;
    console.log(id);
    myHTML='<a href="trend.html?" onclick="return confirm('+'\''+'정말 로그아웃하시겠습니까?'+'\''+');">로그아웃</a>';

    document.getElementById("login").innerHTML=myHTML;
  }
  function check()
  {
    confirm('정말 로그아웃하시겠습니까?');
  }
  function go_trend()
  {
    location.href="trend.html?"+id;
  }
  function go_home()
  {
    location.href="index.html?"+id;
  }
  function get_id()
  {
    temp=location.href.split("?");
    data=temp[1].split(":");
    id=data[0];
    console.log(id);
  }
</script>

<?php
  $con = mysqli_connect("localhost","geniuses777","todolist123","geniuses777");

  $subject = $_GET['name'];
  $id=$_GET['id'];

  $sql="SELECT list from list join subject on list.subject = subject.name WHERE u_id='$id'";     // SELECT 구문을 통해 DB를 불러옵니다.

    $result=mysqli_query($con,$sql);

    $numrow = mysqli_num_rows($result);   //총 몇 개의 행을 불러왔는지 확인합니다.    

    for($i=0; $i<$numrow; $i++){                 //행(ROW) 수 만큼 

        $row[$i]=mysqli_fetch_array($result);     // mysql_fetch_array를 반복합니다.

    }    
    for($i = 0; $i < $numrow; $i++){             // mysql_fetch_array를 실행할 때마다 배열을 생성합니다. 

        $ListArr[$i] = $row[$i][0];  // $ComCodeArr[0]의 값이 IN_ComName 컬럼의 첫번째 값임을 정의 
    }

    for($i =0; $i<$numrow; $i++){
      echo $ListArr[$i];
    }

    //$arr = array_map(utf8_encode, $SubjectArr);
    //echo json_encode($arr);,JSON_UNESCAPED_UNICODE
    //echo json_encode($ListArr,JSON_UNESCAPED_UNICODE);
    $Arr222 = json_encode($ListArr,JSON_UNESCAPED_UNICODE);

    $sqll="SELECT name from subject where u_id='$id'";     // SELECT 구문을 통해 DB를 불러옵니다.

    $result2=mysqli_query($con,$sqll);

    $numrow = mysqli_num_rows($result2);   //총 몇 개의 행을 불러왔는지 확인합니다.    

    for($i=0; $i<$numrow; $i++){                 //행(ROW) 수 만큼 

        $row[$i]=mysqli_fetch_array($result2);     // mysql_fetch_array를 반복합니다.

    }    
    for($i = 0; $i < $numrow; $i++){             // mysql_fetch_array를 실행할 때마다 배열을 생성합니다. 

        $SubjectArr[$i] = $row[$i][name];  // $ComCodeArr[0]의 값이 IN_ComName 컬럼의 첫번째 값임을 정의 
    }

    /*for($i =0; $i<$numrow; $i++){
      $arr = array_map(utf8_encode, $SubjectArr);
    }*/

    //$arr = array_map(utf8_encode, $SubjectArr);
    //echo json_encode($arr);,JSON_UNESCAPED_UNICODE
    $Arr = json_encode($SubjectArr,JSON_UNESCAPED_UNICODE);


    echo $id; 
    header("Location: /home.php?id=".$id."&Arr=".$Arr."&Arr222=".$Arr222);
    //exit();

    mysqli_close($con);   

?>