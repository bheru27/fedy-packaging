# fedy-packaging

Repository and packaging for Fedy

## Updating packages

* Place your source file under `SOURCES`
* Change version number in `SPECS/${packagename}.spec`
* Run `./build ${packagename}`
* Commit and push the changes

## Publishing updates to the repo

* On the VPS, run the following command,

```sh
cd /var/www/repo.folkswithhats.org; git pull; ./build --repo
```
