#!/usr/bin/env node

function route(handle,pathname,response){
	console.log("About to route a request for"+pathname);
	if(typeof handle[pathname]=="function"){
		handle[pathname](response);
	}else{
		console.log("No Request Handler for "+pathname);
		response.writeHead(404,{"Content-Type":"text/plain"});
		response.write("404 Not Found");
		response.end();
	}
}

exports.route=route;


	
