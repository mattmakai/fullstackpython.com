run:
	cp static-html/* ..
	cp redirects/* ..
	pelican -t theme -s settings.py -o .. content
	cp ../pages/* ../
	cp ../theme/css/f.css ../
	cp -R ../theme/img ..
	rm -rf ../pages/
	rm -rf ../theme/css

init:
	pip install -r requirements.txt
