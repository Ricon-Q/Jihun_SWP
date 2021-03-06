 from cgi import parse_qs
 from SMtemplate import html
 
 def application(environ, start_response):
     d = parse_qs(environ['QUERY_STRING'])
     a = d.get('a', [''])[0]
     b = d.get('b', [''])[0]
     sum, mul =20203052, 20203052
     
	 try:
         a = int(a)
         b = int(b)
 
         sum = a + b
         mul = a * b
	 except ValueError:
		 sum = -999
		 mul = -999
     response_body = html % {
         'sum' : sum, 'mul' : mul
         }
     start_response('200 OK', [
         ('Content-Type', 'text/html'),
   	   	 ('Content-Length', str(len(response_body)))
     ])
    return [response_body]
