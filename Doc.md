
Prerequisite:
* You have the custom CSS UE4 installed
* You have visual studio installed
* You have the starter project downloaded and setup


# Hello World

0. In `SatisfactoryModLoader\Source\ExampleMod\ExampleModModule.cpp` add 
    `SML::Logging::warning(TEXT("Hello world"));` inside `void FExampleModModule::StartupModule()`
   
1. Make sure Visual studio is building `Shipping` not `Development` (the default) this is **critical**, 
    else only the editor version of it will be generated and it will not work.

2. Now when building you should see `<modfolder>\Binaries\Win64\UE4-ExampleMod-Win64-Shipping.dll` file being created,
   To test your code on the game you will have to copy it to the mod folder **every single time**. Alpakit only takes care of .uasset!
   
3. To avoid copying the file every single time it is recommended that you use a symlink
   Open cmd prompt on windows and type
   
   mklink `<Satisfactory folder>/mods/UE4-ExampleMod-Win64-Shipping.dll` `<modfolder>\Binaries\Win64\UE4-ExampleMod-Win64-Shipping.dll`

To get a readable stacktrace after segmentation fault also link the pdb file!
    
    mklink `<Satisfactory folder>/mods/UE4-ExampleMod-Win64-Shipping.pdb` `<modfolder>\Binaries\Win64\UE4-ExampleMod-Win64-Shipping.pdb`


4. Your mod folder structure should look like: 

    SteamLibrary\steamapps\common\Satisfactory\mods
        * ExampleMod.pak                     <-- Blueprints and assets
        * ExampleMod.sig                     <-- .pak sign (makes sure no corrumption happen
        * UE4-ExampleMod-Win64-Shipping.dll  <-- Your C++ Mod with C++ custom logic (Or symnlink)
    

5. In `SteamLibrary\steamapps\common\Satisfactory\configs\SML.cfg` enable logging 

    {
        "enableSMLCommands": true,
        "enableCrashReporter": true,
        "developmentMode": true,
        "debug": true,
        "consoleWindow": true,
        "dumpGameAssets": false,
        "enableCheatConsoleCommands": false
    }

If your setup is correct you should see in the logs:

    SatisfactoryModLoader: Warning: Loading development raw mod: SteamLibrary\steamapps\common\Satisfactory/mods/ExampleMod.pak
    SatisfactoryModLoader: Warning: Dependencies and versioning won't work!
    SatisfactoryModLoader: Warning: Loading development raw mod: SteamLibrary\steamapps\common\Satisfactory/mods/UE4-ExampleMod-Win64-Shipping.dll
    SatisfactoryModLoader: Warning: Dependencies and versioning won't work!

The .pak is loaded first then the dll.
The StartupModule() is called after the the Game engine is initialized (before main menu)


# Hooking

Now that you have your C++ dev environment setup properly you can hook into any functions.
Hooking is useful when you want to modify the behaviour of an object but you cannot override it because the object was defined in C++.

    void FExampleModModule::StartupModule() {
        SML::Logging::warning(TEXT("Registering Example Module"));

        SUBSCRIBE_METHOD(AFGCharacterPlayer::EquipEquipment, [](auto&, AFGCharacterPlayer* self, AFGEquipment* equipment) {
            // do some nice stuff there
            SML::Logging::warning(TEXT("EquipEquipment_BEFORE"));
        });

        SUBSCRIBE_METHOD_AFTER(AFGCharacterPlayer::EquipEquipment, [](AFGCharacterPlayer* self, AFGEquipment* equipment) {
            // do some nice stuff there
            SML::Logging::warning(TEXT("EquipEquipment_AFTER"));
        });
    }
    
    
NB: To see your C++ classes in the editor you must compile your code in `Development Editor` instead of shipping
 
    

