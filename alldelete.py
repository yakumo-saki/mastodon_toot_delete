# !pip3 install Mastodon.py
# このコードは割と雑な作りで、エラーハンドリング等をしていません。
# だいたい動くと思いますがもう少しマシな実装を使った方がいいかもしれません。

from mastodon import Mastodon

# ユーザー設定→開発でアプリを登録することで以下の値を得ることができる
mastodon = Mastodon(
    access_token = 'your_access_token',
    client_id = 'your_client_id',
    client_secret = 'your_client_secret',
    api_base_url = 'https://instance.com'
)

account = mastodon.account_verify_credentials()

toots = mastodon.account_statuses(account)
for toot in toots:
    from time import sleep
    print(toot.id)
    mastodon.status_delete(toot)
    sleep(5)   # インスタンスへの負荷に応じて調整してください

# print('deleted first 20 toots')

next_toots = mastodon.fetch_next(toots)

while len(next_toots) != 0:
    for toot in next_toots:
        from time import sleep
        print(toot.id)
        sleep(5)   # インスタンスへの負荷に応じて調整してください
        mastodon.status_delete(toot)
        
    print("loop done")
    next_toots = mastodon.fetch_next(toots)

print("done")

