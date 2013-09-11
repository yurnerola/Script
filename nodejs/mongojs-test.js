var databaseUrl="test"
var collections=["users"]
var db=require("mongojs").connect(databaseUrl,collections);

db.users.find({"name":"liu"},function(err,user_r){
	if(err||!user_r) console.log("No Result Found.");
	else user_r.forEach(function(user){
		console.log(user);
	});
});


db.users.save({email:"yurnerola@gmail.com",password:"123456",sex:"male"},function(err,saved){
	if(err||!saved) console.log("user not saved.")
	else console.log("User Saved.")
})


db.users.update({email:"yurnerola@gmail.com"},{$unset:{password:"123456"}},function(err,updated){
		if(err||!updated) console.write("Updated error~")
		else console.log("Update Sucess.")
})