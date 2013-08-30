#!/usr/bin/env node
var exec =require("child_process").exec;

function ls(response){
	console.log("Request handler 'ls' was  called.");
	exec("ls -lah",function(error,stdout,strerr){
		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write(stdout);
		response.end();
});
}

function find(response){
	console.log("Request  handler 'find' was called.");
	exec("find /",{timeout: 10000,maxBuffer:20000*1024},
	function(error,stdout,stderr){
		response.writeHead(200,{"Content-Type":"text/plain"});
		response.write(stdout);
		response.end();
	});
}

function upload(response){
	console.log("Request handler 'upload' was called.");
	response.writeHead(200,{"Content-Type":"text/plain"});
	response.write("HelloWorld");
	response.end();
}

var handle={};
handle["/"]=ls;
handle["/ls"]=ls;
handle["/find"]=find;
handle["/upload"]=upload;

exports.handle=handle;

