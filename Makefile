run:
	pelican -t theme -s settings.py -o generated/updated_site content
	cp -R static-html/* generated/updated_site/
	cp -R redirects/* generated/updated_site/
	cp -R static/* generated/updated_site/
	sed -i '' 's/\(^.*~~.*$$\)/<span class="highlight">\1<\/span>/g' generated/updated_site/pages/*.html 
	sed -i '' 's/\(^.*~~.*$$\)/<span class="highlight">\1<\/span>/g' generated/updated_site/blog/*.html
	sed -i '' 's/~~//g' generated/updated_site/pages/*.html 
	cp generated/updated_site/pages/* generated/updated_site/
	sed -i '' 's/~~//g' generated/updated_site/blog/*.html


prod: run
	rm -rf generated/updated_site/pages/
	sed -i '' 's/<span class="k">\(.[a-zA-Z0-9()_]*\)<\/span>/\1/g; s/<span class="n">\(.[a-zA-Z0-9 ()_]*\)<\/span>/\1/g; s/<span class="o">\(.[a-zA-Z0-9 ()_.~*=&;/-]*\)<\/span>/\1/g; s/<span class="p">\(.[][a-zA-Z0-9 ()_,&;:#{}]*\)<\/span>/\1/g; s/<span class="mi">\(.[0-9]*\)<\/span>/\1/g; s/<span class="sa">\(.[a-zA-Z0-9 ()_]*\)<\/span>/\1/g; s/<span class="vm">\(.[a-zA-Z0-9 ()_]*\)<\/span>/\1/g; s/<span class="ow">\(.[a-zA-Z0-9()_]*\)<\/span>/\1/g; s/<span class="nb">\(.[a-zA-Z0-9 ()_.]*\)<\/span>/\1/g; s/<span class="nd">\(.[a-zA-Z0-9 ()_.]*\)<\/span>/\1/g; s/<span class="ne">\(.[a-zA-Z0-9 ()_.]*\)<\/span>/\1/g; s/<span class="nn">\(.[a-zA-Z0-9 ()_.]*\)<\/span>/\1/g; s/<span class="kn">\(.[a-zA-Z0-9 ()_]*\)<\/span>/\1/g; s/<span class="bp">\(.[][a-zA-Z0-9 ()_,&;:#{}]*\)<\/span>/\1/g; s/<span class="nc">\(.[][a-zA-Z0-9 /()_,.&^;:+#{}*!%-]*\)<\/span>/\1/g; s/<span class="nf">\(.[][a-zA-Z0-9 /()_,.&^;:+#{}*!%-]*\)<\/span>/\1/g; s/<span class="fm">\(.[][a-zA-Z0-9 /()_,.&^;:+#{}*!%-]*\)<\/span>/\1/g; s/<span class="nt">\(.[][a-zA-Z0-9 /()_,.&^;:+#{}*!%-]*\)<\/span>/\1/g; s/<span class="s1">\(.[][a-zA-Z0-9 /()_,.&^\\\;:+#{}~*@`!?%-]*\)<\/span>/\1/g; s/<span class="si">\(.[][a-zA-Z0-9 /()_,.&^;:+#{}*!%-]*\)<\/span>/\1/g; s/<span class="sd">\(.[][a-zA-Z0-9 /()_,.&^\\\;:+#{}~*@`!?%-]*\)<\/span>/\1/g; s/<span class="s2">\(.[][a-zA-Z0-9 /\\\()_,.&$^;:+#{}|=~*@`!?%-]*\)<\/span>/\1/g; s/<span class="c1">\(.[][a-zA-Z0-9 /()_,.&^;:+#{}*@`!%-]*\)<\/span>/\1/g; s/<span class="o"><\/span>//g; s/<span class="s2"><\/span>//g' generated/updated_site/*.html generated/updated_site/blog/*.html


bookbuild:                                                                   
	mkdir -p tempcontent/pages
	cp -R content/pages/0* tempcontent/pages
	cp -R content/pages/meta tempcontent/pages
	python transform_book.py pdf
	pelican -t theme -s book_settings.py -o generated/book tempcontent
	cp -R static-html/* generated/book/
	cp -R static/* generated/book/
	rm -rf generated/book/pages
	rm -rf tempcontent


pdf: bookbuild
	sed -i '' 's/\(^.*~~.*$$\)/<span class="highlight-line">\1<\/span>/g' generated/book/pdf-book.html
	sed -i '' 's/"\/img\//"img\//g' generated/book/pdf-book.html
	sed -i '' 's/~~//g' generated/book/pdf-book.html
	cd generated/book; prince pdf-book.html -o full_stack_python.pdf


epub: bookbuild
	sed -i '' 's/\(^.*~~.*$$\)/<\/pre><pre class="highlight-line">\1<\/pre><pre>/g' generated/book/epub-book.html
	sed -i '' 's/"\/img\//"img\//g' generated/book/epub-book.html
	sed -i '' 's/~~//g' generated/book/epub-book.html
	cd generated/book; pandoc -f html epub-book.html -t epub3 --metadata title="Full Stack Python" --epub-metadata=epub-metadata.xml --epub-cover-image=img/book/cover-a4.jpg --toc-depth=3 --css=theme/css/epub.css -o full_stack_python.epub


mobi: epub
	cd generated/book; kindlegen full_stack_python.epub -o full_stack_python.mobi


update:
	python update_s3.py
	rm -rf generated/current_site
	cp -R generated/updated_site generated/current_site


wc:
	wc content/pages/*/* content/posts/*


init:
	pip install -r requirements.txt
