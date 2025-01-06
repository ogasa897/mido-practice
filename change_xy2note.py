# XY座標の値からnoteに変換してmidファイルを生成する

import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

datas_xy = [
    {"id": 1, "left_x": 0, "right_x": 8, "y_pos": 29},
    {"id": 2, "left_x": 4, "right_x": 8, "y_pos": 36},
    {"id": 3, "left_x": 2, "right_x": 8, "y_pos": 33},
    {"id": 4, "left_x": 6, "right_x": 8, "y_pos": 40}
]
# print(datas_xy)


# 初めのx座標、終わりのx座標でそれぞれ(on/off, y座標, x座標)のセットに変える
# 座標の値をそれぞれy座標→note, x座標→長さをtime用の長さに変換したものに変える

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