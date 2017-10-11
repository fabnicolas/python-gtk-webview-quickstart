# Python cross-platform application quickstart using WebView and GTK
So, I just discovered Python and its syntax and ease of use.

I asked myself: does Python have a WebView component to render ViStriker from https://finalgalaxy.github.io/vistriker-FE/ ? Answer: yes.

TL;DR: ViStriker, focusing on frontend website, is a platform to watch YouTube videos in a different way, built by using Angular 4 and TypeScript and its components are based on Material Design Lite (Angular Material).

## Why Python and WebView?
The task is to run ViStriker not only in a browser, but in a separate window, a "client" that actually users can download and execute on Windows and main Linux distros (Currently I'm on Linux Mint 64 bit with XFCE desktop environment).

## Are there other alternatives?
Yes. I tried to use Electron: https://github.com/Finalgalaxy/vistriker-FE-desktop/tree/master/electron . Electron did a really good job rendering ViStriker but the drawbacks are that, even if it is production-ready, even a simple application weights about 100 MB. I am trying to find a cheaper solution in terms of bundle size. That's why I'm trying to do experiments.

## So here comes Python GTK and WebKit.
Work in progress to add more data to this README.

Stay tuned :D
