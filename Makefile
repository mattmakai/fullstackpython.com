run:
	pelican -t theme -s settings.py -o generated/updated_site content
	cp -R static-html/* generated/updated_site/
	cp -R redirects/* generated/updated_site/
	cp -R static/* generated/updated_site/
	cp generated/updated_site/pages/* generated/updated_site/
	rm -rf generated/updated_site/pages/
	sed -i '' 's/\(^.*~~.*$$\)/<span class="highlight">\1<\/span>/g' generated/updated_site/blog/*.html
	sed -i '' 's/~~//g' generated/updated_site/blog/*.html


update:
	python update_s3.py
	rm -rf generated/current_site
	cp -R generated/updated_site generated/current_site


init:
	pip install -r requirements.txt
