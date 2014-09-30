# webshell

This is a little toy project, which uses
[websocketd](https://github.com/joewalnes/websocketd) to build an easy shell
in the browser. It allows you to run predefined commands and sends the output
back to the browser using websockets.

## Running `webshell`

From inside the project directory, having `websocketd` installed, you can run
it with:

```bash
$ websocketd --port=8888 --passenv=USER,HOME,PATH --staticdir=html/ ./webshell.py
```

## Security concerns

**You shouldn't make this publicly accessible!!!**

Use a normal webserver (nginx, apache ...) as a reverse proxy with a suitable
authentication method configured. [Follow these instructions for a cookie-based authentication using Nginx.](http://blog.pboehm.org/blog/2014/07/19/authentication-for-websockets/)

## Licence
Copyright (C) 2014 Philipp Böhm

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
