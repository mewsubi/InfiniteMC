# InfiniteMC
Immortalizing the Minecraft Dimensions 20w14infinite Snapshot

## Goals
After the release of Minecraft's 20w14infinite Snapshot on April 1st, 2020, I've been playing the snapshot non-stop with my friends. Together, we've enjoyed exploring hundreds of different, randomly generated dimensions, and we want to keep the features alive, updated, and available in all future versions. I've started this project with the learning objective of better understanding the Minecraft source code, and to serve as a reference for anyone else interested in doing the same.

### Obtaining the Minecraft .jar files
There are several ways to go about obtaining the .jar for the server & client:  

- One way is to go to <https://mcversions.net/> and find the server.jar and client.jar for the version you're interested in
- Another way is to go to the .minecraft folder (Windows), and go to /versions and find the .jar file based on the version. There will also be a .json file, which will contain a link to server.jar

### Obsfucation
The Minecraft .jar files are obsfucated & optimized by a program called ProGuard. In essence, this means that the code is almost unreadable, as all variable, method, and class names will be coverted to nonsensical names like `a`, `aa`, `aaa`. However, this program also generates a .txt file containing the mappings from the nonsensical (obsfucated) names, back to the originals. These mappings can be found in the aforementioned .json file in the .minecraft/versions/<version> folder, and it will be called either `client.txt` or `server.txt`.
 
By using this tool by LXGaming <https://github.com/LXGaming/Reconstruct>, we can use the mappings on the client/server .jar files to turn them into their deobsfucated versions.

### Decompilation
There is a program called FernFlower that can be used to decompile the .jar files. First, we extract the .jar file to its own folder, then we obtain the FernFlower release that's used in Spigot. Since Spigot's BuildTools are used specifically to decompile Minecraft code, we can reasonably trust that it will be reliable with decompiling the .jar files we need. 
