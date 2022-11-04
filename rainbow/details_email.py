from django.core.mail import send_mail

def email_message(absolute_link, user_image, user_id_details,
 user_full_name_details, user_password_details, user_email_details):
    html_message = f"""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>world2 email</title>

<style>
""" + """ body {
    background-color: rgba(27,90,169);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;


}

.main_div {
width: 100%;
padding-top: 30px;
padding-bottom: 30px;
text-align: center;
color: white;
}

.my_image {
border-radius: 50px;
border: 4px solid white;
text-align: center;
box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(255, 255, 255, 0.2);
margin-bottom: 20px;
margin-top: 40px;
}


.table {
    width: 100%;
}

.table tr td {
    padding: 5px;
}

.table tr {
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(255, 255, 255, 0.2);
   
}
table tr:nth-child(odd) {
    background-color: rgb(110, 189, 0);
}



.logo-div h2, .logo-div img {
float: left;
color: white;
font-weight: bolder;
font-family: Tahoma;
}


@media screen and (max-width : 600px) {
.my_image {
    text-align: center;
}  
}

""" + f"""</style>
</head>
<body>
<div class="logo-div">
<img src="{user_image}" alt="" width="70" height="70">
<h2>World2</h2>
</div>
<div class="main_div">
<img src="HTML.jpg" alt="" width="70" height="70" class="my_image">


<p>welcome to world2, we're a real estate investment company, w're glad
to have you onboard, below are your registration details, click on 
the link below to confirm your email
</p>
<table class="table">
    <tbody>
        <tr>
            <td scope="row">User id</td>
            <td>{user_id_details}</td>
        </tr>

        <tr>
            <td scope="row">Full Name</td>
            <td>{user_full_name_details}</td>
        </tr>
        <tr>
            <td scope="row">email</td>
            <td>{user_email_details}</td>
        </tr>
        <tr>
            <td scope="row">Password</td>
            <td> <span id="password" class="hide">*************</span>  <button onclick="hidebutton()">hide/show</button></td>
        </tr>
    </tbody>
</table>

<h2>confirm email</h2>
<a href="{absolute_link}">{absolute_link}</a>
</div>

<script>
function hidebutton()""" + """ {
var Password_text = document.getElementById("password");

if (Password_text.classList.contains("hide")) {
Password_text.innerHTML = """ + f""" "{user_password_details}";
Password_text.classList.remove("hide"); """ + """ } else {
Password_text.innerHTML = "****************";   
Password_text.classList.add("hide");

}
}
""" + """
</script>
</body>
</html>
"""
    send_mail(subject= "Welcome to World2 real estate",
                message= " God is god",
                recipient_list = [user_email_details],
                html_message = html_message,
                from_email = "banabaz.sk@gmail.com"

            )

