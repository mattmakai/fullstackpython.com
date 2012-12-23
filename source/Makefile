run:
	lessc --compress ./theme/less/custom.less > ./theme/static/css/c.css
	mkdir ./output
	mkdir ./output/static/
	cp -R theme/static/css theme/static/js theme/static/img output/
	cp -R static-html/* output/
	pelican -t theme -s settings.py content
	cp -R output/* ..
	rm -rf output/

init:
	pip install -r requirements.txt
