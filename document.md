# mido

## 概要
pythonのmidiを扱うことができるライブラリ

## 入出力
### 読み込み
- 新規作成の場合
```python
mid = MidiFile()
```

- test.midファイルを読み込む場合
```python
mid = MidiFile('test.mid')
```

### 書き出し
- ' '内がファイル名になる
```python
mid.save('test.mid')
```

## Object
- mid(MidiFile) > tracks > track(MidiTrack) > MetaMessage, Message
### Message
#### note_on/off
- note_onでその音が始まる
- note_offでその音が終わる
#### channel
- トラック番号
#### note
- 音の高さ(ピッチ)
#### velocity
- 音の強さ
#### time
- timeの値は一つ前のMessageからどれだけ時間が離れているか
- 1920 = 1小節, 960 = 2分音符, 480 = 4部音符

### MetaMessage
#### bpmの設定
- デフォルト(設定しない場合)のbpmは120
- 以下のコードではbpmを200に設定できる
```python
track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(200)))
```

#### 音の設定
- nameで音の種類を設定できる
	- 例：piano1, piano2, Serum
```python
track.appned(MetaMessage('track_name', name='piano1', time=0))
```

#### 曲の終了
- timeで最後になった音からどれだけの時間無音を続けるか設定できる
- デフォルト(設定しない場合)はtime=0
```python
track.append(MetaMessage('end_of_track', time=0))
```