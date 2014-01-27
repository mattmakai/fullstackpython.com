run:
	mkdir ./output
	cp -R static-html/* output/
	pelican -t theme -s settings.py content
	cp output/pages/* output/
	rm -rf output/pages/
	cp -R output/* ..
	rm -rf output/

init:
	pip install -r requirements.txt
