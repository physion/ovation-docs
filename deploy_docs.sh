make clean
make html
git checkout gh-pages
cp -R build/html/* .
git commit -a -m "Deploying docs"
git push origin gh-pages
git checkout master