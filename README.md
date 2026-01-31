## alias-tts
Console text to speech program where you can create short forms for words.
[Pocket TTS](https://github.com/kyutai-labs/pocket-tts) was used for the TTS
## Installation
Simply install the program source code zip and unzip the file. 
## Program prerequisites
  * I mean you probably have to have python 3.x, I think anything 3.x is ok.
  * [Scipy](https://pypi.org/project/scipy/)
  * [sounddevice](https://pypi.org/project/sounddevice/)
  * [numpy](https://pypi.org/project/numpy/)
  * [Pocket TTS](https://pypi.org/project/pocket-tts/)
## Short forms and editing them
Basically the short forms are stored in alias.json in the format
```json
{
  "short form":"word",
  ...
}
```
For example if the short form DES were in alias.json like:
```json
{
  "DES":"descend and maintain",
  ...
}
```

Entering DES as text in the program, would cause the program to read it as "descend and maintain"

Feel free to create your own alias.json, just replace the file provided with your own file named alias.json with your short forms.

The default alias.json is for some goofy roblox atc server hence the terms in it.

## Running the program
Navigate to the project folder via console, then enter the command
```bash
python main.py
```
Then you should get the option to input text.

To input text not meant to be interpreted as a short form quote the text with quotation marks ("")

Eg. if EXP were short for "expect" and RWY short for "runway"

Then the input: 
```
"Bigjet" EXP RWY "2 for arrival"
```
Would be read as "Bigjet expect runway 2 for arrival"
## Macros
Sometimes the stuff you need to say is so predictable you might find yourself typing the same words in the same format every time. Macros can probably shorten this i guess.

Macros are stored in the file macros.json, again feel free to make your own but yea.

As an example of how they work here's the CLEARI macro in the default macros.json

```json
{
    "CLEARI":"CLR %s %s IC %s \"on Departure contact\" %s SQ %s EXP DEP RWY %s",
    ...
}
```
as you can see uh the macros can use short forms from the alias.json

and to use the macro in the program you can type:
```
"Smolplane" <CLEARI,"fictional location","via radar vectors to akmir thence as filed","2 thousand","fictional departure frequency",33>
```
and this would be read as

"Smolplane cleared to fictional location via radar vectors to akmir thence as filed initial climb 2 thousand, on departure contact fictional departure frequency, expect departure runway 33"

Basically for each %s in the macro, the %s is substituted with the respective text you put in the macro command thingy. (Ok this is basically me making python c style string formatting a "feature" but be for real its useful right trust)
## License
This project is carried by [Pocket TTS](https://github.com/kyutai-labs/pocket-tts) which is licensed under the MIT license.
