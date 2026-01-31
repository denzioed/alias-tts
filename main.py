from pocket_tts import TTSModel
import scipy.io.wavfile
import json
import sounddevice as sd
import numpy as np
tts_model = TTSModel.load_model()
voice_state = tts_model.get_state_for_audio_prompt(
    "alba"
)
skip = True
arrays = {}
with open("alias.json") as f:
    d = json.load(f)
    for k,v in d.items():
        try:
            f = open(f'./audio/{k}.npy')
            f.close()
        except FileNotFoundError:
            audio = tts_model.generate_audio(voice_state, v)
            audio_arr = audio.numpy()[0:-6000]
            np.save(f'./audio/{k}.npy',audio_arr)
            arrays[k] = audio_arr
        else:
            arrays[k] = np.load(f'./audio/{k}.npy')
macros = {}
with open("macro.json") as f:
    macros = json.load(f)
sd.default.samplerate = tts_model.sample_rate*1.05
intended = [1,"CABLE Input (VB-Audio Virtual C, MME"]
sd.default.device = intended
def create_arr(text):
    arrays_to_concat = []
    buff = ""
    text_open = False
    macro_open = False
    for t in text:
        skip = False
        if (t == " " and not(text_open)) or (t=="\"") or (t in "<") or (t.isdigit() and not(text_open)) or macro_open:
            if macro_open:
                if t!=">":
                    buff+=t
                    continue
                else:
                    macro_open = False
                    arguments = buff.split(",")
                    macro_str = macros[arguments[0]]
                    arr = create_arr(macro_str%tuple(arguments[1:len(arguments)]))
            elif text_open:
                print(buff)
                arr = tts_model.generate_audio(voice_state, buff).numpy()
                text_open=False
                skip = True
            else:
                arr = arrays.get(buff,-1)
            if type(arr) is np.ndarray:
                arrays_to_concat.append(arr)
            buff = ""
            if t.isdigit():
                arrays_to_concat.append(arrays.get(t,-1))
        else:
            buff += t
        if t == "\"" and not(text_open) and not(skip):
            text_open = True
        if t == "<":
            macro_open=True
    arr = arrays.get(buff)
    if type(arr) is np.ndarray:
        arrays_to_concat.append(arr)
    return np.concatenate(arrays_to_concat,axis=0)
while True:
    txt = input("Input text here: ")
    if txt == "*":
        sd.stop()
        continue
    try:
        arr = create_arr(txt)
    except:
        continue
    sd.play(arr)