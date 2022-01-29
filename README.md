<h1>指でキャラクターを操作するゲーム</h1>
<ul>
  <li>numpy                 1.21.0</li>
  <li>pygame                2.0.1</li>
  <li>opencv-contrib-python 4.5.2.54</li>
  <li>opencv-python         4.5.2.54</li>
  <li>mediapipe             0.8.5</li>
</ul> 

<table>
    <thead>
        <tr>
            <th>file name</th>
            <th>contents</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>game.py </td>
            <td>キーボード入力でのゲーム</td>
        </tr>
      <tr>
            <td>cgame.py</td>
            <td>camera.pyで取得した座標を用いてキャラクターが移動するゲーム</td>
        </tr>
      <tr>
            <td>camera.py </td>
            <td>カメラで手のランドマークを取得しcgame.pyを動かすプログラム</td>
        </tr>
      <tr>
            <td>camera2.py</td>
            <td>カメラで手のランドマークを取得しflygame.pyを動かすプログラム</td>
        </tr>
      <tr>
            <td>flygame.py</td>
            <td>camera2.pyで取得したフラグを用いてキャラクターが上下移動するゲーム部分のプログラム</td>
        </tr>
      <tr>
            <td>enemy.py</td>
            <td>flygame.pyの敵について処理を行うプログラム</td>
        </tr>
      <tr>
            <td>item.py</td>
            <td>flygame.pyのアイテムについて処理を行うプログラム</td>
        </tr>
    </tbody>
</table>

<p><a href='https://maou.audio/bgm_neorock82/'</a>音源: 魔王魂</p>
