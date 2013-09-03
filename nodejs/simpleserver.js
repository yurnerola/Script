#!/usr/bin/env node
var http=require("http");
http.createServer(function(request,response){
	response.writeHead(200,{"Content-Type":"text/plain"});
	response.write("HelloWorld");
	console.log("---\n");
	response.end();
});
//}).listen(8888);
