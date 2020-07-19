# Customized Statisfactory mod starter project

New folder structure, that allows you to have all your mods in a single repository, making everything
easier to keep up to date.

    * Extensions
        * SML            Git submodule repository
            * Content
            * Source
        * MyMod1         Git submodule repository
            * Content
            * Source
        * MyMod2         Git submodule repository
            * Content
            * Source
    * Content
        * SML    -> Link to Extensions/SML/Content
        * MyMod1 -> Link to Extensions/MyMod1/Content
        * MyMod2 -> Link to Extensions/MyMod2/Content
    * Source
        * SML    -> Link to Extensions/SML/Source
        * MyMod1 -> Link to Extensions/MyMod1/Source
        * MyMod2 -> Link to Extensions/MyMod2/Source



# How to

## Use this repo as starter project

    git clone --recursive https://github.com/Delaunay/SatisfactoryModStarterProject

## Add the source of a mod

    # Add the repo to the project
    git submodule add <mod-repo> Extensions/<mod-name>
    
    # Add symlinks
    python uproject.py --sym-link 
    # OR manually
    mklink /D Content/<Mod> Extensions/<Mod>/Content
    mklink /D Source/<Mod> Extensions/<Mod>/Source
    
    # Add the mod to your build
    notepad++ Source/FactoryGame.Target.cs
    notepad++ Source/FactoryGameEditor.Target.cs
    
   
## Update a mod

    cd Extensions/<mod-to-update>
    git pull origin master
    
 
---

# SatisfactoryModLoader [![Build Status](https://ci.ficsit.app/job/SML2/job/master/badge/icon)](https://ci.ficsit.app/job/SML2/job/master/)
A tool used to load mods for the game Satisfactory. It's under development until Coffee Stain releases a proper Unreal modding API.

# Discord Server
Join our [discord server](https://discord.gg/QzcG9nX) to talk about SML and Satisfactory Modding in general.

# DISCLAIMER
This software is provided by the author "as is". In no event shall the author be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any 
theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.
