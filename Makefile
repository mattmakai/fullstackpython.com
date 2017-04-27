run:
	pelican -t theme -s settings.py -o generated/updated_site content
	cp -R static-html/* generated/updated_site/
	cp -R static/* generated/updated_site/
	cp generated/updated_site/pages/* generated/updated_site/
	rm -rf generated/updated_site/pages/

init:
	pip install -r requirements.txt
