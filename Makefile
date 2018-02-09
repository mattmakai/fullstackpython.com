run:
	pelican -t theme -s settings.py -o generated/updated_site content
	cp -R static-html/* generated/updated_site/
	cp -R redirects/* generated/updated_site/
	cp -R static/* generated/updated_site/
	cp generated/updated_site/pages/* generated/updated_site/
	rm -rf generated/updated_site/pages/
	sed -i '' 's/\(^.*~~.*$$\)/<span class="highlight">\1<\/span>/g' generated/updated_site/blog/*.html
	sed -i '' 's/~~//g' generated/updated_site/blog/*.html


bookbuild:                                                                   
	pelican -t theme -s book_settings.py -o generated/book content
	cp -R static-html/* generated/book/
	cp -R static/* generated/book/
	rm -rf generated/book/pages


pdf: bookbuild
	sed -i '' 's/\(^.*~~.*$$\)/<span class="highlight-line">\1<\/span>/g' generated/book/pdf-book.html
	sed -i '' 's/"\/img\//"img\//g' generated/book/pdf-book.html
	sed -i '' 's/~~//g' generated/book/pdf-book.html
	cd generated/book; prince pdf-book.html -o full_stack_python.pdf



update:
	python update_s3.py
	rm -rf generated/current_site
	cp -R generated/updated_site generated/current_site


wc:
	wc content/pages/*/* content/posts/*


init:
	pip install -r requirements.txt
