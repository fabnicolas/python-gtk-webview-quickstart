# Python cross-platform desktop application quickstart
So, I was googling around how to make a cross-platform desktop application to use my website without rewriting the whole application from scratch in other languages and frameworks.

While doing that, I discovered Python and its syntax and ease of use.

I found out that Python has some WebView components that I could use to render ViStriker at the following URL: https://finalgalaxy.github.io/vistriker-FE/ . Let's give it a try!

TL;DR: ViStriker, focusing on frontend website, is a platform to watch YouTube videos in a different way, built by using Angular 4 and TypeScript and its components are based on Material Design Lite (Angular Material).

Angular 4 and TypeScript generates HTML/CSS/JS resources: the hope is that this WebView can render this application properly.

## What about this repository?
This project is a quickstart using GTK 3.0 and WebKit 3.0, using its WebView component along with GTK frame.

As stated above, the task is to run ViStriker not only in a browser but also in a separate window, a "client" that actually users can download and execute on Windows and main Linux distros (Currently I'm on Linux Mint 64 bit with XFCE desktop environment).

You can clone this repository and just change the following URL to give it a try for your personal project:
```python
        self.wview.load_uri('http://finalgalaxy.github.io/vistriker-FE/')
```
Below there are instruction to properly install dependencies and run this desktop app.

## Dependencies
On Linux, if you don't have python3 already installed (It's usually shipped with many Linux distros):
```
sudo apt-get install python3
```
To use pip for installing Python libraries, WebKit for WebView, setuptools and screeninfo to detect screen size:
```
sudo apt-get install python3-pip python-webkit python-webkit-dev
pip install setuptools
pip install screeninfo
```

## Run the app
```
python app.py
```
Done!

## Build the app
You can build this application with `cx_Freeze`, `py2exe`, `pyinstaller`, `niutka` or anything you want.
I tried `niutka` and I actually liked the concept of compiling source code to increase performance and make it harder to reverse-engineer it. But I found `pyinstaller` dead simple to build standalone executables.


Each solution has its pro and its cons.

Code is cross-platform, but compilation with `pyinstaller` is platform dependent.

To compile for Windows, you have to install `pyinstaller` on Windows and compile inside a Windows OS; in alternative you can run it on Wine.

To compile for Windows, by following this videos: https://www.youtube.com/watch?v=Rw5y7K2FBv0

Install Python and then do:
```
python pyinstaller.py -F app.py
```

To compile for Linux, just do it on Linux this way:
```
pip install pyinstaller
pyinstaller --onefile app.py
```
Executable is inside `/dist` folder (.gitignore already ignores files generated from `pyinstaller`).

## Removing screeninfo
By executing `pip install screeninfo`, you installed screeninfo Python library. This is not really needed for any WebView quickstart, but I found it useful myself.

The point is that, to center the window, I needed to calculate the screen size; this is a cross-platform way to do it.

If you don't wish to use this feature, comment those lines or remove them completely:
```python
...
from screeninfo import get_monitors
...
        screen_info=get_monitors()[0]
        ...
        window.move(screen_info.width/2 - self.size_width/2, screen_info.height - self.size_height/2) # Center window according to screen size and window size
```



## Are there other alternatives?
Yes; I'm testing some of them.

I tried to use Electron: https://github.com/Finalgalaxy/vistriker-FE-desktop/tree/master/electron . Electron did a really good job rendering ViStriker but the drawbacks are that, even if it is production-ready, even a simple application weights about 100 MB. I am trying to find a cheaper solution in terms of bundle size. That's why I'm trying to do experiments.

## Results
The WebView used for this project renders some components good and some other components badly.

Definitively it doesn't look like production-ready like Electron at the moment, but I'm still researching on the argument; this project might get tweaked for this particular use case.

What I come out with is:
![image](https://i.imgur.com/qXG9jW9.png)

![image](https://i.imgur.com/pjWdgM6.png)


## Personal conclusions
Some of the basic resources (HTML5/CSS3/JS) are loaded correctly inside WebView; links works; if you click a video it actually redirects to the video page and video loads. It looks very small, instead in Electron it takes the whole page as it should be.

Issues found about my use-case (As of 12/10/2017):
- Angular 4 Material "md-toolbar" doesn't render properly;
- Angular 4 Material "sidenav" opens but it doesn't close, also it overlays while navigating on other pages.
- YouTube embedded videos looks small.

Maybe with an additional CSS, loaded --- maybe injected --- after all page CSS, this might get fixed... but I wouldn't suggest to throw an Angular 4 website inside this component.

I would suggest it tho for basic websites like portfolio and blogs, since rendering complexity is reduced and this Python WebView may suit your use-case.
