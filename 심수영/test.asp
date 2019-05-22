   <%@ LANGUAGE="VBSCRIPT" %>
   <%
   ' Clear out the existing HTTP header information
   Response.Expires = 0
   Response.Buffer = TRUE
   Response.Clear

' Change the HTTP header to reflect that an image is being passed.
   Response.ContentType = "image/jpg"

   Set cn = Server.CreateObject("ADODB.Connection")
   ' The following open line assumes you have set up a System DataSource by the name of myDSN.
   cn.Open "DSN=myDSN;UID=sa;PWD=;DATABASE=pubs"
   Set rs = cn.Execute("SELECT logo FROM pub_info WHERE pub_id='0736'")
   Response.BinaryWrite rs("logo")
   Response.End
   %>
