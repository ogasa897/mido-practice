# XY座標の値からnoteに変換してmidファイルを生成する

import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

datas_xy = [
    {'id': 1, 'left_x': 48, 'right_x': 64, 'y_pos': 24},
    {'id': 2, 'left_x': 32, 'right_x': 40, 'y_pos': 26},
    {'id': 3, 'left_x': 16, 'right_x': 24, 'y_pos': 28},
    {'id': 4, 'left_x': 50, 'right_x': 64, 'y_pos': 28},
    {'id': 5, 'left_x': 0, 'right_x': 8, 'y_pos': 29},
    {'id': 6, 'left_x': 34, 'right_x': 40, 'y_pos': 29},
    {'id': 7, 'left_x': 8, 'right_x': 16, 'y_pos': 31},
    {'id': 8, 'left_x': 40, 'right_x': 48, 'y_pos': 31},
    {'id': 9, 'left_x': 52, 'right_x': 64, 'y_pos': 31},
    {'id': 10, 'left_x': 18, 'right_x': 24, 'y_pos': 32},
    {'id': 11, 'left_x': 2, 'right_x': 8, 'y_pos': 33},
    {'id': 12, 'left_x': 24, 'right_x': 32, 'y_pos': 33},
    {'id': 13, 'left_x': 36, 'right_x': 40, 'y_pos': 33},
    {'id': 14, 'left_x': 10, 'right_x': 16, 'y_pos': 35},
    {'id': 15, 'left_x': 20, 'right_x': 24, 'y_pos': 35},
    {'id': 16, 'left_x': 42, 'right_x': 48, 'y_pos': 35},
    {'id': 17, 'left_x': 54, 'right_x': 64, 'y_pos': 35},
    {'id': 18, 'left_x': 4, 'right_x': 8, 'y_pos': 36},
    {'id': 19, 'left_x': 26, 'right_x': 32, 'y_pos': 36},
    {'id': 20, 'left_x': 38, 'right_x': 40, 'y_pos': 36},
    {'id': 21, 'left_x': 12, 'right_x': 16, 'y_pos': 38},
    {'id': 22, 'left_x': 22, 'right_x': 24, 'y_pos': 38},
    {'id': 23, 'left_x': 44, 'right_x': 48, 'y_pos': 38},
    {'id': 24, 'left_x': 56, 'right_x': 64, 'y_pos': 38},
    {'id': 25, 'left_x': 6, 'right_x': 8, 'y_pos': 40},
    {'id': 26, 'left_x': 28, 'right_x': 32, 'y_pos': 40},
    {'id': 27, 'left_x': 14, 'right_x': 16, 'y_pos': 41},
    {'id': 28, 'left_x': 46, 'right_x': 48, 'y_pos': 41},
    {'id': 29, 'left_x': 30, 'right_x': 32, 'y_pos': 43}
]
# print(datas_xy)


# 初めのx座標、終わりのx座標でそれぞれ(on/off, y座標, x座標)のセットに変える
# 座標の値をそれぞれy座標→note, x座標→time用の長さに変換したものに変える

SEMIQUAVER_VALUE = 120  # 音の長さをmidi用に変換するためにx座標の値に掛ける数
MIDI_PITCH_ADJUST= 36  # 音の高さをmidi用に調整するためにy座標の値に足す数
datas_noteXY =[]

for data_xy in datas_xy:
    entryLeft = {"noteEnable": "note_on", "y": data_xy["y_pos"] + MIDI_PITCH_ADJUST, "x": data_xy["left_x"] * SEMIQUAVER_VALUE}
    entryRight = {"noteEnable": "note_off", "y": data_xy["y_pos"] + MIDI_PITCH_ADJUST, "x": data_xy["right_x"] * SEMIQUAVER_VALUE}
    datas_noteXY.append(entryLeft)
    datas_noteXY.append(entryRight)
# print(datas_noteXY)


# x座標の値を基準にしてソート
datas_noteXY.sort(key=lambda x: x["x"])
# print(datas_noteXY)


# 一つ前の値との差をとり、x座標の値の部分をそれ用に書き換える
datas_note = []

for i, data_noteXY in enumerate(datas_noteXY):
    if i == 0:
        entry = {"noteEnable": data_noteXY["noteEnable"], "note": data_noteXY["y"], "time": data_noteXY["x"]}
        datas_note.append(entry)
    else:
        entry = {"noteEnable": data_noteXY["noteEnable"], "note": data_noteXY["y"], "time": datas_noteXY[i]["x"] - datas_noteXY[i-1]["x"]}
        datas_note.append(entry)
# print(datas_note)
    

# midのtrackにデータを入れる
VELOCITY = 100
bpm = 120

# midデータの作成 ここから
mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
# ここまでは本来ここで行わない

track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(bpm)))
for data_note in datas_note:
    track.append(Message(data_note["noteEnable"], note = data_note["note"], velocity = VELOCITY, time = data_note["time"]))
print(mid)

#midFileを保存
mid.save('test2.mid')