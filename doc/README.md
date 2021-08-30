![architecture](https://insujang.github.io/assets/images/191110/electron-architecture.png)

* Electron uses `Chromium` and `Node.js` to package codes into an app for Windows, Linux, and macOS
* Electron uses 2 different types of processes:
  * `Main process`:
    * The main process, commonly a file named main.js, is the entry point to Electron app
    * It controls the life of the app, from open to close
    * It calls the native elements and creates each new renderer process in the app
      * Opening dialogs and other native operating system interactions 
  * `Renderer process`: 
    * Each web page that is created by the main script is rendered by a renderer process
    * The renderer process is a browser window in your app 
      * Unlike the main process, there can be multiple renderer processes and each is independent 
        * They can be hidden
        * Usually one is named index.html 
    * They're like typical HTML files but in Electron you have the whole Node API available here (unlike any web browser)

![2proc](https://cameronnokes.com/images/electron-apis-venn-diagram.png)

![2proc2](https://jlord.us/essential-electron/imgs/like-this.png)

## Chromium
* It is an open-source browser project that forms the basis for the Chrome web browser
* Google adds a number of closed-source features to the Chrome browser that Chromium lacks
  * AAC, H.264, and MP3 Support
  * Google Update
  * Extension Restrictions

## IPC
The main and renderer processes need to be able to communicate using IPC (Inter-Process Communication)

## Quick start
```
index.html
main.js
package.json
```

## Release 
```
electron-packager <sourcedir> <appname> --platform=<platform> --arch=<arch> [optional flags...]
```

* before we run `electron-packager`, we need to run `npm install` first
```
electron-packager . myapp --platform=mas --arch=x64
```


