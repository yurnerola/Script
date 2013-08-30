#!/usr/bin/env node
var exec =require("child_process").exec;

function start(response,postData){
	console.log("Request handler 'start' was called.");
	var body='<html>'+
					 '<head>'+
					 '<meta http-equiv="Content-Type" content="text/html;'+
					 'charset=UTF-8" />'+
					 '</head>'+
					 '<body>'+
					 '<form action="/upload" method="post">'+
					 '<textarea name="text" rows="20" cols="60"></textarea>'+
					 '<input type="submit" value="Submit text"/>'+
					 '</form>'+
					 '</body>'+
					 '</html>';
	response.writeHead(200,{"Content-Type":"text/html"});
	response.write(body);
	response.end();
}

function ls(response,postData){
	console.log("Request handler 'ls' was  called.");
	exec("ls -lah",function(error,stdout,strerr){
		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write(stdout);
		response.end();
});
}

function find(response,postData){
	console.log("Request  handler 'find' was called.");
	exec("find /",{timeout: 10000,maxBuffer:20000*1024},
	function(error,stdout,stderr){
		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write(stdout);
		response.end();
	});
}

function upload(response,postData){
	console.log("Request handler 'upload' was called.");
	response.writeHead(200,{"Content-Type":"text/plain"});
	response.write("U R send: " + postData);
	response.end();
}

var handle={};
handle["/"]=start;
handle["/ls"]=ls;
handle["/find"]=find;
handle["/upload"]=upload;

exports.handle=handle;

