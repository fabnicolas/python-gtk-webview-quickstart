# Python cross-platform desktop application quickstart
So, I just discovered Python and its syntax and ease of use.

I asked myself: does Python have a WebView component to render ViStriker from https://finalgalaxy.github.io/vistriker-FE/ ? Answer: yes.

TL;DR: ViStriker, focusing on frontend website, is a platform to watch YouTube videos in a different way, built by using Angular 4 and TypeScript and its components are based on Material Design Lite (Angular Material).

## What about this repository?
This project is a quickstart using GTK 3.0 and WebKit 3.0, using its WebView component along with GTK frame.

The task is to run ViStriker not only in a browser but also in a separate window, a "client" that actually users can download and execute on Windows and main Linux distros (Currently I'm on Linux Mint 64 bit with XFCE desktop environment).

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

Issues found about my use-case:
- Angular 4 Material "md-toolbar" doesn't render properly;
- Angular 4 Material "sidenav" opens but it doesn't close, also it overlays while navigating on other pages.
- YouTube embedded videos looks small.

Maybe with an additional CSS this might get fixed, but I wouldn't suggest to throw an Angular 4 website inside this component.
I would suggest it tho for basic websites like portfolio and blogs.

## Also...
Work in progress to add more data to this README.

Stay tuned :D
