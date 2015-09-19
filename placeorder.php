<?php
    header("content-type: application/json"); 
 	//A object to store in formation, will be send back to our website
 	//usr: username
 	//psw: password
 	//message: message(can be anything)
 	//total: account balance
 	//ctime: account creation time stamp


    $usr = $_POST['usr'];
    $psw = $_POST['psw'];
    $symbol = $_POST['symbol']; // Stock Symbol
    $priceType = $_POST['price'];    // price Type (string): market; limit; stop
    $transaction = $_POST['transaction'];   // transaction (string): buy; sell
    $duration = $_POST['duration']; //duration (string): Good till cancelled; Day order
    $amount = $_POST['quantity'];
    
    //MySQL section
    
	$servername = "mysql.serversfree.com";
	$username = "u463979611_tang";
	$password = "boilerup";
	$dbname = "u463979611_users";
	$conn = new mysqli($servername, $username, $password, $dbname);
	if ($conn->connect_error) {
    	$message="fail";
    	$total="111";
		$ctime="111";
    	die("Connection failed: " . $conn->connect_error);
	}
    
    /* ADD FETCH price from the database; assigned to priceDatabase*/
    
    $priceDatabase = 5.00
    $priceLimit = $priceDatabase
    $priceStop = $priceDatabase
    $profile = array("cash" => 5000000);
    
    switch($priceType){
        case "market":
            $price = $priceDatabase;
            switch($transaction){
                case "buy":
                    $profile["cash"] = $profile["cash"] - $price * $amount;
                    $profile[$symbol] = $amount;
                    break;
                case "sell":
                    $profile["cash"] = $profile["cash"] + $price * $amount;
                    $profile[$symbol] = $profile[$symbol] - $amount;
                    break;
            }
            break;
        case "limit":
            switch($transaction){
                case "buy":
                    if($price <= $priceLimit){
                        $profile["cash"] = $profile["cash"] - $price * $amount;
                        $profile[$symbol] = $amount;
                    }
                    break;
                case "sell":
                    if($price >= $priceLimit){
                        $profile["cash"] = $profile["cash"] + $price * $amount;
                        $profile[$symbol] = $profile[$symbol] - $amount;
                    }
                    break;
            }
            break;
        case "stop":
            switch($transaction){
                case "buy":
                    if($price >= $priceStop){
                        $profile["cash"] = $profile["cash"] - $price * $amount;
                        $profile[$symbol] = $amount;
                    }
                    break;
                case "sell":
                    if($price <= $priceLimit){
                        $profile["cash"] = $profile["cash"] + $price * $amount;
                        $profile[$symbol] = $profile[$symbol] - $amount;
                    }
                    break;
            }
            break;
    }
    
    /*
	$sql = 'SELECT psw, total, ctime FROM usrs WHERE usr="'. (string)$usr .'"';
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
		$row=$result->fetch_assoc();
	    $realpsw=(string)$row["psw"];
	    $amount=$row["total"];
	    $time=strval($row["ctime"]);
	    if ($realpsw==(string)$psw) {
	    	$message="login success";
	    	$total=$amount;
	    	$ctime=$time;
	    }
	    else{
	    	$message="wrong password";
	    	$total="111";
			$ctime="111";
	    }
	} else {
	    $message="account does not exist";
	   	$total="111";
		$ctime="111";
	}
	*/
	
    
    
    // This line will send the obeject back to our website
    
    
    
	// $dataArray=array('message'=>$message,'usr'=>$usr,'psw'=>$psw,'total'=>$total,'ctime'=>$ctime);
	// echo json_encode($dataArray);
    echo profile;
	$conn->close();

	exit();
?>
