# scrapbox_notify_slack

## 概要
Scrapboxの1週間分の更新件数をslackに通知する (月曜の昼の12時に通知)
ScrapboxのファイルはPrivateだとエラーを出します．
privateのものも通知するのであれば，こちらを参照: https://scrapbox.io/nishio/Scrapbox%E3%81%AEprivate%E3%83%97%E3%83%AD%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AEAPI%E3%82%92%E5%8F%A9%E3%81%8F

## 環境
```
python>=3.6.1
schedule>=1.0.0
slackweb>=1.0.5
requests>=1.0.4
```

## 使い方
- -url: 通知したいscrapboxのURL
- -slack: Slackの通知先のチャンネルのWebHooks　参考: https://sociocom.slack.com/apps/A0F7XDUAZ-incoming-webhooks


```python -url https://scrapbox.io/... -slack WebHooks-url ```

## 例
![image](sample.png)
