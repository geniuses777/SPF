<?php
	$conn = mysqli_connect("localhost","geniuses777","stock7840","geniuses777");
	Statement stmt = $conn.createStatement();
	ResultSet rs = stmt.executeQuery("SELECT image FROM stock_hye where company_name='CJ'");
	if (rs.next()) {
	// 바이너리 데이터를 저장하고 있는 컬럼으로부터 데이터를 가져온다
	InputStream in = rs.getBinaryStream("bfile");
	// BufferedImage를 생성하면 ImageIO를 통해 브라우저에 출력하기가 쉽다.
	BufferedImage bimg = ImageIO.read(in);
	in.close();

	ServletOutputStream sos = response.getOutputStream();

	ImageIO.write(bimg, "png", sos);
	}
	rs.close();
	stmt.close();
	conn.close();

	}
	catch(Exception e) {
	System.err.println(e);
	}
	}
	}
?>