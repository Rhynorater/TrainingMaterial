#!/usr/bin/bash
if ! [ -x "$(command -v python)" ]; then
		python3 -m http.server 8000
else 
		python -m http.server 8000
fi 
