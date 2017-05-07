[alt text](img/readme_img.jpg)

Python source code to configure html file that shows youtube trailers. 

## File structure
- `start.py`: It contains data of movies, page_title, page_comment, which 
	you can modify as [following](#to-set-movie-info).  
- `media.py`: It defines Movie class
- `generateHTML.py`: It generates trailer.html
- `trailer.html`: It is the generated html file
- js
  - `main.js`: This js helps trailer.html in interactive function
- css
  - `style.css`: This css helps trailer.html
- `LICENCE.txt`			
- `README.md`
- img
  - `readme\_img.jpg`: This image is for README.md

## Usage
#### To generate html file. 
Command line in Mac terminal: 
```
$ python start.py
```
This will generate trailer.html


#### To set page title 
Change `"Your page title"` to your page title in `start.py`
```python
page_title = "Your page title"
```

#### To set page content comment 
Change `"Your page comment"` to your page comment in `start.py`
```python
page_comment = "Your page comment"
```

#### To set Movie info
##### 1. Create Movie instances
```python
instance_name = media.Movie(arg1, arg2, arg3, arg4) 
```
- `arg1`: {string} movie title
- `arg2`: {string} movie description 
- `arg3`: {string} path to the movie image
- `arg4`: {string} Youtube trailer url 

#### 2. Add instance name to a list
```python
movies = [instance_name, instance_name2, instance_name3,....]
```

### To stye generated html
The site uses [bootstrap](http://getbootstrap.com/css/).
\n To modify, write over css in `css/style.css`


## Licence
[MIT Licence](https://choosealicense.com/licenses/mit/) © [Yukino Kohmoto](http://yukinokoh.github.io/portfolio/)



