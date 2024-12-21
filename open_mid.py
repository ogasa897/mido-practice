# 既存のmidファイル読み出して内部データを出力する
from mido import MidiFile

mid = MidiFile('sample_3track.mid')
print(mid)