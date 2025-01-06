# midデータからxy座標へ変換

import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

# midデータ
mid = MidiFile() # 引数なしで呼び出すと、新しいファイルを作成できる
track = MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(150))) # bpm150
track.append(Message('program_change', program=26, time=0)) # Electric Guitar (jazz)
track.append(MetaMessage('track_name', name='Electric Guitar', time=0)) # track_nameの指定
track.append(Message('note_on', note=65, velocity=100, time=0))
track.append(Message('note_on', note=69, velocity=100, time=240))
track.append(Message('note_on', note=72, velocity=100, time=240))
track.append(Message('note_on', note=76, velocity=100, time=240))
track.append(Message('note_off', note=65, velocity=100, time=240))
track.append(Message('note_off', note=69, velocity=100, time=0))
track.append(Message('note_off', note=72, velocity=100, time=0))
track.append(Message('note_off', note=76, velocity=100, time=0))
track.append(Message('note_on', note=67, velocity=100, time=0))
track.append(Message('note_on', note=71, velocity=100, time=240))
track.append(Message('note_on', note=74, velocity=100, time=240))
track.append(Message('note_on', note=77, velocity=100, time=240))
track.append(Message('note_off', note=67, velocity=100, time=240))
track.append(Message('note_off', note=71, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=0))
track.append(Message('note_off', note=77, velocity=100, time=0))
track.append(Message('note_on', note=64, velocity=100, time=0))
track.append(Message('note_on', note=68, velocity=100, time=240))
track.append(Message('note_on', note=71, velocity=100, time=240))
track.append(Message('note_on', note=74, velocity=100, time=240))
track.append(Message('note_off', note=64, velocity=100, time=240))
track.append(Message('note_off', note=68, velocity=100, time=0))
track.append(Message('note_off', note=71, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=0))
track.append(Message('note_on', note=69, velocity=100, time=0))
track.append(Message('note_on', note=72, velocity=100, time=240))
track.append(Message('note_on', note=76, velocity=100, time=240))
track.append(Message('note_on', note=79, velocity=100, time=240))
track.append(Message('note_off', note=69, velocity=100, time=240))
track.append(Message('note_off', note=72, velocity=100, time=0))
track.append(Message('note_off', note=76, velocity=100, time=0))
track.append(Message('note_off', note=79, velocity=100, time=0))
track.append(Message('note_on', note=62, velocity=100, time=0))
track.append(Message('note_on', note=65, velocity=100, time=240))
track.append(Message('note_on', note=69, velocity=100, time=240))
track.append(Message('note_on', note=72, velocity=100, time=240))
track.append(Message('note_off', note=62, velocity=100, time=240))
track.append(Message('note_off', note=65, velocity=100, time=0))
track.append(Message('note_off', note=69, velocity=100, time=0))
track.append(Message('note_off', note=72, velocity=100, time=0))
track.append(Message('note_on', note=67, velocity=100, time=0))
track.append(Message('note_on', note=71, velocity=100, time=240))
track.append(Message('note_on', note=74, velocity=100, time=240))
track.append(Message('note_on', note=77, velocity=100, time=240))
track.append(Message('note_off', note=67, velocity=100, time=240))
track.append(Message('note_off', note=71, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=0))
track.append(Message('note_off', note=77, velocity=100, time=0))
track.append(Message('note_on', note=60, velocity=100, time=0))
track.append(Message('note_on', note=64, velocity=100, time=240))
track.append(Message('note_on', note=67, velocity=100, time=240))
track.append(Message('note_on', note=71, velocity=100, time=240))
track.append(Message('note_on', note=74, velocity=100, time=240))
track.append(Message('note_off', note=60, velocity=100, time=960))
track.append(Message('note_off', note=64, velocity=100, time=0))
track.append(Message('note_off', note=67, velocity=100, time=0))
track.append(Message('note_off', note=71, velocity=100, time=0))
track.append(Message('note_off', note=74, velocity=100, time=0))
track.append(MetaMessage('end_of_track', time=0)) # track終了

# midデータを取り出して辞書型の配列に直す
datas_mid = []

for midMessage in mid.tracks[0]:
    if hasattr(midMessage, 'note'):  # hasattrはオブジェクトに指定した属性(今回はnote)が存在するか確かめる関数
        entry = {"noteEnable": midMessage.type, "note": midMessage.note, "time": midMessage.time}
        datas_mid.append(entry)
# print(mids)


# timeの値を絶対的な値に修正
for i, data_mid in enumerate(datas_mid):
    if i >= 1:
        data_mid["time"] += datas_mid[i-1]["time"]
# print(mids_xy)


# midsの値をそれぞれnote→y座標, time用の長さ→x座標に変換したものに変える
SEMIQUAVER_VALUE = 120  # 音の長さを座標用に変換するためにtimeの値に割る数
MIDI_PITCH_ADJUST= 36  # 音の高さを座標用に調整するためにnoteの値に引く数

for data_mid in datas_mid:
    data_mid["time"] //= SEMIQUAVER_VALUE
    data_mid["note"] -= MIDI_PITCH_ADJUST
# print(mids_xy)


# midsの値からGUIのブロックにするための変換

# noteの値, on/offごとにソート
datas_mid.sort(key=lambda x: (x["note"], x["time"]))
# print(datas_mid)

# 合体
datas_xy =[]

for i, data_mid in enumerate(datas_mid):
    if(data_mid["noteEnable"] == "note_on"):
        entry = {"id": i//2 + 1, "left_x": datas_mid[i]["time"], "right_x": datas_mid[i+1]["time"], "y_pos": data_mid["note"]}
        datas_xy.append(entry)
print(datas_xy)