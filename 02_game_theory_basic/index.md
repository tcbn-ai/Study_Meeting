# ゲーム理論の基礎

ゲーム理論について、勉強会でいずれ話したいと思っています (2022/08/06時点)。

- 非協力ゲーム
  - 定義
  - 最適反応とナッシュ均衡
  - 混合戦略と混合戦略ナッシュ均衡
  - 数値計算
- 進化ゲーム

## 数値計算の環境
`virtualenv` で作成

```
python3 -m venv ~/.venvs/game_numerical
source ~/.venvs/game_numerical/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```