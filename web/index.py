#!/usr/local/bin/python3
print ("Content-Type: text/html")
print()

print ('''<!doctype html>
<html>
<head>
  <title>WEB1</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href ="index.html"tager="_blank">블로그</a></h1>
  <ol>
    <li><a href ="index.py?id=1page" tager="_blank">1page</a></li>
    <li><a href ="index.py?id=2page" tager="_blank">2page</a></li>
    <li><a href ="index.py?id=3page" tager="_blank">3page</a></li>
  </ol>
  <h2>title</h2>

  <p><iframe width="560" height="315" src="https://www.youtube.com/embed/skb_xHyuFaM"
    frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen></iframe></p>
  <p><a href="https://www.naver.com/"tager="_blank" title="html5 specification">The script’s input</a> is connected to the client too, and
  sometimes the form data is read this way; at other times
  the form data is passed via the “query string” part of
  the URL. This module is intended to take care of the
   different cases and provide a simpler interface to
   the Python script. It also provides a number of
   utilities that help in debugging scripts, and the
   latest addition is support for file uploads from a
   form (if your browser supports it).
  </p>
  <img src="coding.jpeg" width="80%">
  <p style="magin-top:200px;">
  The output of a CGI script should consist of two
  sections, separated by a blank line. The first
  section contains a number of headers, telling the
  client what kind of data is following. Python code
  to generate a minimal header section looks like this:
  </p>
  <p>
    <div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://blog-nhce5kz7af.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>

  </p>
  <!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/5c6a579977e0730ce0436ca8/default';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>
<!--End of Tawk.to Script-->
</body>
</html>

''')
