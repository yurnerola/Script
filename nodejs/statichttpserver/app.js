var http=require("http");
var url=require("url");
var fs=require("fs");
var path=require("path");
var mime=require("./mime").types;
var config=require("./config");
var zlib=require("zlib");


var server= http.createServer(function(request,response){
	var pathname=url.parse(request.url).pathname;
	var ext=path.extname(pathname);
	ext=ext?ext.slice(1):'unknown';
	if (ext.match(config.Expires.fileMatch)){
    	var expires = new Date();
    	expires.setTime(expires.getTime() + config.Expires.maxAge * 1000);
    	response.setHeader("Expires", expires.toUTCString());
    	response.setHeader("Cache-Control", "max-age=" + config.Expires.maxAge);
	}
	var contentType=mime[ext]||"text/plain";
	var realPath="assets"+pathname;
	fs.exists(realPath,function(exists){
		if(!exists){
			response.writeHead(404,{
				'Content-Type':'text/plain'
		});
		response.write("This request URL "+pathname+" was not found on this server.");
		response.end();
		}else{
			fs.readFile(realPath,"binary",function(err,file){
				if(err){
					response.writeHead(500,{
						'Content-Type':'text/plain'
					});
					response.end(err);
				}else{
					fs.stat(realPath,function(err,stat){
					var lastModified=stat.mtime.toUTCString();
					response.setHeader("Last-Modified",lastModified);
					console.log(lastModified);
					if(request.headers["if-modified-since"]&&lastModified==request.headers["if-modified-since"]){
						response.writeHead(304,"Not Mondifed");
						response.end();
					}else{
						response.writeHead(200,{
							'Content-Type':contentType});
						response.write(file,"binary");
						response.end();
					}
				});	
				}		
			});
		}
	});
}).listen(10000);
