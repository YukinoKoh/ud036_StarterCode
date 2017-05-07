![screenshot of trailer.html](img/readme_img.jpg)

Python source code to configure html file that shows youtube trailers. 

## File structure
- `start.py`: It contains data of movies, page\_title, page\_comment, which 
	you can modify and use as [following](#to-set-movie-info).  
- `media.py`: It defines Movie class
- `generateHTML.py`: It generates trailer.html
- `trailer.html`: It is the generated html file
- js
  - `main.js`: This js helps trailer.html interactive function
- css
  - `style.css`: This css helps trailer.html on top of [bootstrap css](http://getbootstrap.com/css/)
- `LICENCE.txt`			
- `README.md`
- img
  - `readme\_img.jpg`: This image is for README.md

## Usage
### To generate html file 
Command line: 
```
$ python start.py
```
This will generate trailer.html

## To modify
### To set page title 
Change **"Your page title"** to your page title in `start.py`
```python
page_title = "Your page title"
```

### To set page content comment 
Change **"Your page comment"** to your page comment in `start.py`
```python
page_comment = "Your page comment"
```

### To set Movie info
1. Create Movie instances in `start.py`
```python
instance_name = media.Movie(arg1, arg2, arg3, arg4) 
```
- `arg1`: {string} movie title
- `arg2`: {string} movie description 
- `arg3`: {string} path to the movie image
- `arg4`: {string} Youtube trailer url 

2. Add instance name to a list in `start.py`
```python
movies = [instance_name, instance_name2, instance_name3,....]
```

## Licence
[MIT Licence](https://choosealicense.com/licenses/mit/) © [Yukino Kohmoto](http://yukinokoh.github.io/portfolio/)



